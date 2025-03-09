output "container_id" {
  value       = docker_container.python_app.id
}

output "image_id" {
  value       = docker_image.python_app.id
}