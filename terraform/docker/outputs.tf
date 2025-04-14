output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.python_app.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.python_app.id
}
