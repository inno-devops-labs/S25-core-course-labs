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

resource "docker_container" "app_typescript_container" {
  image = var.docker_image_typescript
  name  = var.container_name_typescript
  ports {
    internal = var.internal_port_typescript
    external = var.external_port_typescript
  }
}