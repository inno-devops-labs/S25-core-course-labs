variable "token" {
    type = string
    description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
    sensitive = true
}

variable "repository_name" {
  type        = string
  description = "Name of the GitHub repository"
  default = "S25-core-course-labs-lab-4-terraform-test"
}

variable "repository_description" {
  type        = string
  description = "Description of the GitHub repository"
  default = "DevOps lab4 terraform test"
}

variable "repository_visibility" {
  type        = string
  description = "Visibility of the repository (private or public)"
  default     = "public"
}

variable "default_branch" {
  type        = string
  description = "Default branch name"
  default     = "main"
}