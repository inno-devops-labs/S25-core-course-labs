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
