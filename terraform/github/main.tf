terraform {
  #  required_version = "~> 1.2.0"
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

resource "github_repository" "S25-core-course-labs" {
  name        = "S25-core-course-labs"
  description = "For DevOps course"
  visibility  = "public"
}

#Set default branch 'master'
resource "github_branch_default" "master" {
  repository = github_repository.S25-core-course-labs.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.S25-core-course-labs.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
