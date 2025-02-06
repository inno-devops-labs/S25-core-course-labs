variable "token" {
  description = "Access token"
  type        = string
  sensitive   = true
}

variable "repo_name" {
  description = "GitHub repository name"
  type        = string
  default     = "S25-core-course-labs"
}

variable "repo_description" {
  description = "Repository description"
  type        = string
  default     = "Smth with terraform"
}

variable "repo_visibility" {
  description = "Repository visibility (public or private)"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "The default branch for the repository"
  default     = "lab4-solution"
}
