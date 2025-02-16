variable "container_name" {
  type    = string
  default = "app_python"
}

variable "image_name" {
  type    = string
  default = "daniilzimin4/devopsapp:latest"
}

variable "internal_port" {
  type    = number
  default = 9200
}

variable "external_port" {
  type    = number
  default = 9200
}