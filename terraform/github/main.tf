terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "core-course-labs" {
  name       = "S25-core-course-labs"
  description = "DevOps Engineering Course Labs"
  visibility  = "public"

  allow_merge_commit = true
  has_issues        = true
  has_wiki          = true

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