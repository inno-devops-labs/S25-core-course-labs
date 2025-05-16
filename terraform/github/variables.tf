variable "github_token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub owner/org name"
  type        = string
  default     = "alimansour0002"
}