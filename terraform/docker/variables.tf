variable "docker_image_name" {
  description = "Name for the Docker image"
  default     = "emapfff/app_python:latest"
  type        = string
}

variable "docker_container_name" {
  description = "Name for the Docker container"
  default     = "app_python"
  type        = string
}

variable "int_port" {
  description = "Value of port on which application is running inside Docker container"
  default     = 8080
  type        = number
}

variable "ext_port" {
  description = "Value of port on which local host redirects requests to Docker cotainer"
  default     = 8080
  type        = number
}