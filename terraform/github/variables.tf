variable "token" {
  type        = string
  description = "GitHub Token"
  sensitive   = true
}

variable "repo_name" {
  type        = string
  description = "Repo name"
  default     = "S25-core-course-labs"
}

variable "repo_desc" {
  type        = string
  description = "Repo description"
  default     = "My very incredible solution for DevOps Labs"
}

variable "repo_visibility" {
  type        = string
  description = "Visibility"
  default     = "public"
}

variable "repo_has_issues" {
  type        = bool
  description = "Issues"
  default     = true
}

variable "repo_has_wiki" {
  type        = bool
  description = "Wiki"
  default     = false
}

variable "repo_auto_init" {
  type        = bool
  description = "README auto init"
  default     = false
}

variable "repo_license" {
  type        = string
  description = "License"
  default     = "mit"
}

variable "repo_gitignore" {
  type        = string
  description = "Gitignore"
  default     = "Python"
}

variable "default_branch" {
  type        = string
  description = "Default Branch"
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
  description = "Required approving reviews number"
  default     = 1
}
