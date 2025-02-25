variable "token" {
  type        = string
  description = "GitHub token"
  sensitive   = true
}

variable "repository_name" {
  type        = string
  description = "Repository name"
  default     = "S25-DevOps-Test-Org-Repo-1"
}

variable "repository_description" {
  type        = string
  description = "Repository description"
  default     = "S25 DevOps course labs test repository"
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
  default     = "main"
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

variable "organization" {
  type        = string
  description = "GitHub organization"
  default = "S25-DevOps-Test-Org-1"
}

variable "team_backend_name" {
  type        = string
  description = "Backend team name"
  default     = "backend"
}

variable "team_backend_desc" {
  type        = string
  description = "Backend team description"
  default     = "Backend team"
}

variable "team_backend_privacy" {
  type        = string
  description = "Backend team privacy"
  default     = "closed"
}

variable "team_backend_permission" {
  type        = string
  description = "Backend team permission"
  default     = "push"
}

variable "team_frontend_name" {
  type        = string
  description = "Frontend team name"
  default     = "frontend"
}

variable "team_frontend_desc" {
  type        = string
  description = "Frontend team description"
  default     = "Frontend team"
}

variable "team_frontend_privacy" {
  type        = string
  description = "Frontend team privacy"
  default     = "closed"
}

variable "team_frontend_permission" {
  type        = string
  description = "Frontend team permission"
  default     = "triage"
}
