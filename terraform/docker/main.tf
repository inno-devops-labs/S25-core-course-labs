terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
}

resource "docker_image" "app_image" {
  name = var.image_name
}

resource "docker_container" "app_container" {
  image = var.image_name
  name  = var.container_name
  
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}