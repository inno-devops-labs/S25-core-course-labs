output "nginx_container_id" {
  description = "The ID of the created NGINX Docker container"
  value       = docker_container.nginx.id
}

output "nginx_container_name" {
  description = "The name of the created NGINX Docker container"
  value       = docker_container.nginx.name
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.id
}
