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

resource "github_branch_default" "default" {
  repository = "lab"
  branch     = "main"
}

resource "github_branch" "main_branch" {
  repository = "lab"
  branch     = "main"
}

resource "github_branch_protection" "main_branch_protection" {
  repository_id = "lab"
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
  }

  allows_deletions    = false
  allows_force_pushes = false
}
