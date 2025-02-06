variable "external_port" {
  type        = number
  description = "External container port"
  default     = 8080
}

variable "internal_port" {
  type        = number
  description = "Internal container port"
  default     = 80
}

variable "container_name" {
  type        = string
  description = "Container name"
  default     = "tutorial-container"
}
