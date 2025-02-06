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
  has_issues         = var.repository_has_issues
  has_wiki           = var.repository_has_wiki
  auto_init          = var.repository_auto_init
  license_template   = var.repository_license
  gitignore_template = var.repository_gitignore_template
}

resource "github_branch_default" "master" {
  repository = github_repository.repository.name
  branch     = var.default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repository.id
  pattern                         = var.default_branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}
