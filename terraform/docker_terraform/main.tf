terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "app_python_container" {
  image = var.docker_image_python
  name  = var.container_name_python
  ports {
    internal = var.internal_port_python
    external = var.external_port_python
  }
}

resource "docker_container" "app_ruby_container" {
  image = var.docker_image_ruby
  name  = var.container_name_ruby
  ports {
    internal = var.internal_port_ruby
    external = var.external_port_ruby
  }
}
