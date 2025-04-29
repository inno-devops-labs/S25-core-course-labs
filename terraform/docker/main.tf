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
  image = var.docker_image_python
  name  = var.container_name_python
  ports {
    internal = var.internal_port_python
    external = var.external_port_python
  }
}
