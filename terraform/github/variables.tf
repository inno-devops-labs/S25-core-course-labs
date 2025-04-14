variable "repo_name" {
  type        = string
  description = "Repository name"
  default     = "S25-core-course-labs"
}

variable "repo_description" {
  type        = string
  description = "Repository description"
  default     = "DevOps Engineering Labs"
}

variable "repo_visibility" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}

variable "repo_default_branch" {
  type        = string
  description = "Default branch"
  default     = "master"
}

variable "require_conversation_resolution" {
  type        = bool
  description = "Require conversation resolution"
  default     = true
}

variable "enforce_admins" {
  type        = bool
  description = "Enforce branch protection for admins"
  default     = true
}

variable "required_approving_review_count" {
  type        = number
  description = "Number of required approving reviews count"
  default     = 1
}

variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}