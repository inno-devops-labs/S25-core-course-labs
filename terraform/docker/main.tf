terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "python_webapp_container" {
  image = var.python_webapp_docker_image
  name  = var.python_webapp_container_name
  ports {
    internal = var.python_webapp_internal_port
    external = var.python_webapp_external_port
  }
}

resource "docker_container" "go_webapp_container" {
  image = var.go_webapp_docker_image
  name  = var.go_webapp_container_name
  ports {
    internal = var.go_webapp_internal_port
    external = var.go_webapp_external_port
  }
}
