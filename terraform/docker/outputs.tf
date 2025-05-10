output "container_id" {
  description = "ID of container"
  value = docker_container.app_python.id
}

output "image_id" {
  description = "ID of image"
  value = docker_container.app_python.image
}