variable "container_name" {
  description = "Name of the Docker container"
  default     = "my-nginx-container"
}

variable "image_name" {
  description = "Docker image name"
  default     = "nginx:latest"
}

variable "internal_port" {
  description = "Internal port of the container"
  default     = 5000
}

variable "external_port" {
  description = "External port of the container"
  default     = 5000
}