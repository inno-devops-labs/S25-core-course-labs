variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Name of the GitHub repository"
  type        = string
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  description = "Description of the GitHub repository"
  type        = string
  default     = "Core course labs for S25"
}

variable "repository_visibility" {
  description = "Repository visibility (private or public)"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch name"
  type        = string
  default     = "master"
}
