output "aws-public-ip" {
  value = aws_instance.my-terraform-server.public_ip
}