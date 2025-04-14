terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name         = "decafattic/moscow-time-app:latest"
  keep_locally = false
}

resource "docker_container" "python_app" {
  image = docker_image.python_app.image_id
  name  = "var.container_name"

  ports {
    internal = 8000
    external = var.external_port
  }
}

