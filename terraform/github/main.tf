terraform {
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
  name        = var.repo_name
  description = var.repo_description
  visibility  = var.repo_visibility
  auto_init   = true
  has_issues  = true
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.default.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

