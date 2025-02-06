terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_python" {
  name         = "saleemasekrea/app_python:latest"
  keep_locally = true
}

resource "docker_container" "app_python" {
  name  = var.python_container_name
  image = docker_image.app_python.image_id
  ports {
    internal = var.app_python_internal_port
    external = var.app_python_external_port
  }
}
