variable "token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "GitHub repository name"
  type        = string
  default     = "S25-core-course-labs"
}