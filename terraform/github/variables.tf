variable "token" {
  type        = string
  description = "Specifies the `GITHUB_TOKEN`"
  sensitive   = true
}

variable "repository_name" {
  default     = "devops-lab4-terraform-repo"
  description = "Repo name"
  type        = string
}

variable "repository_description" {
  default     = "Repo created from terraform for lab4 at DevOps course in Innopolis University"
  description = "Repo description"
  type        = string
}

variable "default_branch" {
  default     = "main"
  description = "Default branch"
  type        = string
}

variable "repository_visibility" {
  default     = "public"
  description = "Repo visibility"
  type        = string
}

variable "has_downloads" {
  default     = true
  description = "GitHub downloads (on / false)"
  type        = bool
}

variable "has_issues" {
  default     = false
  description = "GitHub issues (on / false)"
  type        = bool
}

variable "has_wiki" {
  default     = false
  description = "GitHub wiki (on / false)"
  type        = bool
}

variable "has_projects" {
  default     = false
  description = "GitHub projects (on / false)"
  type        = bool
}

variable "license_template" {
  default     = "mit"
  description = "Template of LICENSE"
  type        = string
}

variable "auto_init" {
  default     = true
  description = "Repo automatic initialization with README.md (on / false)"
  type        = bool
}