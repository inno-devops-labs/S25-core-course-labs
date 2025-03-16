output "python_app_container_id" {
  description = "Container ID of the Python app container"
  value       = docker_container.python_app_container.id
}

output "python_app_container_ports" {
  description = "Ports of the Python app container"
  value       = docker_container.python_app_container.ports
}

output "go_app_container_id" {
  description = "Container ID of the Go app container"
  value       = docker_container.go_app_container.id
}

output "go_app_container_ports" {
  description = "Ports of the Go app container"
  value       = docker_container.go_app_container.ports
}
