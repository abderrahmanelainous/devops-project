variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "Ubuntu 22.04 LTS AMI ID for us-east-1"
  type        = string
  default     = "ami-00de3875b03809ec5"
}

variable "instance_type" {
  description = "EC2 instance type - t2.micro is free tier eligible"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Name of the EC2 key pair"
  type        = string
  default     = "devops-project-key"
}

variable "project_name" {
  description = "Project name used for tagging resources"
  type        = string
  default     = "devops-project"
}
