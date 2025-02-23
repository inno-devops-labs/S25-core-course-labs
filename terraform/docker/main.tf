terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name         = "jodak628286/python_app:latest"
  keep_locally = false
}

resource "docker_container" "python_app" {
  image = docker_image.python_app.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = 8000
  }
}

output "python_app_image_name" {
  value = docker_image.python_app.name
}

output "python_app_container_name" {
  value = docker_container.python_app.name
}

output "python_app_container_exposed_port" {
  value = docker_container.python_app.ports[0].external
}
