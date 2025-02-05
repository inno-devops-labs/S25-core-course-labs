variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Github Organization"
  default     = "AmogusOrg"
}

variable "repo_name" {
  type        = string
  description = "Repository name"
  default     = "Sus25-core-course-labs"
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
  description = "Auto-initialize repository with README"
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
  default     = "Go"
}

variable "default_branch" {
  type        = string
  description = "Default branch for the repository"
  default     = "main"
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

variable "dev_team_name" {
  type        = string
  description = "Name of the development team"
  default     = "Developers"
}

variable "dev_team_desc" {
  type        = string
  description = "Description of the development team"
  default     = "Team responsible for development"
}

variable "dev_team_privacy" {
  type        = string
  description = "Privacy setting for the development team"
  default     = "closed"
}

variable "qa_team_name" {
  type        = string
  description = "Name of the QA team"
  default     = "QA"
}

variable "qa_team_desc" {
  type        = string
  description = "Description of the QA team"
  default     = "Quality assurance team"
}

variable "qa_team_privacy" {
  type        = string
  description = "Privacy setting for the QA team"
  default     = "closed"
}

variable "dev_member_username" {
  type        = string
  description = "Username of a development team member"
  default     = "developer_username"
}

variable "dev_member_role" {
  type        = string
  description = "Role of the development team member"
  default     = "member"
}

variable "qa_member_username" {
  type        = string
  description = "Username of a QA team member"
  default     = "qa_username"
}

variable "qa_member_role" {
  type        = string
  description = "Role of the QA team member"
  default     = "member"
}

variable "dev_team_permission" {
  type        = string
  description = "Repository permission level for the development team"
  default     = "push"
}

variable "qa_team_permission" {
  type        = string
  description = "Repository permission level for the QA team"
  default     = "triage"
}
