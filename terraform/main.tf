terraform {
   required_providers {
     docker = {
       source  = "kreuzwerker/docker"
       version = "3.0.2"
     }
   }
 }

provider "docker" {
    host = "unix:///run/podman/podman.sock"
}

 resource "docker_image" "app_python" {
   name         = "kartofanych/app_python:latest"
   keep_locally = false
   platform     = "linux/amd64"
 }

 resource "docker_container" "app_python" {
   name  = "my container"
   image = docker_image.app_python.image_id

   ports {
     internal = 5000
     external = 8080
   }

   env = [
     "ENVIRONMENT=production"
   ]
 }