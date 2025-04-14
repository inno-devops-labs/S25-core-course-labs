variable "py_app_image" {
  default = "wensiet/devops-py-app:latest"
}

variable "py_app_container_name" {
  default = "py_app"
}

variable "py_app_internal_port" {
  default = 8000
}

variable "py_app_external_port" {
  default = 8000
}