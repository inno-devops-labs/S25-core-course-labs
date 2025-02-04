# main.tf

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

# APP_PYTHON

resource "docker_image" "python_app_image" {
  name = var.python_app_image_name
  build {
    context    = var.python_app_context
    dockerfile = "distroless.Dockerfile"
  }
}

resource "docker_container" "python_app_container" {
  name  = var.python_container_name
  image = docker_image.python_app_image.image_id

  ports {
    internal = 5000
    external = 5000
  }
}

# APP_JAVA

resource "docker_image" "java_app_image" {
  name = var.java_app_image_name
  build {
    context    = var.java_app_context
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "java_app_container" {
  name  = var.java_container_name
  image = docker_image.java_app_image.image_id

  ports {
    internal = 8080
    external = 8080
  }
}