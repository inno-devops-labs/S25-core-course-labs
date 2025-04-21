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


output "container_name_typescript" {
  value = docker_container.app_typescript_container.name
}

output "container_id_typescript" {
  value = docker_container.app_typescript_container.id
}

output "container_image_typescript" {
  value = docker_container.app_typescript_container.image
}

output "container_port_typescript" {
  value = docker_container.app_typescript_container.ports
}