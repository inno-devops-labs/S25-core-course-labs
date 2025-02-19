variable "github_token" {
  type        = string
  description = "GitHub access token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Organization"
  default     = "dyddxd-for-github-teams"
}