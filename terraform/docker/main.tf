terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"  # For Windows
}

# Pull the Docker images (using distroless images)
resource "docker_image" "app_python" {
  name         = "kira354/app-python-distroless:latest"
  keep_locally = false
}

resource "docker_image" "app_javascript" {
  name         = "kira354/app-javascript-distroless:latest"
  keep_locally = false
}

# Create Docker containers
resource "docker_container" "app_python_container" {
  name  = var.python_container_name
  image = docker_image.app_python.latest
  ports {
    internal = 5000
    external = 5000
  }
}

resource "docker_container" "app_javascript_container" {
  name  = var.javascript_container_name
  image = docker_image.app_javascript.latest
  ports {
    internal = 3000
    external = 3000
  }
}
