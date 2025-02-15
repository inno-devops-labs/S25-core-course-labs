variable "container_name" {
  description = "The name of the container"
  type        = string
  default     = "moscow-time-app"
}

variable "image_name" {
  description = "The name of the Docker image"
  type        = string
  default     = "moscow-time"
}

variable "image_tag" {
  description = "The tag for the Docker image"
  type        = string
  default     = "moscow-time:latest"
}

variable "external_port" {
  description = "The external port for the container"
  type        = number
  default     = 8000
} 