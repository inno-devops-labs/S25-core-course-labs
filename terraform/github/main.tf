terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
}

resource "github_repository" "repo" {
  name        = var.repo_name
  description = var.repo_description
  visibility  = var.repo_visibility
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = var.repo_default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}