output "container_name_python" {
  value = docker_container.flask-app.name
}

output "container_id_python" {
  value = docker_container.flask-app.id
}

output "container_image_python" {
  value = docker_container.flask-app.image
}

output "container_port_python" {
  value = docker_container.flask-app.ports
}
