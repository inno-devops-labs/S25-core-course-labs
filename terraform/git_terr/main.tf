terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token   = var.github_token
  owner   = "UTKANOS-RIBA"
}

resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Repository for managing core course labs"
  visibility  = "public"
  has_issues  = true
  has_projects = false
  has_wiki    = false
}

resource "github_branch_protection" "main_protection" {
  repository_id = github_repository.core_course_labs.id
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = ["ci/test"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }

  enforce_admins = true
}
