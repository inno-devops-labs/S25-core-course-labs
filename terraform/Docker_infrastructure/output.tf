output "container_name" {
  value = docker_container.nginx.name
  description = "The name of the Docker container."
}

output "container_id" {
  value = docker_container.nginx.id
  description = "The unique ID of the Docker container."
}

output "image_id" {
  value = docker_image.nginx.image_id
  description = "The ID of the Docker image used by the container."
}

output "container_ports" {
  value = docker_container.nginx.ports
  description = "The port mappings configured for the container."
}