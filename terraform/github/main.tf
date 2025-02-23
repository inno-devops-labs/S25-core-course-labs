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
  name               = var.repo_name
  description        = var.repo_desc
  visibility         = var.repo_visibility
  has_issues         = var.repo_has_issues
  has_wiki           = var.repo_has_wiki
  auto_init          = var.repo_auto_init
  license_template   = var.repo_license
  gitignore_template = var.repo_gitignore
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
