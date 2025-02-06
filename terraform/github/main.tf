terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "core_course_labs" {
  name               = "core-course-labs"
  description        = "Repository for core DevOps course labs"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "main" {
  repository     = github_repository.core_course_labs.name
  branch         = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.core_course_labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
