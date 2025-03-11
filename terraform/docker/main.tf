terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_image" {
  name = var.docker_image
}

resource "docker_container" "app_container" {
  name  = var.container_name
  image = docker_image.app_image.name
  ports {
    internal = 8000
    external = 8000
  }
}

variable "docker_image" {
  description = "Docker image name"
  type        = string
  default     = "pupolina7/moscow-time-app:latest"
}

variable "container_name" {
  description = "Name of the Docker container"
  type        = string
  default     = "moscow-time-container"
}

output "container_id" {
  value = docker_container.app_container.id
}

output "container_name" {
  value = docker_container.app_container.name
}
