# Docker provider.

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Pull the NGINX image from Docker Hub.
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# Create a Docker container using the pulled NGINX image.
resource "docker_container" "nginx" {
  name  = "var.docker_image_name"
  image = docker_image.nginx.image_id

  # Map container port 80 to host port 8000.
  ports {
    internal = 80
    external = 8000
  }
}
