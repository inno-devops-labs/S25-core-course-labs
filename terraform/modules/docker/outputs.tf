
# Outputs
output "python_app_container_id" {
  description = "ID of the Python app Docker container"
  value       = docker_container.python_app.id
}

output "python_app_image_id" {
  description = "ID of the Python app Docker image"
  value       = docker_image.python_app.id
}

output "typescript_app_container_id" {
  description = "ID of the TypeScript app Docker container"
  value       = docker_container.typescript_app.id
}

output "typescript_app_image_id" {
  description = "ID of the TypeScript app Docker image"
  value       = docker_image.typescript_app.id
}
