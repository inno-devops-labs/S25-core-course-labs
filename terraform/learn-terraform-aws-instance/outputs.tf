 output "instance_id" {
  description = "i-03d8f517e09075ba8"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "52.24.191.183"
  value       = aws_instance.app_server.public_ip
}
