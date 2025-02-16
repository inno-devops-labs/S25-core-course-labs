variable "github_token" {
  type        = string
  description = "GitHub Personal Access Token"
  sensitive   = true
}

variable "github_owner" {
  type        = string
  description = "GitHub user or organization name"
  default     = "MohamadSafi"
}

variable "repo_name" {
  type        = string
  description = "Name of the existing GitHub repository"
  default     = "S25-core-course-labs"
}

variable "repo_description" {
  type        = string
  default     = "Repository for core course labs"
}

variable "repo_visibility" {
  type        = string
  default     = "public" 
}

variable "default_branch" {
  type        = string
  default     = "master"
}
