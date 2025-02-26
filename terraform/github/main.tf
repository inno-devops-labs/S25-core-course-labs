resource "github_repository" "core-course-labs-v3" {
  name        = var.repo_name
  description = var.repo_description
  visibility  = var.visibility
  auto_init = var.auto_init
}

resource "github_branch_default" "master" {
  repository = var.repo_name
  branch     = var.default_branch
}

resource "github_branch_protection" "core-course-labs-v3" {
  repository_id = github_repository.core-course-labs-v3.id
  pattern       = var.default_branch

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews      = true
    require_code_owner_reviews = true
  }

  enforce_admins = true
}
