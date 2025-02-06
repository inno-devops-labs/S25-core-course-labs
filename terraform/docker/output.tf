output "my_container_name" {
  value = docker_container.nginx.name
}

output "my_container_id" {
  value = docker_container.nginx.id
}

output "my_container_image" {
  value = docker_container.nginx.image
}
