terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

# Pull the latest nginx image
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# Define the Docker container using an input variable for the name
resource "docker_container" "nginx" {
  image = docker_image.nginx.name
  name  = var.contain_name

  ports {
    internal = 80
    external = 8080
  }
}
