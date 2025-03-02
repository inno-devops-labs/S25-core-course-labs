output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_python.id
}

output "container_image" {
  description = "Image name of the Docker image"
  value       = docker_container.app_python.image
}

output "container_name" {
  description = "Name of the Docker container"
  value       = docker_container.app_python.name
}

