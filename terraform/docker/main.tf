terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "time_service_python" {
  image = var.time_service_image_name_python
  name  = var.time_service_container_name_python
  ports {
    internal = var.python_container_port
    external = var.python_host_port
  }
}

resource "docker_container" "time_service_kotlin" {
  image = var.time_service_image_name_kotlin
  name  = var.time_service_container_name_kotlin
  ports {
    internal = var.kotlin_container_port
    external = var.kotlin_host_port
  }
}

