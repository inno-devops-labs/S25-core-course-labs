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
  name  = "time-in-moscow"
  ports {
    internal = 8000
    external = var.python_container_external_port
  }
}

resource "docker_container" "number_facts_app" {
  image = var.goapp_image
  name  = "random-number-facts"
  ports {
    internal = 8080
    external = var.go_container_external_port
  }
}

