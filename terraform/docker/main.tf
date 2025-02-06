terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}

provider "docker" {}

variable "container_name" {
  default = "my-nginx-container"
}

resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "nginx" {
  name  = var.container_name
  image = docker_image.nginx.image_id
  ports {
    internal = 80
    external = 8080
  }
}

output "container_name" {
  value = docker_container.nginx.name
  description = "Container's name"
}

output "container_ip" {
  value = docker_container.nginx.network_data[0].ip_address
  description = "Container's IP"
}

output "container_image" {
  value = docker_container.nginx.image
  description = "Container's image"
}
