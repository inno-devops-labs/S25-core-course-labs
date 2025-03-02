variable "github_token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub owner/organization name"
  type        = string
}

variable "repository_name" {
  description = "Name of the repository to create"
  type        = string
}

variable "repository_description" {
  description = "Description of the repository"
  type        = string
} 