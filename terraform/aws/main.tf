terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  
  region = "us-east-1"
} 

resource "aws_instance" "aws_vm" {
  instance_type = "t2.micro"
  ami = "ami-04b4f1a9cf54c11d0"

  tags = {
    Name = "Example"
  }
}