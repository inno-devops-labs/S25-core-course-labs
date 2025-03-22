variable "token" {
  type        = string
  description = "GitHub token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Github Organization"
  default     = "BasedLangsOrg"
}

variable "repo_name" {
  type        = string
  description = "Repository name"
  default     = "BasedLangsRepo"
}

variable "repo_desc" {
  type        = string
  description = "Repository description"
  default     = "This is the repository that belongs to the most based languages to exist"
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
  default     = true
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
  default     = "main"
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

variable "rust_team_name" {
  type        = string
  description = "Name of the Rust team"
  default     = "Rustaceans"
}

variable "rust_team_desc" {
  type        = string
  description = "Description of the rust team"
  default     = "Team consisting of based rust devs"
}

variable "rust_team_privacy" {
  type        = string
  description = "Privacy setting for the rust team"
  default     = "closed"
}

variable "golang_team_name" {
  type        = string
  description = "Name of the Goland team"
  default     = "Golangers"
}

variable "golang_team_desc" {
  type        = string
  description = "Description of the Golang team"
  default     = "Team consisting of (slightly less) based go devs"
}

variable "golang_team_privacy" {
  type        = string
  description = "Privacy setting for the golang team"
  default     = "closed"
}

variable "dev_member_username" {
  type        = string
  description = "Username of a rustacean"
  default     = "crab"
}

variable "dev_member_role" {
  type        = string
  description = "Role of a crab"
  default     = "member"
}

variable "qa_member_username" {
  type        = string
  description = "Username of a golanger"
  default     = "hamster"
}

variable "qa_member_role" {
  type        = string
  description = "Role of a hamster"
  default     = "member"
}

variable "rust_team_permission" {
  type        = string
  description = "Repository permission level for the crabs"
  default     = "push"
}

variable "golang_team_permission" {
  type        = string
  description = "Repository permission level for the hamsters"
  default     = "push"
}
