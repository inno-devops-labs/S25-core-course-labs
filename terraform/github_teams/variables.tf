variable "token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "repo_name" {
  description = "GitHub repository name"
  type        = string
  default     = "terraform-teams"
}

variable "repo_description" {
  description = "Repository description"
  type        = string
  default     = "Managed with Terraform"
}

variable "repo_visibility" {
  description = "Repository visibility (public or private)"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "The default branch for the repository"
  default     = "main"
}

variable "organization" {
  description = "The name of github organization"
  type        = string
  default     = "S25-devops-terraform"
}

