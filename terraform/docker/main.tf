terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_container" "python_app_container" {
  image = var.python_app_image
  name  = var.python_app_container_name
  ports {
    internal = var.python_app_int_port
    external = var.python_app_ext_port
  }
}

resource "docker_container" "scala_app_container" {
  image = var.scala_app_image
  name  = var.scala_app_container_name
  ports {
    internal = var.scala_app_int_port
    external = var.scala_app_ext_port
  }
}
