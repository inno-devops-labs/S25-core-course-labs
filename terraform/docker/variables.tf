variable "python_webapp_docker_image" {
  description = "Python web application Docker image"
  type        = string
  default     = "magicwinnie/simple-python-web-app-distroless:latest"
}

variable "python_webapp_container_name" {
  description = "Python web application Docker container name"
  type        = string
  default     = "simple-python-web-app"
}

variable "python_webapp_internal_port" {
  description = "Python web application internal port"
  type        = number
  default     = 8000
}

variable "python_webapp_external_port" {
  description = "Python web application external port"
  type        = number
  default     = 8888
}

variable "go_webapp_docker_image" {
  description = "Go web application Docker image"
  type        = string
  default     = "magicwinnie/simple-go-web-app-distroless:latest"
}

variable "go_webapp_container_name" {
  description = "Go web application Docker container name"
  type        = string
  default     = "simple-go-web-app"
}

variable "go_webapp_internal_port" {
  description = "Go web application internal port"
  type        = number
  default     = 8080
}

variable "go_webapp_external_port" {
  description = "Go web application external port"
  type        = number
  default     = 8889
}

