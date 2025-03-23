output "container_name" {
  description = "Name of the deployed Docker container"
  value       = docker_container.flask_app.name
}

output "container_id" {
  description = "ID of the deployed Docker container"
  value       = docker_container.flask_app.id
}

output "container_image" {
  description = "Docker image used for the container"
  value       = docker_container.flask_app.image
}

output "container_ports" {
  description = "Ports mapping of the deployed container"
  value = {
    internal = docker_container.flask_app.ports[0].internal
    external = docker_container.flask_app.ports[0].external
  }
}

output "container_ip" {
  description = "IP address of the running container"
  value       = docker_container.flask_app.network_data[0].ip_address
}
