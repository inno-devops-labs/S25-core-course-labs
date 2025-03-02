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

resource "docker_container" "python_time_app" {
  image = var.python_time_app_image
  name  = var.python_time_app_name
  ports {
    internal = 80
    external = 5000
  }
}

