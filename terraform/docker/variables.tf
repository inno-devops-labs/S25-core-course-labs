variable "python_container_name" {
  type    = string
  default = "app_python"
}

variable "python_image_name" {
  type    = string
  default = "ilsiia/app_python:latest"
}

variable "node_container_name" {
  type    = string
  default = "app_nodejs"
}

variable "node_image_name" {
  type    = string
  default = "ilsiia/app_nodejs:latest"
}

