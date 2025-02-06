variable "github_owner" {
  description = "The GitHub owner (username or organization)"
  type        = string
  default     = "SergePolin"
}

variable "repository_name" {
  description = "The name of the GitHub repository"
  type        = string
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  description = "The description of the GitHub repository"
  type        = string
  default     = "Core Course Labs Repository for S25"
}

variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
} 