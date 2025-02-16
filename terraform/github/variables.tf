variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
}

variable "default_branch" {
  description = "Default branch for repository"
  type        = string
  default     = "master"
}