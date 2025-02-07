terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Python App
resource "docker_image" "python_app" {
  name         = "python_app"
  build {
    context    = "${path.module}/../../app_python"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "python_app" {
  image = docker_image.python_app.image_id
  name  = "python_app_container"

  ports {
    internal = 8000
    external = 8000
  }
}

# TypeScript App
resource "docker_image" "typescript_app" {
  name         = "typescript_app"
  build {
    context    = "${path.module}/../../app_typescript"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "typescript_app" {
  image = docker_image.typescript_app.image_id
  name  = "typescript_app_container"

  ports {
    internal = 80
    external = 8080
  }

  user = "nonroot"
}
