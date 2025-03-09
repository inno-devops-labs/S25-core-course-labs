variable "container_name" {
  type = string
  description = "Name for moscow time application container"
  default = "app_python"
}

variable "external_port" {
  type = number
  description = "Port for container to forward"
  default = 8080
}