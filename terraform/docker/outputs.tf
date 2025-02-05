output "python_container_id" {
  description = "The ID of the Python container"
  value       = docker_container.python_container.id
}

output "node_container_id" {
  description = "The ID of the Node.js container"
  value       = docker_container.node_container.id
}

output "python_container_name" {
  description = "The name of the Python container"
  value       = docker_container.python_container.name
}

output "node_container_name" {
  description = "The name of the Node.js container"
  value       = docker_container.node_container.name
}

output "python_container_ip" {
  description = "The IP address of the Python container"
  value       = docker_container.python_container.network_data[0].ip_address
}

output "node_container_ip" {
  description = "The IP address of the Node.js container"
  value       = docker_container.node_container.network_data[0].ip_address
}

output "python_container_port" {
  description = "The exposed port of the Python container"
  value       = docker_container.python_container.ports[0].external
}

output "node_container_port" {
  description = "The exposed port of the Node.js container"
  value       = docker_container.node_container.ports[0].external
}

output "python_container_image" {
  description = "The image used for the Python container"
  value       = docker_container.python_container.image
}

output "node_container_image" {
  description = "The image used for the Node.js container"
  value       = docker_container.node_container.image
}

