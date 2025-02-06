terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token # Token will be provided via GITHUB_TOKEN environment variable
  owner = var.github_owner
}

resource "github_repository" "core-course-labs" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = "public"

  allow_merge_commit     = true
  allow_squash_merge    = true
  allow_rebase_merge    = true
  delete_branch_on_merge = true
  has_issues           = true
  has_projects         = true
  has_wiki             = true
  vulnerability_alerts = true

  security_and_analysis {
    secret_scanning {
      status = "enabled"
    }
    secret_scanning_push_protection {
      status = "enabled"
    }
  }
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "main"

  required_status_checks {
    strict = true
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    required_approving_review_count = 1
  }

  enforce_admins = true
} 