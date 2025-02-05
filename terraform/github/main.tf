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
  name          = var.repo_config.name
  description   = var.repo_config.desc
  visibility    = var.repo_config.visibility
  has_downloads = var.repo_config.has_downloads
  has_projects  = var.repo_config.has_projects
  has_wiki      = var.repo_config.has_wiki
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = var.default_branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}