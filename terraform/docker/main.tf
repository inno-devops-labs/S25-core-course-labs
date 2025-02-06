terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "my_container" {
  name  = var.docker_container_name
  image = var.docker_image
  ports {
    internal = 5000
    external = 8000
  }
}
