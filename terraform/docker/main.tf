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

resource "docker_container" "custom_container_python" {
  image = var.python_docker_image
  name  = var.python_container_name
  ports {
    internal = var.python_internal_port
    external = var.python_external_port
  }
}
