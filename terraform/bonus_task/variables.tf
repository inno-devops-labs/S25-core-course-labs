variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "org_name" {
  description = "GitHub Organization Name"
  type        = string
}

variable "repository_name" {
  description = "GitHub Repository Name"
  type        = string
} 