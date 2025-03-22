output "container_id" {
  value = docker_container.python_app.id
}

output "container_status" {
  value = docker_image.python_app.id
}

output "container_ports" {
  value = docker_container.python_app.ports
}
