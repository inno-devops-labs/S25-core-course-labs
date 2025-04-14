terraform {
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

resource "github_repository" "core_course_labs" {
  name        = "core_course_labs"
  description = "Terraform-managed repository for DevOps labs"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
  auto_init   = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "master" {
  repository = github_repository.core_course_labs.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.core_course_labs.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
