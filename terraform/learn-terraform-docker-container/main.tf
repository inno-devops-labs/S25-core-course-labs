terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "flask_app_container" {
  image = var.flask_app_docker_image
  name  = var.flask_app_docker_name

  ports {
    internal = var.flask_app_internal_port
    external = var.flask_app_external_port
  }
}
