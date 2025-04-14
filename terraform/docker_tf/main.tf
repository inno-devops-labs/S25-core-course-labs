terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "py_app" {
  image = var.py_app_image
  name  = var.py_app_container_name
  ports {
    internal = var.py_app_internal_port
    external = var.py_app_external_port
  }
}

