output "container_id_py" {
  description = "ID of the Python Docker container"
  value       = docker_container.python_app.id
}

output "image_id_py" {
  description = "ID of the Python Docker image"
  value       = docker_image.python_app.id
}


output "container_id_node" {
  description = "ID of the Node.js Docker container"
  value       = docker_container.node_app.id
}

output "image_id_node" {
  description = "ID of the Node.js Docker image"
  value       = docker_image.node_app.id
}
