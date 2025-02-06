variable "container_name" {
  description = "My docker container"
  type        = string
  default     = "inno_devops_terraform"
}

variable "internal_port" {
  description = "This is internal port of my container"
  type        = number
  default     = 80
}

variable "external_port" {
  description = "This is external port of my container"
  type        = number
  default     = 8000
}