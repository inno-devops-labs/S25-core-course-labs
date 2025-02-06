output "container_id" {
  description = "ID of Docker container"
  value       = docker_container.app_python.id
}

output "image_id" {
  description = "ID of Docker image"
  value       = docker_image.app_python.id
}