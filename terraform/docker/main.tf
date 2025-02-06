terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
  required_version = ">= 1.3.0"
}

provider "docker" {}

resource "docker_container" "app_python" {
  image = var.app_image
  name  = var.container_name
  ports {
    internal = 80
    external = 8080
  }
}
