provider "docker" {

}

resource "docker_image" "app_kotlin" {
  name         = var.docker_image_name
  keep_locally = false
}

resource "docker_container" "app_kotlin" {
  image = docker_image.app_kotlin.image_id
  name  = var.docker_container_name
  ports {
    internal = var.int_port
    external = var.ext_port
  }
}