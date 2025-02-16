terraform {
  required_version = "~> 1.2.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "repo" {
  name = "S25-core-course-labs"
  description = "Codebase"
  visibility = "private"  
  default_branch = "main"
}

resource "github_branch_default" "lab4" {
  repository = github_repository.repo.name
  branch     = "lab4"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}