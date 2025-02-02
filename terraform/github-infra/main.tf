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
  owner = var.github_organization
}

resource "github_repository" "devops" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.visibility
  auto_init   = true

  allow_merge_commit     = false
  delete_branch_on_merge = true
}

resource "github_branch_protection" "master_branch_protection" {
  repository_id = github_repository.devops.node_id
  pattern       = var.default_branch

  enforce_admins = true

  required_status_checks {
    strict   = true
    contexts = ["ci"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }
}
