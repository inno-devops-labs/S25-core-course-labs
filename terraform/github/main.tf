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

resource "github_repository" "repository" {
  name               = var.repository_name
  description        = var.repository_description
  visibility         = var.repository_visibility
}

resource "github_branch_default" "default_branch" {
  repository = github_repository.repository.name
  branch     = var.default_branch_name
}

resource "github_branch_protection" "default_branch_protection" {
  repository_id                   = github_repository.repository.id
  pattern                         = var.default_branch_name
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}
