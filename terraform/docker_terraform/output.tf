output "python_container_info" {
  value = {
    name       = docker_container.python_app.name
    ip_address = docker_container.python_app.network_data[0].ip_address
    ports      = docker_container.python_app.ports
  }
  description = "python docker container information output"
}

output "golang_container_info" {
  value = {
    name       = docker_container.golang_app.name
    ip_address = docker_container.golang_app.network_data[0].ip_address
    ports      = docker_container.golang_app.ports
  }
  description = "golang docker container information output"
}
