terraform {
 required_providers {
   docker = {
     source = "kreuzwerker/docker"
     version = "3.0.2"
   }
 }
}

provider "docker" {}

variable "container_name" {
 type = string
 default = "my_container"
}

resource "docker_image" "nginx" {
 name = "nginx:latest"
}

resource "docker_container" "app" {
 image = docker_image.nginx.image_id
 name  = var.container_name
 ports {
   internal = 80
   external = 8080
 }
}

output "container_id" {
 value = docker_container.app.id
}