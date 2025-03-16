variable "container_name" {
  type        = string
  default     = "devopslavs"
}

variable "docker_hub_username" {
  type        = string
}

variable "external_port" {
  type        = number
  default     = 5001
} 