terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "app_python" {
  image = var.app_python_image
  name  = var.app_python_container_name
  ports {
    internal = 5000
    external = 8000
  }
}

variable "app_python_image" {
  default = "demakoder/app_python:latest"
}

variable "app_python_container_name" {
  default = "app_python"
}

output "app_python_container_id" {
  value = docker_container.app_python.id
}