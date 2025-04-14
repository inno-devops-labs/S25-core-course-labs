variable "pyapp_container" {
  type        = string
  description = "Docker container for Python app"
}

variable "pyapp_image" {
  type        = string
  description = "Docker image for Python app"
}

variable "python_container_external_port" {
  type        = number
  description = "External port for Python container"
}

variable "goapp_container" {
  type        = string
  description = "Docker container for Go app"
}

variable "goapp_image" {
  type        = string
  description = "Docker image for Go app"
}

variable "go_container_external_port" {
  type        = number
  description = "External port for Go container"
}
