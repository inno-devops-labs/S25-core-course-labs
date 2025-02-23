terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_container" "app_python" {
  image = var.application_image
  name  = var.container_name

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}

