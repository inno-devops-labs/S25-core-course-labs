terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_container" "moscow_time_app_container" {
  image = var.moscow_time_app_docker_image
  name  = var.moscow_time_app_container_name
  ports {
    internal = var.moscow_time_app_internal_port
    external = var.moscow_time_app_external_port
  }
}

resource "docker_container" "js_app_container" {
  image = var.js_app_docker_image
  name  = var.js_app_container_name
  ports {
    internal = var.js_app_internal_port
    external = var.js_app_external_port
  }
}
