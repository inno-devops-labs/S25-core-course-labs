output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_python.id
}

output "docker_container_name" {
  description = "Name of the Docker container"
  value       = var.app_python_container
}

output "docker_image_name" {
  description = "Name of the Docker image"
  value       = var.app_python_docker_image_name
}
