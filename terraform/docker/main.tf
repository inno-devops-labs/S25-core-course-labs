terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }

  required_version = ">= 0.13"
}

provider "docker" {}

resource "docker_image" "moscow_time_app" {
  name         = "pr0ventu5/moscow-time-app"
  keep_locally = false
}

resource "docker_container" "moscow_time_app" {
  image = docker_image.moscow_time_app.image_id
  name  = var.container_name

  ports {
    internal = 8080
    external = 8000
  }
}
