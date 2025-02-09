variable "container_name_python" {
  description = "Docker container name for Python app"
  type        = string
  default     = "msk"
}

variable "docker_image_python" {
  description = "Docker image for Python app"
  type        = string
  default     = "ebob/moscow-time:v1.0"
}

variable "internal_port_python" {
  description = "Internal port for Python app"
  type        = number
  default     = 8080
}

variable "external_port_python" {
  description = "External port for Python app"
  type        = number
  default     = 8080
}

variable "container_name_ruby" {
  description = "Docker container name for Ruby app"
  type        = string
  default     = "omsk"
}

variable "docker_image_ruby" {
  description = "Docker image for Ruby app"
  type        = string
  default     = "ebob/omsk-time:v1.0"
}

variable "internal_port_ruby" {
  description = "Internal port for Ruby app"
  type        = number
  default     = 4567
}

variable "external_port_ruby" {
  description = "External port for Ruby app"
  type        = number
  default     = 8081
}
