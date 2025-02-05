output "python_webapp_container_id" {
  description = "ID of the Python web application Docker container"
  value       = docker_container.python_webapp_container.id
}

output "python_webapp_container_ports" {
  description = "Ports of the Python web application Docker container"
  value       = docker_container.python_webapp_container.ports
}
output "go_webapp_container_id" {
  description = "ID of the Go web application Docker container"
  value       = docker_container.go_webapp_container.id
}

output "go_webapp_container_ports" {
  description = "Ports of the Go web application Docker container"
  value       = docker_container.go_webapp_container.ports
}
