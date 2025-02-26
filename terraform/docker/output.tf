output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.image_id
}

output "container_name" {
  description = "Name of the Docker container"
  value       = var.container_name
}

output "container_ports" {
  description = "Port mappings for the container"
  value       = docker_container.nginx.ports
}