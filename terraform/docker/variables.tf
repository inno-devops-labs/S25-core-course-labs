variable "container_name" {
  type = string
  description = "The name of the Docker container"
  default = "app_python_container"
}

variable "app_image" {
  default = "anyarylova/app_python"
}