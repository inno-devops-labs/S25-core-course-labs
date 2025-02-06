output "container_name" {
  value = docker_container.nginx.name
}

output "container_id" {
  value = docker_container.nginx.id
}
