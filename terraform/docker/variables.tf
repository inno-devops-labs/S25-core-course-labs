variable "app_docker_image_name" {
  description = "App Docker image"
  type        = string
  default     = "darrpyy/app_python:latest"
}

variable "app_container_name" {
  description = "App Docker container name"
  type        = string
  default     = "app"
}

variable "app_internal_port" {
  description = "App internal port"
  type        = number
  default     = 5000
}

variable "app_external_port" {
  description = "App external port"
  type        = number
  default     = 5000
}
