output "contain_name" {
  value = docker_container.nginx.name
  description = "The name of the Docker container"
}

output "container_id" {
  value = docker_container.nginx.id
  description = "The ID of the Docker container"
}
