output "container_id_piton" {
  description = "ID of the Piton Docker container"
  value       = docker_container.app_piton.id
}

output "image_id_piton" {
  description = "ID of the Piton Docker image"
  value       = docker_image.app_piton.id
}

output "container_id_flutter" {
  description = "ID of the Flutter Docker container"
  value       = docker_container.app_flutter.id
}

output "image_id_flutter" {
  description = "ID of the Flutter Docker image"
  value       = docker_image.app_piton.id
}
