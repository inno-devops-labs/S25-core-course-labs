terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_piton" {
  name         = "paranid5/app_piton:latest"
  keep_locally = false
}

resource "docker_container" "app_piton" {
  image = docker_image.app_piton.image_id
  name  = var.container_piton

  ports {
    internal = 8080
    external = 6060
  }
}

resource "docker_image" "app_flutter" {
  name         = "paranid5/app_flutter:latest"
  keep_locally = false
}

resource "docker_container" "app_flutter" {
  image = docker_image.app_flutter.image_id
  name  = var.container_flutter

  ports {
    internal = 80
    external = 7070
  }
}

variable "container_piton" {
  description = "Name of the Piton Docker container."
  type        = string
  default     = "app_piton"
}

variable "container_flutter" {
  description = "Name of the Flutter Docker container."
  type        = string
  default     = "app_flutter"
}
