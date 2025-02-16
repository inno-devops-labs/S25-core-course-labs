variable "token" {
  description = "Personal access token"
  type        = string
  sensitive   = true
}

variable "name" {
  description = "Name of the repository"
  type        = string
  default     = "S25-core-course-labs"
}

variable "default_branch" {
  description = "Default branch"
  default     = "feature/lab4"
}
