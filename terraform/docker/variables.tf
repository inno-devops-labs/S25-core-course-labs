variable "container_name" {
  description = "Docker container name"
  type        = string
  default     = "my_container"
}

variable "image_name" {
  description = "Docker image name"
  type        = string
  default     = "nginx:latest"
}

variable "internal_port" {
  description = "Internal port for the container"
  type        = number
  default     = 80
}

variable "external_port" {
  description = "External port for the container"
  type        = number
  default     = 8000
}
