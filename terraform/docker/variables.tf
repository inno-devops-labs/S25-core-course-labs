variable "py_image" {
  default = "zerohalf/moscow-time-app:latest"
}

variable "python_container_name" {
  description = "Name for the Python application container"
  type        = string
  default     = "moscow-app"
}

variable "py_external_port" {
  description = "Port to be externally mapped to work with Python app"
  type        = number
  default     = 8080
}