variable "aws_region" {
  description = "AWS region where ComicNerd will be deployed"
  type        = string
  default     = "ap-south-1"
}

variable "availability_zone" {
  description = "Availability Zone for the public subnet"
  type        = string
  default     = "ap-south-1a"
}

variable "vpc_cidr" {
  description = "CIDR block for ComicNerd VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

