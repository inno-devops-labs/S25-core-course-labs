variable "py_container_name" {
  description = "Value of the name for the Python Docker container"
  type        = string
  default     = "python-msk-time"
}

variable "node_container_name" {
  description = "Value of the name for the Node Docker container"
  type        = string
  default     = "js-cities-dist"
}
