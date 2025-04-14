variable "app_docker_image" {
  description = "Web app Docker image"
  type        = string
  default     = "innoenjoyer/moscow-time-app:latest"
}

variable "app_container_name" {
  description = "Web app Docker container name"
  type        = string
  default     = "moscow-time-app"
}

variable "app_internal_port" {
  description = "Web app internal port"
  type        = number
  default     = 5000
}

variable "app_external_port" {
  description = "Web app external port"
  type        = number
  default     = 8000
}
