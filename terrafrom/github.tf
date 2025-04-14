terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "course_repo" {
  name        = "S25-core-course-labs"
  description = "Terraform-managed repository"
  visibility  = "public"
  auto_init   = true
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.course_repo.node_id
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = ["CI Pipeline"]
  }
}
