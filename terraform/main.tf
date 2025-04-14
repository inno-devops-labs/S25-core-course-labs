terraform {
  required_providers {
    docker = {
      source  = "g3nd4/python-web"
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