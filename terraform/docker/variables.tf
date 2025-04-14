variable "container_name_python" {
  description = "Docker container name"
  type        = string
  default     = "app_python"
}

variable "docker_image_python" {
  description = "Docker image"
  type        = string
  default     = "raleksan/app_python:v0.1"
}

variable "internal_port_python" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port_python" {
  description = "External port"
  type        = number
  default     = 8080
}

variable "container_name_rust" {
  description = "Docker container name"
  type        = string
  default     = "app_rust"
}

variable "docker_image_rust" {
  description = "Docker image"
  type        = string
  default     = "raleksan/app_rust:v0.1"
}

variable "internal_port_rust" {
  description = "Internal port"
  type        = number
  default     = 8081
}

variable "external_port_rust" {
  description = "External port"
  type        = number
  default     = 8081
}