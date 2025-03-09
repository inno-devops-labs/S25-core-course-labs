variable "github_token" {
  description = "GitHub token with repo admin rights"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = " "
  type        = string
}

variable "repo_name" {
  description = " "
  type        = string
  default     = "lab4"
}

variable "repo_description" {
  description = " "
  type        = string
  default     = "Repository managed by Terraform"
}

variable "repo_visibility" {
  description = "Repository visibility: public, private, or internal"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch for the repository"
  type        = string
  default     = "lab4"
}
