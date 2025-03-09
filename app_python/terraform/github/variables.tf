variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}
variable "repo_name" {
  description = "GitHub Repository Name"
  type        = string
  default     = "S25-core-course-labs"
}
