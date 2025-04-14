terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

output "container_id" {
  value = docker_container.nginx.id
}

output "container_name" {
  value = docker_container.nginx.name
}

output "container_port" {
  value = docker_container.nginx.ports[0].external
}

variable "container_name" {
  default = "my-nginx-container"
}

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
