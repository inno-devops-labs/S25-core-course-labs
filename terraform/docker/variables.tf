variable "app_python_container" {
  description = "Container for app_python"
  type        = string
  default     = "app_python"
}

variable "app_python_docker_image_name" {
  description = "Docker image name for app_python"
  type        = string
  default     = "dsaee/app"
}
