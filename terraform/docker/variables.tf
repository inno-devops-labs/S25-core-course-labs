variable "container_name_python" {
  description = "Docker container name"
  type        = string
  default     = "flask-app"
}

variable "docker_image_python" {
  description = "Docker image"
  type        = string
  default     = "atkond/flask-app:latest"
}

variable "internal_port_python" {
  description = "Internal port"
  type        = number
  default     = 5000
}

variable "external_port_python" {
  description = "External port"
  type        = number
  default     = 5000
}

