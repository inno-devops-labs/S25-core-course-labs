variable "python_app_docker_image_name" {
  description = "Python app Docker image"
  type        = string
  default     = "azamatbayramov/s25-devops-py-dl:latest"
}

variable "python_app_container_name" {
  description = "Python app Docker container name"
  type        = string
  default     = "python-app"
}

variable "python_app_internal_port" {
  description = "Python app internal port"
  type        = number
  default     = 8001
}

variable "python_app_external_port" {
  description = "Python app external port"
  type        = number
  default     = 8011
}

variable "go_app_docker_image_name" {
  description = "Go app Docker image"
  type        = string
  default     = "azamatbayramov/s25-devops-go-dl:latest"
}

variable "go_app_container_name" {
  description = "Go app Docker container name"
  type        = string
  default     = "go-app"
}

variable "go_app_internal_port" {
  description = "Go app internal port"
  type        = number
  default     = 8002
}

variable "go_app_external_port" {
  description = "Go app external port"
  type        = number
  default     = 8012
}
