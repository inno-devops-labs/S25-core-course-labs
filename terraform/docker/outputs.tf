output "go_container_id" {
  description = "id of the Go application docker container"
  value       = docker_container.number_facts_app.id
}

output "go_container_ports" {
  description = "used ports of Go application docker container"
  value       = docker_container.number_facts_app.ports
}

output "python_container_id" {
  description = "id of the Python application docker container"
  value       = docker_container.moscow_time_app.id
}

output "python_container_ports" {
  description = "used ports of Python application docker container"
  value       = docker_container.moscow_time_app.ports
}

