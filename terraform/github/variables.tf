variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "The name of the GitHub repository"
  type        = string
  default     = "terraform-managed-repo"
}

variable "repository_description" {
  description = "Description of the GitHub repository"
  type        = string
  default     = "Repository managed via Terraform"
}

variable "repository_visibility" {
  description = "Visibility of the GitHub repository"
  type        = string
  default     = "private"
}

variable "default_branch" {
  description = "Default branch of the GitHub repository"
  type        = string
  default     = "main"
}

variable "branch_protection_enabled" {
  description = "Enable branch protection"
  type        = bool
  default     = false
}

variable "require_code_owner_reviews" {
  description = "Require code owner reviews for pull requests"
  type        = bool
  default     = true
}

variable "required_approving_review_count" {
  description = "Number of required approvals for a pull request"
  type        = number
  default     = 1
}
