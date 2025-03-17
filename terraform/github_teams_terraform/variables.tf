variable "github_token" {
  type        = string
  description = "GitHub token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Organization"
  default     = "Bobkunov"
}
