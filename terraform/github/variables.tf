variable "token" {
  type        = string
  description = "GitHub token"
  sensitive   = true
}

variable "repository_name" {
  type        = string
  description = "Repository name"
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  type        = string
  description = "Repository description"
  default     = "S25 DevOps course labs"
}

variable "repository_visibility" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}

variable "repository_has_issues" {
  type        = bool
  description = "Issues in the repository"
  default     = false
}

variable "repository_has_wiki" {
  type        = bool
  description = "Wiki in the repository"
  default     = false
}

variable "repository_auto_init" {
  type        = bool
  description = "Initialize the repository with a README"
  default     = true
}

variable "repository_license" {
  type        = string
  description = "Repository license"
  default     = "mit"
}

variable "repository_gitignore_template" {
  type        = string
  description = "Gitignore template for the repository"
  default     = "VisualStudio"
}

variable "default_branch" {
  type        = string
  description = "Default branch"
  default     = "master"
}

variable "require_conversation_resolution" {
  type        = bool
  description = "Require resolution of conversation before merging"
  default     = true
}

variable "enforce_admins" {
  type        = bool
  description = "Enforce protection of the default branch for admins"
  default     = true
}

variable "required_approving_review_count" {
  type        = number
  description = "Number of approving reviews required"
  default     = 1
}
