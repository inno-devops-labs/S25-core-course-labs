output "flask_app_container_id_output" {
  description = "ID of Docker container"
  value       = docker_container.flask_app_container.id
}

output "flask_app_container_ports_output" {
  description = "Internal and External Ports of Docker container"
  value       = docker_container.flask_app_container.ports
}