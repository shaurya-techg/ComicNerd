output "vpc_id" {
  description = "ComicNerd VPC ID"
  value       = aws_vpc.comicnerd_vpc.id
}

output "public_subnet_id" {
  description = "ComicNerd public subnet ID"
  value       = aws_subnet.comicnerd_public_subnet.id
}

output "internet_gateway_id" {
  description = "ComicNerd Internet Gateway ID"
  value       = aws_internet_gateway.comicnerd_igw.id
}

output "ec2_role_name" {
  description = "IAM role attached to the ComicNerd EC2 instance"
  value       = aws_iam_role.comicnerd_ec2_role.name
}

output "instance_profile_name" {
  description = "EC2 instance profile for ComicNerd"
  value       = aws_iam_instance_profile.comicnerd_instance_profile.name
}

output "elastic_ip" {
  description = "Stable public IP address for ComicNerd"
  value       = aws_eip.comicnerd_eip.public_ip
}
