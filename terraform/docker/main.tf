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
  name = "nginx:latest"
}

resource "docker_container" "moscow_time" {
  image = var.app_python_docker_image
  name  = var.app_python_docker_container

  ports {
    internal = var.app_python_internal_port
    external = var.app_python_external_port
  }
}
