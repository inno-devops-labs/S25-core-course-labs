variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

## REPO SETTINGS

variable "repo_name" {
  type        = string
  description = "The name of the repository"
  default     = "devops-labs-repository"
}

variable "repo_description" {
  type        = string
  description = "The description of the repository"
  default     = "This is repository that will be created by using the terraform for the labs on the DevOPs course"
}

variable "repo_visibility" {
  type        = string
  description = "The visibility of the repository"
  default     = "public"
}

variable "repo_default_branch" {
  type        = string
  description = "The default branch for the repository"
  default     = "master"
}

variable "repo_ignore_template" {
  type        = string
  description = "The .gitignore template"
  default     = "IntelliJ"
}
