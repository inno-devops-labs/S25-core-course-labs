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
  name        = "core-course-labs"
  description = "Repository for terraform lab"
  visibility  = "public"
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.my_repo.node_id
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }
}
