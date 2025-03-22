terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "app_python" {
  image = var.app_python_docker_image_name
  name  = var.app_python_container

  ports {
    internal = 8000
    external = 8000
  }
}
