variable "github_pat" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "managed organization in GitHub"
  default     = "Smack-org"
}