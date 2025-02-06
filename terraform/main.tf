terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

provider "yandex" {
  zone = "default"
}

data "yandex_compute_image" "my_image" {
  family = "ubuntu-2204-lts"
}

output "my_image_id" {
  value = data.yandex_compute_image.my_image.id
}


resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "my_container" {
  name  = var.container_name
  image = docker_image.nginx.image_id
  
  ports {
    internal = 80
    external = 8080
  }
}