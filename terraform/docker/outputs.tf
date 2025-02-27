output "name_of_container" {
  value = docker_container.custom_container.name
}

output "port_of_container" {
  value = docker_container.custom_container.ports
}

output "id_of_container" {
  value = docker_container.custom_container.id
}

output "image_of_container" {
  value = docker_container.custom_container.image
}