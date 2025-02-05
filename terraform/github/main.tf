provider "github" {
  token = var.github_token
}

resource "github_repository" "core-course-labs" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.repository_visibility

  has_issues      = true
  has_wiki        = true
  has_projects    = true
  has_downloads   = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true

  delete_branch_on_merge = true
  auto_init             = true
}

resource "github_branch_default" "master" {
  repository = github_repository.core-course-labs.name
  branch     = var.default_branch
}

resource "github_branch_protection" "master" {
  repository_id = github_repository.core-course-labs.node_id
  pattern      = var.default_branch

  required_status_checks {
    strict = true
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }

  enforce_admins = false
}
