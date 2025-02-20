terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name = var.python_app_image
}

resource "docker_container" "moscow_time_app" {
  image = docker_image.python_app.name
  name  = var.python_container_name
  ports {
    internal = 5000
    external = var.python_container_external_port
  }
}

resource "docker_image" "js_app" {
  name = var.js_app_image
}

resource "docker_container" "countdown_timer_app" {
  image = docker_image.js_app.name
  name  = var.js_container_name
  ports {
    internal = 8080
    external = var.js_container_external_port
  }
}
