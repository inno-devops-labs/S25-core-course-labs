terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "my_repo" {
  name        = var.repo_name
  description = var.repo_desc
  visibility  = var.repo_vis
}

resource "github_branch_default" "master" {
  repository = github_repository.my_repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "pro" {
  repository_id     = github_repository.my_repo.id
  pattern           = github_branch_default.master.branch
  enforce_admins    = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}