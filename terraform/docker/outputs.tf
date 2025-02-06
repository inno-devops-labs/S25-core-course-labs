output "python_container_id" {
  description = "The ID of the Python container"
  value       = docker_container.python_container.id
}

output "python_container_name" {
  description = "The name of the Python container"
  value       = docker_container.python_container.name
}

output "python_container_image" {
  description = "The image used for the Python container"
  value       = docker_container.python_container.image
}
