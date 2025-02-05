terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name         = "alexstrnik/python-app:latest"
  keep_locally = false
  platform     = "linux/amd64"
}

resource "docker_container" "python_app" {
  name  = var.container_name
  image = docker_image.python_app.image_id

  ports {
    internal = 5000
    external = 8080
  }

  env = [
    "ENVIRONMENT=production"
  ]
}
