variable "github_token" {
  type        = string
  description = "GitHub token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "GitHub organization name"
  default     = "devops-lab-vladislav"
}
