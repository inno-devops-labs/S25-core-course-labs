terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}


provider "aws" {

  region = "us-east-1"
}

resource "aws_instance" "S25-core-course-labs" {
  instance_type = "t2.micro"
  ami           = "ami-04b4f1a9cf54c11d0"
}

