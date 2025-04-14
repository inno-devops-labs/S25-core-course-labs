
output "python-container-id" {
  description = "ID of the Python web application Docker container"
  value       = docker_container.app_python.id
}

output "python-container_ports" {
  description = "Ports of the Python web application Docker container"
  value       = docker_container.app_python.ports
}