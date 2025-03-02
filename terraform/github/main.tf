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

resource "github_repository" "core_repo" {
  name        = "S25-core-course-labs-terraform"
  description = "such dirty legend like"
  visibility  = "public"
  auto_init   = true
}

resource "github_branch" "main" {
  repository = github_repository.core_repo.name
  branch     = "main"
}

resource "github_branch_default" "main" {
  repository = github_repository.core_repo.name
  branch     = github_branch.main.branch
}

resource "github_branch_protection" "core_repo" {
  repository_id = github_repository.core_repo.id

  pattern = github_branch_default.main.branch

  enforce_admins   = true
  allows_deletions = true

  require_conversation_resolution = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
