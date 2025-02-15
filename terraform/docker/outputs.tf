output "image_id" {
    value = docker_image.nginx.name
}

output "container_id" {
    value = docker_container.nginx.name
}
