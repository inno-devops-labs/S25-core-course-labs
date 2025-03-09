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

resource "docker_container" "app_python" {
  image = var.app_python_image
  name  = var.app_python_name
  ports {
    internal = 80
    external = 5000
  }
}
