output "container-name" {
  value = docker_container.flask_app_container.name
}

output "container-port" {
  value = docker_container.flask_app_container.ports
}

output "container-id" {
  value = docker_container.flask_app_container.id
}

output "container-image" {
  value = docker_container.flask_app_container.image
}