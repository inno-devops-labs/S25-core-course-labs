terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "devops-labs" {
  name       = "S25-core-course-labs"
  visibility = "public"
  has_issues = true
  has_wiki   = true
  auto_init  = true
}

resource "github_branch_default" "master" {
  repository = github_repository.devops-labs.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops-labs.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
