terraform {
  required_providers {
    github = {
      source = "hashicorp/github"
      version = "4.0.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = "your-github-username"
}

resource "github_repository" "my_repo" {
  name        = "core-course-labs"
  description = "Terraform GitHub infrastructure setup"
  visibility  = "private"  # или "public"
  default_branch = "main"
}

resource "github_branch_protection" "default_branch_protection" {
  repository = github_repository.my_repo.name
  branch     = github_repository.my_repo.default_branch

  required_status_checks {
    strict   = true
    contexts = []
  }

  enforce_admins = true
  required_pull_request_reviews {
    dismiss_stale_reviews = true
  }
}
