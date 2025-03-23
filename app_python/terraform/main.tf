terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Create a docker image resource - using the image from your Dockerfile
resource "docker_image" "moscow_time" {
  name         = "marketer7/flask-time:v1"  # This matches your Docker image name from README.md
  keep_locally = false
}

# Create a docker container resource
resource "docker_container" "moscow_time_container" {
  image = docker_image.moscow_time.image_id
  name  = var.container_name
  
  ports {
    internal = 8000  # Matches your Flask app port
    external = 8000
  }
}
