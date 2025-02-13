terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "nginx" {
  image = "nginx:latest"
  name  = var.container_name
  ports {
    internal = 80
    external = 8080
  }
}

variable "container_name" {
  default = "my_nginx_container"
}
output "container_ip" {
  value = docker_container.nginx.ip_address
}

output "container_name" {
  value = docker_container.nginx.name
}