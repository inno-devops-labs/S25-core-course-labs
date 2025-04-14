output "python_container_name" {
  value = docker_container.custom_container_python.name
}

output "python_container_id" {
  value = docker_container.custom_container_python.id
}

output "python_container_image" {
  value = docker_container.custom_container_python.image
}

output "python_container_port" {
  value = docker_container.custom_container_python.ports
}
