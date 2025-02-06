variable "github_token" {
  type        = string
  description = "GitHub personal access token (or GITHUB_TOKEN environment variable)"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "GitHub organization name"
  default     = "DevOpsLabsMeganov"
}