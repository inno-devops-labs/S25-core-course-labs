variable "github_token" {
  description = "GitHub token"
  type        = string
  sensitive   = true
}

variable "repo_name" {
  description = "Repository name"
  default     = "S25-core-course-labs"
  type        = string
}

variable "repo_description" {
  default = "Repository for the DevOps course"
  type    = string
}

variable "visibility" {
  description = "Visibility"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch"
  type        = string
  default     = "master"
}

variable "auto_init" {
  description = "Auto init"
  type        = bool
  default     = true
}
