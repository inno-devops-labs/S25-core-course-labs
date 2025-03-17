terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "repo" {
  name          = var.repository_name
  description   = var.repository_description
  visibility    = var.repository_visibility
  has_downloads = var.has_downloads
  has_issues    = var.has_issues
  has_wiki      = var.has_wiki
  has_projects  = var.has_projects
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "master" {
  repository_id = github_repository.repo.node_id
  pattern       = var.default_branch
  required_status_checks {
    strict   = var.strict
    contexts = []
  }
  enforce_admins = var.enforce_admins
  required_pull_request_reviews {
    dismiss_stale_reviews      = var.dismiss_stale_reviews
    require_code_owner_reviews = var.require_code_owner_reviews
  }
}
