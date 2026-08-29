terraform {
  required_version = ">= 1.15.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.60"
    }
  }
}

provider "aws" {
  region = var.aws_region
}


# VPC

resource "aws_vpc" "comicnerd_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name    = "comicnerd-vpc"
    Project = "ComicNerd"
  }
}


# Public Subnet

resource "aws_subnet" "comicnerd_public_subnet" {
  vpc_id                  = aws_vpc.comicnerd_vpc.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = var.availability_zone
  map_public_ip_on_launch = true

  tags = {
    Name    = "comicnerd-public-subnet"
    Project = "ComicNerd"
  }
}

# Internet Gateway

resource "aws_internet_gateway" "comicnerd_igw" {
  vpc_id = aws_vpc.comicnerd_vpc.id

  tags = {
    Name    = "comicnerd-igw"
    Project = "ComicNerd"
  }
}

# Route Table

resource "aws_route_table" "comicnerd_public_rt" {
  vpc_id = aws_vpc.comicnerd_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.comicnerd_igw.id
  }

  tags = {
    Name    = "comicnerd-public-rt"
    Project = "ComicNerd"
  }
}


# Route Table Association

resource "aws_route_table_association" "comicnerd_public_rta" {
  subnet_id      = aws_subnet.comicnerd_public_subnet.id
  route_table_id = aws_route_table.comicnerd_public_rt.id
}

# Security Group

resource "aws_security_group" "comicnerd_sg" {
  name        = "comicnerd-sg"
  description = "Security group for ComicNerd Kubernetes EC2"
  vpc_id      = aws_vpc.comicnerd_vpc.id

  # HTTP
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTPS
  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    description = "Allow outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "comicnerd-sg"
    Project = "ComicNerd"
  }
}

# IAM Role for EC2 / SSM

resource "aws_iam_role" "comicnerd_ec2_role" {
  name = "comicnerd-ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "ec2.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })

  tags = {
    Name    = "comicnerd-ec2-role"
    Project = "ComicNerd"
  }
}

resource "aws_iam_role_policy_attachment" "comicnerd_ssm_policy" {
  role = aws_iam_role.comicnerd_ec2_role.name

  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_role_policy_attachment" "comicnerd_cloudwatch_policy" {
  role = aws_iam_role.comicnerd_ec2_role.name

  policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"
}

resource "aws_iam_instance_profile" "comicnerd_instance_profile" {
  name = "comicnerd-instance-profile"

  role = aws_iam_role.comicnerd_ec2_role.name

  tags = {
    Name    = "comicnerd-instance-profile"
    Project = "ComicNerd"
  }
}

# Ubuntu AMI

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}


resource "aws_instance" "comicnerd_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "m7i-flex.large"
  subnet_id              = aws_subnet.comicnerd_public_subnet.id
  vpc_security_group_ids = [aws_security_group.comicnerd_sg.id]

  iam_instance_profile = aws_iam_instance_profile.comicnerd_instance_profile.name

  associate_public_ip_address = true

  root_block_device {
    volume_size           = 16
    volume_type           = "gp3"
    encrypted             = true
    delete_on_termination = true
  }

  tags = {
    Name    = "comicnerd-kubernetes-server"
    Project = "ComicNerd"
  }
}

# Elastic IP

resource "aws_eip" "comicnerd_eip" {
  domain = "vpc"

  tags = {
    Name    = "comicnerd-eip"
    Project = "ComicNerd"
  }
}

# Associate Elastic IP with EC2
resource "aws_eip_association" "comicnerd_eip_association" {
  instance_id   = aws_instance.comicnerd_server.id
  allocation_id = aws_eip.comicnerd_eip.id
}

