output "container_name" {
  value = docker_container.devopsapp.name
}

output "container_image" {
  value = docker_container.devopsapp.image
}

output "container_port" {
  value = docker_container.devopsapp.ports
}