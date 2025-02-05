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

variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "tutorial"
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}