terraform {
  required_providers {
    github = {
      source = "integrations/github"
      version = "5.0.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "core-course-labs" {
  name               = "core-course-labs"
  description        = "Lab assignments for Core Course"
  visibility         = "public"
  auto_init          = true
  license_template   = "mit"
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.id
  pattern       = "main"
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
