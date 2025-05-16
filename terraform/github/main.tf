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
  owner = var.github_owner
}


resource "github_repository" "repo" {
  name               = "terraform-github"
  description        = "Github Terraform infrastructure"
  visibility         = "public"
  has_issues         = false
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}


resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "A repo containing materials from the course DevOps Engineering for the year 2025"
  visibility  = "public"
}