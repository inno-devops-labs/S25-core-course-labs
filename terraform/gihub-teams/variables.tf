variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Organization"
  default     = "devops-efim"
}