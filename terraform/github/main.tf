terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.visibility
  auto_init    = true
  has_issues   = true
  license_template   = "mit"
  has_projects = false
  has_wiki     = false
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.repo.node_id
  pattern       = var.default_branch

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    required_approving_review_count = 1
  }

  enforce_admins = true
}