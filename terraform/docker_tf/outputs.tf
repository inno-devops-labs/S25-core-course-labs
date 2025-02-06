output "custom_container_name" {
  value = docker_container.nginx.name
}

output "custom_container_id" {
  value = docker_container.nginx.id
}

output "custom_container_image" {
  value = docker_container.nginx.image
}
