variable "container_name" {
  type    = string
  default = "app_python_changed"
}

variable "image_name" {
  type    = string
  default = "redis:latest"
}

variable "internal_port" {
  type    = number
  default = 4000
}

variable "external_port" {
  type    = number
  default = 4000
}