variable "container_name" {
  description = "Name of the container"
  type        = string
  default     = "python_app"
}

variable "docker_hub_username" {
  description = "Docker Hub username"
  type        = string
}

variable "external_port" {
  description = "External port for the container"
  type        = number
  default     = 5001
} 