variable "python_app_image" {
  description = "Python app Docker image"
  type        = string
  default     = "bugay/python-msk-time-app-distroless:latest"
}

variable "python_app_container_name" {
  description = "Python app Docker container name"
  type        = string
  default     = "python-msk-time-app-distroless"
}

variable "scala_app_image" {
  description = "Scala app Docker image"
  type        = string
  default     = "bugay/scala-msk-time-app-distroless:latest"
}

variable "scala_app_container_name" {
  description = "Scala app Docker container name"
  type        = string
  default     = "scala-msk-time-app-distroless"
}

variable "python_app_int_port" {
  description = "Python app internal port"
  type        = number
  default     = 5000
}

variable "python_app_ext_port" {
  description = "Python app external port"
  type        = number
  default     = 5000
}

variable "scala_app_int_port" {
  description = "Scala app internal port"
  type        = number
  default     = 9090
}

variable "scala_app_ext_port" {
  description = "Scala app external port"
  type        = number
  default     = 9090
}
