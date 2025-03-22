variable "python_app_image" {
  default     = "dtolmach/python-app:latest"
}

variable "python_container_name" {
  description = "Name for Python application container"
  type        = string
  default     = "python_app"
}

variable "python_ext_port" {
  description = "Python application external port"
  type        = number
  default     = 8000
}
