provider "aws" {
    region = "us-east-1"
    access_key = var.access_key
    secret_key = var.secret_access_key
    token = var.session_token
}

resource "aws_instance" "my_vm" {
    instance_type = "t2.micro"
    ami           = "ami-04b4f1a9cf54c11d0"

    tags = {
        Name = "MyInstance1"
    }
}