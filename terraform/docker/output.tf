output "container_name" {
  value = docker_container.app_container.name
}

output "container_image" {
  value = docker_container.app_container.image
}

output "container_port" {
  value = docker_container.app_container.ports
}
