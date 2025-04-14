output "container_name" {
  value = docker_container.moscow_time_app.name
}

output "container_image" {
  value = docker_container.moscow_time_app.image
}

output "container_port" {
  value = docker_container.moscow_time_app.ports
}