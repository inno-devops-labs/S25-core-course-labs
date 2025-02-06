terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

variable "docker_username" {}
variable "docker_password" {}

provider "docker" {
  host = "unix:///var/run/docker.sock"

  registry_auth {
    address  = "index.docker.io/v1/"
    username = "matveyplat"
    password = "&3?bftJYfV^.tVR"
  }
}

variable "container_name" {
  description = "The name of the Docker container"
  type        = string
  default     = "running_container"  # You can set a default value
}

resource "docker_image" "my_image" {
  name         = "matveyplat/flask-app:latest"
  keep_locally = false
}

resource "docker_container" "flask_app" {
  name  = var.container_name
  image = docker_image.my_image.image_id
  ports {
    internal = 80
    external = 8080
  }
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.flask_app.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.my_image.id
}
