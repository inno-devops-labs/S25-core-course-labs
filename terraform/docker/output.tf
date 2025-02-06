output "container_name_python" {
  value = docker_container.custom_container_python.name
}

output "container_id_python" {
  value = docker_container.custom_container_python.id
}

output "container_image_python" {
  value = docker_container.custom_container_python.image
}

output "container_port_python" {
  value = docker_container.custom_container_python.ports
}

output "container_name_go" {
  value = docker_container.custom_container_go.name
}

output "container_id_go" {
  value = docker_container.custom_container_go.id
}

output "container_image_go" {
  value = docker_container.custom_container_go.image
}

output "container_port_go" {
  value = docker_container.custom_container_go.ports
}