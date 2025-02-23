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

resource "github_repository" "S25-core-course-labs" {
  name        = var.repository_name
  description = "Repository for Core Course Labs"
  visibility  = "public"

  has_issues      = true
  has_wiki        = true
  has_downloads   = true
  has_projects    = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  auto_init         = true
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.S25-core-course-labs.node_id
  pattern       = "main"

  required_status_checks {
    strict = true
    contexts = ["build"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    required_approving_review_count = 1
  }
} 