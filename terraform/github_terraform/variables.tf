variable "github_token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  default     = "devops-labs"
  description = "GitHub repository name"
  type        = string
}

variable "repository_description" {
  default     = "Innopolis University DevOps Course Labs"
  description = "GitHub repository description"
  type        = string
}

variable "repository_visibility" {
  default     = "public"
  description = "GitHub repository visibility"
  type        = string
}

variable "has_downloads" {
  default     = true
  description = "Enable GitHub downloads"
  type        = bool
}

variable "has_issues" {
  default     = false
  description = "Enable GitHub issues"
  type        = bool
}

variable "has_wiki" {
  default     = false
  description = "Enable GitHub wiki"
  type        = bool
}

variable "has_projects" {
  default     = false
  description = "Enable GitHub projects"
  type        = bool
}

variable "default_branch" {
  default     = "master"
  description = "GitHub default branch"
  type        = string
}

variable "strict" {
  default     = false
  description = "Require branches to be up to date before merging"
  type        = bool
}

variable "enforce_admins" {
  default     = false
  description = "Enforce all configured restrictions for administrators"
  type        = bool
}

variable "dismiss_stale_reviews" {
  default     = false
  description = "Dismiss approved reviews when someone pushes a new commit"
  type        = bool
}

variable "require_code_owner_reviews" {
  default     = false
  description = "Require an approved review in pull requests including files with a designated code owner"
  type        = bool
}
