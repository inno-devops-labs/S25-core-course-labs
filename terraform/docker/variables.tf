variable "db_password" {
  description = "PostgreSQL password"
  type        = string
  sensitive   = true
}

variable "db_user" {
  description = "PostgreSQL user"
  type        = string
  default     = "myuser"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "times"
}