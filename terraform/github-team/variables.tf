variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "github_organization" {
  description = "GitHub organization name"
  type        = string
  default     = "my-org-name"  # Replace with your organization name
}
