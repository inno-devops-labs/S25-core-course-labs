output "py_container_id" {
  description = "id of the Python docker container"
  value       = docker_container.moscow_time.id
}

output "py_container_ports" {
  description = "used ports of Python docker container"
  value       = docker_container.moscow_time.ports
}