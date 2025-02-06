terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name         = "${var.docker_hub_username}/devopslabs:latest"
  keep_locally = false
}

resource "docker_container" "python_app" {
  image = docker_image.python_app.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = var.external_port
  }

  restart = "always"
}