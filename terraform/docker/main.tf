terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "python_app_container" {
  image = var.python_app_docker_image_name
  name  = var.python_app_container_name
  ports {
    internal = var.python_app_internal_port
    external = var.python_app_external_port
  }
}

resource "docker_container" "go_app_container" {
  image = var.go_app_docker_image_name
  name  = var.go_app_container_name
  ports {
    internal = var.go_app_internal_port
    external = var.go_app_external_port
  }
}
