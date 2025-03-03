output "container_name_python" {
  value = docker_container.moscow_time_python.name
}

output "container_id_python" {
  value = docker_container.moscow_time_python.id
}

output "container_image_python" {
  value = docker_container.moscow_time_python.image
}

output "container_port_python" {
  value = docker_container.moscow_time_python.ports
}

output "container_name_rust" {
  value = docker_container.moscow_time_rust.name
}

output "container_id_rust" {
  value = docker_container.moscow_time_rust.id
}

output "container_image_rust" {
  value = docker_container.moscow_time_rust.image
}

output "container_port_rust" {
  value = docker_container.moscow_time_rust.ports
}