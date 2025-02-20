terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.16.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

variable "python_container_name" {
  description = "Name of the Python container"
  type        = string
  default     = "my_python_container"
}

variable "python_image_name" {
  description = "Docker image name"
  type        = string
  default     = "python:3.11"
}

resource "docker_image" "python_app" {
  name = var.python_image_name
}

resource "docker_container" "python_container" {
  name    = var.python_container_name
  image   = docker_image.python_app.name

  command = ["tail", "-f", "/dev/null"]

  ports {
    internal = 5089
    external = 5089
    ip       = "0.0.0.0"
    protocol = "tcp"
  }
}

output "container_name" {
  value = docker_container.python_container.name
}
