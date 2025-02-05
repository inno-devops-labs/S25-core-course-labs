variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "repo_config" {
  type = object({
    name          = string
    desc          = string
    visibility    = string
    has_downloads = bool
    has_projects  = bool
    has_wiki      = bool
  })
  default = {
    name          = "S25-core-course-labs"
    desc          = "DevOps labs solution"
    visibility    = "public"
    has_downloads = true
    has_projects  = true
    has_wiki      = true
  }
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