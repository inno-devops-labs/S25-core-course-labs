output "python_app_container_id" {
  description = "ID of the Docker container for python app"
  value       = docker_container.python_app.id
}

output "python_ports" {
  value = docker_container.python_app.ports
}
