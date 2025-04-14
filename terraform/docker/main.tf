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
  name = "python:3.11"
}

resource "docker_image" "node_app" {
  name = "node:18"
}

resource "docker_container" "python_container" {
  name  = var.python_container_name
  image = var.python_image_name
  ports {
    internal = 5000
    external = 5001
  }
}

resource "docker_container" "node_container" {
  name  = var.node_container_name
  image = var.node_image_name
  ports {
    internal = 3000
    external = 3000
  }
}

