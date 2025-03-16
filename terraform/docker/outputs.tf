output "container_name_python" {
  value = docker_container.moscow-time-app.name
}

output "container_id_python" {
  value = docker_container.moscow-time-app.id
}

output "container_image_python" {
  value = docker_container.moscow-time-app.image
}

output "container_port_python" {
  value = docker_container.moscow-time-app.ports
}