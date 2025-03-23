terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}


provider "docker" {}

resource "docker_image" "python_app" {
  name         = "nickolaus899/python-msk-time:latest"
  keep_locally = false
}

resource "docker_image" "node_app" {
  name         = "nickolaus899/js-cities-dist:latest"
  keep_locally = false
}

resource "docker_container" "python_app" {
  name  = var.py_container_name
  image = docker_image.python_app.image_id
  ports {
    internal = 50
    external = 5000
  }
}


resource "docker_container" "node_app" {
  name  = var.node_container_name
  image = docker_image.node_app.image_id
  ports {
    internal = 30
    external = 3000
  }
}
