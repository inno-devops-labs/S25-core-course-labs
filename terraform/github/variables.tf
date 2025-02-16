variable "github_token" {
  description = "GitHub access token"
  type        = string
  sensitive   = true
}

variable "github_repo_name" {
  description = "GitHub repository name"
  type        = string
  default     = "S25-devops-engineering-labs"
}

variable "github_repo_description" {
  description = "Repository description"
  type        = string
  default     = "Bakina Sofia"
}

variable "github_repo_has_issues" {
  type        = bool
  description = "Enable issues in the repository"
  default     = false
}

variable "github_repo_has_wiki" {
  type        = bool
  description = "Enable wiki in the repository"
  default     = false
}

variable "github_repo_auto_init" {
  type        = bool
  description = "Initialize repository with README"
  default     = true
}


variable "github_repo_visibility" {
  description = "Repository visibility (public or private)"
  type        = string
  default     = "public"
}

variable "github_repo_license" {
  type        = string
  description = "License template for the repository"
  default     = "mit"
}

variable "github_repo_gitignore" {
  type        = string
  description = "Gitignore template"
  default     = "Python"
}

variable "github_default_branch" {
  description = "The default branch for the repository"
  type        = string
  default     = "master"
}

variable "require_conversation_resolution" {
  type        = bool
  description = "Require conversation resolution before merging"
  default     = true
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
