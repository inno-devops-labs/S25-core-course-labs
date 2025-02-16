variable "token" {
  type      = string
  sensitive = true
}

variable "repo_name" {
  type    = string
  default = "DemoRepo"
}

variable "visibility" {
  type    = string
  default = "public"
}

variable "description" {
  type    = string
  default = "Demo repo for lab"
}

variable "has_issues" {
  type    = bool
  default = false
}

variable "has_wiki" {
  type    = bool
  default = false
}

variable "auto_init" {
  type    = bool
  default = true
}

variable "license_template" {
  type    = string
  default = "mit"
}

variable "gitignore_template" {
  type    = string
  default = "VisualStudio"
}

variable "default_branch" {
  type    = string
  default = "main"
}

variable "require_conversation_resolution" {
  type    = bool
  default = true
}

variable "enforce_admins" {
  type    = bool
  default = true
}

variable "required_approving_review_count" {
  type    = number
  default = 1
}

variable "team1_permission" {
  type    = string
  default = "push"
}

variable "team2_permission" {
  type    = string
  default = "triage"
}

variable "team1_name" {
  type    = string
  default = "Developers"
}

variable "team2_name" {
  type    = string
  default = "Testers"
}

variable "team1_desc" {
  type    = string
  default = "Team of developers"
}

variable "team2_desc" {
  type    = string
  default = "Team of testers"
}

variable "team1_privacy" {
  type    = string
  default = "closed"
}

variable "team2_privacy" {
  type    = string
  default = "closed"
}