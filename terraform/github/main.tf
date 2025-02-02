terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {}

resource "github_repository" "core-course-labs" {
  name        = "core-course-labs"
  description = "DevOps Engineering Course Labs"
  visibility  = "public"

  allow_merge_commit = true
  has_issues        = true
  has_wiki          = true

  delete_branch_on_merge = true
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
} 