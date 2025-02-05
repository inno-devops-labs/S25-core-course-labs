variable "container_name" {
  type    = string
  default = "app_python"
}

variable "image_name" {
  type    = string
  default = "mishablin/devops-labs:latest"
}

variable "internal_port" {
  type    = number
  default = 5000
}

variable "external_port" {
  type    = number
  default = 5000
}
