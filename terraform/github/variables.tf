variable "token" {
  type        = string
  description = "Token for GitHub"
  sensitive   = true
}

variable "repository_name" {
  type        = string
  description = "Name of the repository"
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  type        = string
  description = "Description of the repository"
  default     = "Repository for the S25 core course labs"
}

variable "repository_visibility" {
  type        = string
  description = "Visibility of the repository"
  default     = "public"
}

variable "default_branch_name" {
  type        = string
  description = "Name of the default branch"
  default     = "master"
}

variable "require_conversation_resolution" {
  type        = bool
  description = "Whether to require conversation resolution before merging"
  default     = true
}

variable "enforce_admins" {
  type        = bool
  description = "Whether to enforce protection of the default branch for admins"
  default     = true
}

variable "required_approving_review_count" {
  type        = number
  description = "Number of approving reviews required"
  default     = 1
}
