variable "container_name_python" {
  description = "Docker container name"
  type        = string
  default     = "app_python"
}

variable "docker_image_python" {
  description = "Docker image"
  type        = string
  default     = "elonmaxx/app_python"
}

variable "internal_port_python" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port_python" {
  description = "External port"
  type        = number
  default     = 8079
}

variable "container_name_go" {
  description = "Docker container name"
  type        = string
  default     = "app_go"
}

variable "docker_image_go" {
  description = "Docker image"
  type        = string
  default     = "elonmaxx/app_go"
}

variable "internal_port_go" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port_go" {
  description = "External port"
  type        = number
  default     = 7999
}
