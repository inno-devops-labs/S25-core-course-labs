terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "repo" {
  name               = var.github_repo_name
  description        = var.github_repo_description
  visibility         = var.github_repo_visibility
  auto_init          = var.github_repo_auto_init
  has_issues         = var.github_repo_has_issues
  has_wiki           = var.github_repo_has_wiki
  license_template   = var.github_repo_license
  gitignore_template = var.github_repo_gitignore
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.github_default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.default.branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}
