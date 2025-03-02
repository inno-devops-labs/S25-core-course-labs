variable "pyapp_image" {
  default = "m0t9docker/pyapp:latest"
}

variable "python_container_name" {
  description = "Name for the Python application container"
  type        = string
  default     = "moscow-time-app"
}

variable "python_container_external_port" {
  description = "Port to be externally mapped to work with Python app"
  type        = number
  default     = 8080
}


variable "goapp_image" {
  default = "m0t9docker/goapp:latest"
}

variable "go_container_name" {
  description = "Name for the Go application container"
  type        = string
  default     = "random-number-facts"
}

variable "go_container_external_port" {
  description = "Port to be externally mapped to work with Go app"
  type        = number
  default     = 8081
}


