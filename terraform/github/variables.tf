variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Name of the GitHub repository"
  type        = string
  default     = "S25-core-course-labs"
} 