variable "token" {
  type        = string
  description = "GitHub Personal Access Token (PAT)"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Organization name"
  default     = "devops-terraform-test-team"
}

variable "repository_name" {
  type        = string
  description = "Github repo name"
  default     = "github_teams_test"
}

variable "repository_description" {
  type        = string
  description = "Repo description"
  default     = "repo for devops course lab4"
}

variable "repository_visibility" {
  type        = string
  description = "Visibility of the"
  default     = "public"
}
