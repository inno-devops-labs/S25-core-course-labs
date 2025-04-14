output "app_container_id" {
  description = "ID of web app Docker container"
  value       = docker_container.app_container.id
}

output "app_container_ports" {
  description = "Ports of web app Docker container"
  value       = docker_container.app_container.ports
}
