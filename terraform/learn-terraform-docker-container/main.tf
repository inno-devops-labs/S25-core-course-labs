terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8000
  }
}

output "container_id" {
  description = "The ID of the created Docker container"
  value       = docker_container.nginx.id
}

output "container_name" {
  description = "The name of the created Docker container"
  value       = docker_container.nginx.name
}

output "container_port" {
  description = "The exposed port of the Docker container"
  value       = docker_container.nginx.ports[0].external
}

