output "container_name" {
  description = "The name of the created Docker container"
  value       = docker_container.nginx.name
}

output "container_id" {
  description = "The ID of the created Docker container"
  value       = docker_container.nginx.id
}

output "image_name" {
  description = "The name of the Docker image"
  value       = docker_image.nginx.name
}

output "image_id" {
  description = "The ID of the Docker image"
  value       = docker_image.nginx.image_id
}
