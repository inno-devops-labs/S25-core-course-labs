variable "github_token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "repo_name" {
  type        = string
  description = "Repository name"
  default     = "S25-devops-labs"
}

variable "repo_desc" {
  type        = string
  description = "Repository description"
  default     = "DevOps Engineering course repository"
}

variable "repo_vis" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}

variable "default_branch" {
  type        = string
  description = "Default branch of the repository"
  default     = "master"
}

variable "enforce_admins" {
  type        = bool
  description = "Enforce branch protection for admins"
  default     = true
}

variable "required_approving_review_count" {
  type        = number
  description = "Number of required approving reviews before merging"
  default     = 1
}