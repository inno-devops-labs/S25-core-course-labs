terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "python_app" {
  image = var.python_app_image
  name  = var.python_container_name

  ports {
    internal = 80
    external = var.python_ext_port
  }
}
