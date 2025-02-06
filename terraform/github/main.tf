terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  # Token will be provided via GITHUB_TOKEN environment variable
}

resource "github_repository" "core-course-labs" {
  name        = "core-course-labs"
  description = "Core Course Labs Repository"
  visibility  = "public"

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  auto_init         = true
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "main"

  required_status_checks {
    strict = true
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    required_approving_review_count = 1
  }

  enforce_admins = true
} 