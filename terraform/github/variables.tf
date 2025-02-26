variable "token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "repo_name" {
  description = "GitHub repository name"
  type        = string
  default     = "my-terraform-repo"
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

