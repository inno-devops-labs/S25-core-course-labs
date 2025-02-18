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
  description        = var.description
  visibility         = var.visibility
  has_issues         = var.has_issues
  has_wiki           = var.has_wiki
  auto_init          = var.auto_init
  license_template   = var.license_template
  gitignore_template = var.gitignore_template
}

resource "github_branch_default" "default_branch" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "default_protection" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.default_branch.branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}
