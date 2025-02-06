variable "app_python_docker_container" {
  description = "app_python Docker container"
  type        = string
  default     = "moscow_app"
}

variable "app_python_docker_image" {
  description = "Docker image name of app_python"
  type        = string
  default     = "tjann7/moscow_time"
}

variable "app_python_internal_port" {
  description = "app_python Internal port"
  type        = number
  default     = 5000
}

variable "app_python_external_port" {
  description = "app_python External port"
  type        = number
  default     = 5000
}
