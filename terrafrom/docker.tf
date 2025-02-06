terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "web" {
  name  = var.container_name
  image = "nginx:latest"
  ports {
    internal = 80
    external = 8080
  }
}

variable "container_name" {
  description = "Name of the Docker container"
  default     = "terraform-nginx"
}
