terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0058f736afded77b3"  
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}

