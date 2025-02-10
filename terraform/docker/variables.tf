variable "time_service_image_name_python" {
  description = "Docker image name for python"
  type        = string
  default     = "nai1ka/time-service:latest"
}

variable "time_service_container_name_python" {
  description = "Docker container name for python"
  type        = string
  default     = "time-service-container-python"
}

variable "python_container_port" {
  description = "Internal port of python app"
  type        = number
  default     = 8000
}

variable "python_host_port" {
  description = "External of python app"
  type        = number
  default     = 8000
}

variable "time_service_image_name_kotlin" {
  description = "Docker image for Kotlin"
  type        = string
  default     = "nai1ka/time-service-kotlin:latest"
}

variable "time_service_container_name_kotlin" {
  description = "Docker container name for Kotlin"
  type        = string
  default     = "time-service-container-kotlin"
}

variable "kotlin_container_port" {
  description = "Internal port for Kotlin app"
  type        = number
  default     = 8080
}

variable "kotlin_host_port" {
  description = "External port for Kotlin app"
  type        = number
  default     = 8080
}