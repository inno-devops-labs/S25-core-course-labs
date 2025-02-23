terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_pat
}

resource "github_repository" "core-course-labs" {
  name             = "S25-core-course-labs"
  description      = "S25 core course labs"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "master" {
  repository = github_repository.core-course-labs.name
  branch     = "master"
}

resource "github_branch_protection" "repo_master" {
  repository_id                   = github_repository.core-course-labs.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
