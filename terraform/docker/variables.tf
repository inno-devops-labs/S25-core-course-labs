variable "container_name_python" {
  description = "Docker container name for Python app"
  type        = string
  default     = "inno_devops_lab2_python_bonus"
}

variable "docker_image_python" {
  description = "Docker image for Python app"
  type        = string
  default     = "dmhd6219/inno_devops_lab2_python_bonus:latest"
}

variable "internal_port_python" {
  description = "Internal port for Python app"
  type        = number
  default     = 8000
}

variable "external_port_python" {
  description = "External port for Python app"
  type        = number
  default     = 8000
}

variable "container_name_typescript" {
  description = "Docker container name for Typescript app"
  type        = string
  default     = "inno_devops_lab2_typescript_bonus"
}

variable "docker_image_typescript" {
  description = "Docker image for Typescript app"
  type        = string
  default     = "dmhd6219/inno_devops_lab2_typescript_bonus:latest"
}

variable "internal_port_typescript" {
  description = "Internal port for Typescript app"
  type        = number
  default     = 8080
}

variable "external_port_typescript" {
  description = "External port for Typescript app"
  type        = number
  default     = 8080
}