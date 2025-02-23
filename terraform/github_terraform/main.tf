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
  name          = "S25-core-course-labs"
  description   = "S25 DevOps course labs"
  has_downloads = true
  visibility    = "public"
  has_issues    = false
  has_projects  = true
  has_wiki      = true
  auto_init     = false
}

resource "github_branch_protection" "master" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "master"

  required_pull_request_reviews {
    required_approving_review_count = 1
    dismiss_stale_reviews           = true
  }

  enforce_admins = false
}