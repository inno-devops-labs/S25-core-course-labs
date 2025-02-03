output "container_name_python" {
  value = docker_container.app_python_container.name
}

output "container_id_python" {
  value = docker_container.app_python_container.id
}

output "container_image_python" {
  value = docker_container.app_python_container.image
}

output "container_port_python" {
  value = docker_container.app_python_container.ports
}

output "container_name_ruby" {
  value = docker_container.app_ruby_container.name
}

output "container_id_ruby" {
  value = docker_container.app_ruby_container.id
}

output "container_image_ruby" {
  value = docker_container.app_ruby_container.image
}

output "container_port_ruby" {
  value = docker_container.app_ruby_container.ports
}
