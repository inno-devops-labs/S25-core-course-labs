terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "moscow_time_app" {
  image = var.pyapp_image
  name  = var.pyapp_container
  ports {
    internal = 5000
    external = var.python_container_external_port
  }
}

resource "docker_container" "random_predictions" {
  image = var.goapp_image
  name  = var.goapp_container
  ports {
    internal = 8080
    external = var.go_container_external_port
  }
}