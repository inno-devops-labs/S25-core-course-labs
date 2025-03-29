terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
  required_version = ">= 0.13"
}

provider "github" {
  token = var.token
}

resource "github_repository" "terraform-example" {
  name             = "terraform-example"
  description      = "Test terraform for creating repository"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "main" {
  repository = github_repository.terraform-example.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.terraform-example.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}