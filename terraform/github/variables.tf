variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "repo_name" {
  type        = string
  description = "Repository name"
  default     = "S25-core-course-labs"
}

variable "repo_desc" {
  type        = string
  description = "Repository description"
  default     = "DevOps course labs solution"
}

variable "repo_visibility" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}

variable "repo_has_issues" {
  type        = bool
  description = "Enable issues in the repository"
  default     = false
}

variable "repo_has_wiki" {
  type        = bool
  description = "Enable wiki in the repository"
  default     = false
}

variable "repo_auto_init" {
  type        = bool
  description = "Initialize repository with README"
  default     = true
}

variable "repo_license" {
  type        = string
  description = "License template for the repository"
  default     = "mit"
}

variable "repo_gitignore" {
  type        = string
  description = "Gitignore template"
  default     = "Python"
}

variable "default_branch" {
  type        = string
  description = "Default branch for the repository"
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
