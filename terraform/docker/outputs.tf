output "app_container_id" {
  description = "Container ID of the app container"
  value       = docker_container.app_container.id
}

output "app_container_ports" {
  description = "Ports of the app container"
  value       = docker_container.app_container.ports
}
