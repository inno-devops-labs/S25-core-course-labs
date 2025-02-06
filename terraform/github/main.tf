terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.token != "" ? var.token : (try(env("GITHUB_TOKEN"), ""))
}


resource "github_repository" "S25-core-course-labs" {
  name        = "S25-core-course-labs"
  description = "Repo for DevOp course"
  visibility  = "public"
}



resource "github_branch_default" "lab4" {
  repository = github_repository.S25-core-course-labs.name
  branch     = "lab4"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.S25-core-course-labs.id
  pattern                         = github_branch_default.lab4.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
