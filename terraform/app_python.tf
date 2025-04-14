terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "msk_time" {
  name         = "absorian/s25-devops-msk-time:latest"
  keep_locally = false
}

resource "docker_container" "msk_time" {
  image = docker_image.msk_time.image_id
  name  = "terraform_msk_time"
  env   = ["APP_HOST=0.0.0.0", "APP_PORT=8000"]
  ports {
    internal = 8000
    external = 8000
  }
}
