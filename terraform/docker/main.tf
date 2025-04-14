terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "moscow_time" {
  image = var.py_image
  name  = "moscow-time"
  ports {
    internal = 8000
    external = var.py_external_port
  }
}

