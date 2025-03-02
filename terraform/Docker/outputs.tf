output "container_name" {
  value = docker_container.app_container.name
}

output "container_port" {
  value = docker_container.app_container.ports
}

output "container_id" {
  value = docker_container.app_container.id
}

output "container_image" {
  value = docker_container.app_container.image
}