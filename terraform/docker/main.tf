terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
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
    external = 8080
  }
}


variable "container_name" {
  default = "my-nginx-container"
}

output "container_name" {
  value = docker_container.nginx.name
}

output "container_id" {
  value = docker_container.nginx.id
}

output "image_name" {
  value = docker_image.nginx.name
}

output "image_id" {
  value = docker_image.nginx.image_id
}

