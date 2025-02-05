variable "python_app_image" {
  default = "vladis7love/app_python:latest"
}

variable "python_container_name" {
  description = "Name for the Python application container"
  type        = string
  default     = "moscow-time-app"
}

variable "python_container_external_port" {
  description = "Port to be externally mapped to work with Python app"
  type        = number
  default     = 5000
}

variable "js_app_image" {
  default = "vladis7love/app_javascript:latest"
}

variable "js_container_name" {
  description = "Name for the JavaScript application container"
  type        = string
  default     = "countdown-timer"
}

variable "js_container_external_port" {
  description = "Port to be externally mapped to work with JavaScript app"
  type        = number
  default     = 8080
}
