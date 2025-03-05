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

resource "docker_container" "time_app_py" {
  image = var.app_python_docker_image
  name  = var.app_python_docker_container

  ports {
    internal = var.app_python_internal_port
    external = var.app_python_external_port
  }
}
