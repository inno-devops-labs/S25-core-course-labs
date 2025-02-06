output "python_container_id" {
  description = "The ID of the Python container"
  value       = docker_container.app_python_container.id
}

output "javascript_container_id" {
  description = "The ID of the JavaScript container"
  value       = docker_container.app_javascript_container.id
}
