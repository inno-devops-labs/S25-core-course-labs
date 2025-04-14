# main.tf

# Provider configuration
terraform {
  required_providers {
    github = {
      source = "hashicorp/github"
    }
  }
}

provider "github" {
  
}

# Variables
variable "repository_name" {
  description = "Name of the GitHub repository"
  type        = string
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  description = "Description of the GitHub repository"
  type        = string
  default     = "Core course labs repository containing Moscow Time web application"
}

# Repository resource
resource "github_repository" "core-course-labs" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = "public"

  has_issues      = true
  has_wiki        = false
  has_downloads   = true
  has_projects    = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true

  auto_init = true
}

# Branch protection
resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "main"

  required_status_checks {
    strict = true
    contexts = ["tests"]
  }

  required_pull_request_reviews {
    required_approving_review_count = 1
  }

  enforce_admins = true
}

# Outputs
output "repository_url" {
  value = github_repository.core-course-labs.html_url
}

output "repository_git_url" {
  value = github_repository.core-course-labs.git_clone_url
}