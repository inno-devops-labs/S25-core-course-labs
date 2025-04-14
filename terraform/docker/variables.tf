variable "container_name_python" {
  description = "Docker container name"
  type        = string
  default     = "app_python"
}

variable "docker_image_python" {
  description = "Docker image"
  type        = string
  default     = "2imt/app_python:latest"
}

variable "internal_port_python" {
  description = "Internal port"
  type        = number
  default     = 8000
}

variable "external_port_python" {
  description = "External port"
  type        = number
  default     = 8000
}

variable "container_name_rust" {
  description = "Docker container name"
  type        = string
  default     = "app_rust"
}

variable "docker_image_rust" {
  description = "Docker image"
  type        = string
  default     = "2imt/app_rust:latest"
}

variable "internal_port_rust" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port_rust" {
  description = "External port"
  type        = number
  default     = 8080
}
