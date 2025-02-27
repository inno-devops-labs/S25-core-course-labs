variable "moscow_time_app_docker_image" {
  description = "Moscow time app image"
  type        = string
  default     = "gendiro/moscow-time-app:latest"
}

variable "moscow_time_app_container_name" {
  description = "Moscow time app name"
  type        = string
  default     = "moscow-time-app"
}

variable "moscow_time_app_internal_port" {
  description = "Moscow time app internal port"
  type        = number
  default     = 8000
}

variable "moscow_time_app_external_port" {
  description = "Moscow time app external port"
  type        = number
  default     = 8000
}

variable "js_app_docker_image" {
  description = "Js app Docker image"
  type        = string
  default     = "gendiro/js-app-distroless:latest"
}

variable "js_app_container_name" {
  description = "Js app Docker container name"
  type        = string
  default     = "js-app-distroless"
}

variable "js_app_internal_port" {
  description = "Js app internal port"
  type        = number
  default     = 3000
}

variable "js_app_external_port" {
  description = "Js app external port"
  type        = number
  default     = 3000
}
