terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///Users/nikitadrozdov/.orbstack/run/docker.sock"
}

resource "docker_image" "moscow_time" {
  name = var.image_name
  build {
    context = "../../app_python"
    tag     = [var.image_tag]
  }
  keep_locally = false
}

resource "docker_container" "moscow_time" {
  image = docker_image.moscow_time.image_id
  name  = var.container_name
  ports {
    internal = 8000
    external = var.external_port
  }
} 