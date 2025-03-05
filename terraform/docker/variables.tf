variable "app_python_docker_image" {
  description = "Docker image name of app_python"
  type        = string
  default     = "unileonid/time-app-py"
}

variable "app_python_docker_container" {
  description = "Docker container name of app_python"
  type        = string
  default     = "unileonid_time_app_py"
}

variable "app_python_internal_port" {
  description = "Internal port of app_python"
  type        = number
  default     = 8080
}

variable "app_python_external_port" {
  description = "External port of app_python"
  type        = number
  default     = 80
}
