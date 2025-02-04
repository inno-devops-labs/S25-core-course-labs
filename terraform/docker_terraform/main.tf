terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_app" {
  name         = "lekski/python-web-app:latest"
  keep_locally = false
}

resource "docker_image" "golang_app" {
  name         = "lekski/golang-web-app:latest"
  keep_locally = false
}

variable "python_docker_name" {
  description = "Python app container name"
  default     = "my-python-app"
}

variable "golang_docker_name" {
  description = "Golang app container name"
  default     = "my-golang-app"
}

resource "docker_container" "python_app" {
  image = docker_image.python_app.image_id
  name  = var.python_docker_name

  ports {
    internal = 8000
    external = 8000
  }
}

resource "docker_container" "golang_app" {
  image = docker_image.golang_app.image_id
  name  = var.golang_docker_name

  ports {
    internal = 8000
    external = 8001
  }
}