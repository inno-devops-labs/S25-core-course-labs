output "python_container_id" {
  description = "Python webapp container's id"
  value       = docker_container.python_container.id
}

output "python_container_name" {
  description = "Python webapp container's name"
  value       = docker_container.python_container.name
}

output "python_container_image" {
  description = "Python webapp container image"
  value       = docker_container.python_container.image
}