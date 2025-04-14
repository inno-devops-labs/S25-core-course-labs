terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
    token = var.github_token
}

resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Repository for core course labs"
  visibility  = "public"
  has_issues  = true
  has_projects = false
}

resource "github_branch_default" "default" {
  repository = github_repository.core_course_labs.name
  branch     = "Lab-4"
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core_course_labs.name
  pattern       = "master"

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    require_code_owner_reviews = true
  }

  required_status_checks {
    strict   = true
    contexts = ["ci/workflow"]
  }
}

variable "github_token" {
  description = "GitHub Personal Access Token"
  sensitive   = true
}

output "repository_url" {
  value = github_repository.core_course_labs.html_url
}

output "default_branch" {
  value = github_branch_default.default.branch
}