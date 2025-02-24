variable "python_container_name" {
  description = "Docker container name"
  type        = string
  default     = "app_python"
}

variable "python_docker_image" {
  description = "Docker image"
  type        = string
  default     = "mihdenis85/app_python"
}

variable "python_internal_port" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "python_external_port" {
  description = "External port"
  type        = number
  default     = 8080
}
