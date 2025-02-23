output "container_name" {
  description = "Container name"
  value       = docker_container.nginx.name
}

output "container_ports" {
  description = "Container ports"
  value       = docker_container.nginx.ports
}
