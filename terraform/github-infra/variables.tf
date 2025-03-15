variable "github_token" {
  type        = string
  description = "GitHub API token."
}

variable "github_organization" {
  type = string
  description = "GitHub organization"
}

variable "repository_name" {
  type        = string
  description = "The name of the GitHub repository."
}

variable "repository_description" {
  type        = string
  description = "A brief description of the repository."
  default     = ""
}

variable "visibility" {
  type        = string
  description = "The visibility of the repository (public or private)."
  default     = "public"
}

variable "default_branch" {
  type        = string
  description = "The default branch of the repository."
  default     = "master"
}