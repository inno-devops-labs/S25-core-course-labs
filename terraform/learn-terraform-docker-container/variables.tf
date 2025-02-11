variable "flask_app_docker_image" {
  description = "Docker image of flask-app"
  type        = string
  default     = "synavtora/flask-app:latest" 
}

variable "flask_app_docker_name" {
  description = "Docker container name"
  type        = string
  default     = "flask-app"
}

variable "flask_app_internal_port" {
  description = "flask-app internal port"
  type        = number
  default     = 5000
}

variable "flask_app_external_port" {
  description = "flask-app external port"
  type        = number
  default     = 5000
}
