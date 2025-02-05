terraform {
  required_version = "~> 1.10.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "repo" {
  name               = var.repository_name
  description        = "Devops labs"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = "master"
}

resource "github_branch_protection" "branch_protection" {
  repository_id                   = github_repository.repo.name
  pattern                         = github_branch_default.default.branch
  require_conversation_resolution = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }

  required_status_checks {
    strict = true
    contexts = ["check", "test", "build"]
  }
}