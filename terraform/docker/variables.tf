variable "docker_image" {
  description = "Python app Docker image"
  type        = string
  default     = "sonyaiv/python_app:latest"
}

variable "docker_container_name" {
  description = "Python app Docker container name"
  type        = string
  default     = "python_app"
}