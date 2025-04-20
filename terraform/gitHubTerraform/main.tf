terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

variable "github_token" {
  description = "GitHub Token for authentication"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "The name of the GitHub repository"
  type        = string
}

variable "repository_description" {
  description = "A short description of the repository"
  type        = string
}

variable "repository_visibility" {
  description = "Visibility of the repository (public or private)"
  type        = string
  default     = "private"
}

variable "default_branch" {
  description = "The default branch of the repository"
  type        = string
  default     = "main"
}

resource "github_repository" "repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.repository_visibility
  auto_init   = true
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "main_protection" {
  repository_id = github_repository.repo.name
  pattern       = var.default_branch

  enforce_admins = true

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }

  required_status_checks {
    strict = true
    contexts = ["ci/test", "ci/lint"]
  }
}
