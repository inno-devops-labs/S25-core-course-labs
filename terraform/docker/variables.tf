variable "python_container_name" {
  description = "Name for the python app container"
  type        = string
  default     = "python-app"
}


variable "app_python_internal_port" {
  description = "Python web application internal port"
  type        = number
  default     = 8000
}

variable "app_python_external_port" {
  description = "Python web application external port"
  type        = number
  default     = 8888
}