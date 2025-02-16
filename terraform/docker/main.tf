resource "docker_image" "moscow-time-app" {
    name         = "justcgh/moscow-time-app:latest"
    keep_locally = false
}

resource "docker_container" "moscow-time-app" {
  image = docker_image.moscow-time-app.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = var.external_port
  }
}