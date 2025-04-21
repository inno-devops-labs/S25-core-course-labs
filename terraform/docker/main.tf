terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app" {
  name         = "mirgasimovk/python-msk:latest"
  keep_locally = false
}

resource "docker_container" "app" {
  image = docker_image.app.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8000
  }
}
