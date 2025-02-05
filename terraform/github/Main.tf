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
  name        = "S25-core-course-labs"
  description = "Devops 2025 course labs"
  visibility  = "public"

  has_issues    = true
  has_wiki      = true
  has_downloads = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  
  delete_branch_on_merge = false
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "master"

  required_status_checks {
    strict = true
    contexts = ["test", "build"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    required_approving_review_count = 1
  }

  enforce_admins = true
}