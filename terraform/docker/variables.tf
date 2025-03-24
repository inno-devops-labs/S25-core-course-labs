variable "application_image" {
  description = "Image from DockerHub"
  type        = string
  default     = "muhammaduss/app-python"
}
variable "container_name" {
  description = "Name of the python application container"
  type        = string
  default     = "time_app_python"
}
variable "internal_port" {
  description = "Application inside docker listening port"
  type        = number
  default     = 8080
}
variable "external_port" {
  description = "Port which by application can be achieved from host"
  type        = number
  default     = 8080
}
