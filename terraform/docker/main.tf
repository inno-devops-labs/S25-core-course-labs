terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Pull the Docker image from Docker Hub
resource "docker_image" "python_app" {
  name         = "jlfkajlkifj/app_python:latest"
  keep_locally = false
}

# Create a Docker container using the pulled image
resource "docker_container" "python_app" {
  name  = var.container_name
  image = docker_image.python_app.image_id

  ports {
    internal = 8000
    external = var.external_port
  }

  restart = "unless-stopped"
}
