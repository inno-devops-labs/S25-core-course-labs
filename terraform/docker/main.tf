terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "custom_image" {
  name = "achulakov/lab2"
}

resource "docker_container" "custom_container" {
  image = docker_image.custom_image.name
  name  = var.container_name
  ports {
    internal = 5000
    external = 8000
  }
}


