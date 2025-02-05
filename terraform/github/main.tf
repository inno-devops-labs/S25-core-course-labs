terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "my_repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.repository_visibility
  auto_init   = true
}

resource "github_branch_protection" "main_branch" {
  count         = var.branch_protection_enabled ? 1 : 0
  repository_id = github_repository.my_repo.node_id
  pattern       = var.default_branch

  required_status_checks {
    strict   = true
    contexts = []
  }

  enforce_admins = true
  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = var.require_code_owner_reviews
    required_approving_review_count = var.required_approving_review_count
  }
}
