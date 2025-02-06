terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "python_app" {
  image = var.python_app_image
  name  = var.python_app_container_name
  ports {
    internal = 80
    external = 8000
  }
}

variable "python_app_image" {
  default = "netpo4ki/python-web:latest"
}

variable "python_app_container_name" {
  default = "python_app"
}

output "python_app_container_id" {
  value = docker_container.python_app.id
}