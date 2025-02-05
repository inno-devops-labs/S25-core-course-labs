provider "github" {
  token = var.github_token
  owner = var.github_owner
}

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

resource "github_repository" "my_repo" {
  name        = "terraform-lab-repo"
  description = "This is a Terraform-managed repository"
  visibility  = "public"

  auto_init    = true
  default_branch = "main"
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.my_repo.node_id
  pattern       = "main"

  enforce_admins = true
  required_status_checks {
    strict = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    required_approving_review_count = 1
  }
}

resource "github_repository" "existing_repo" {
  name        = "S25-core-course-labs"
  description = "Existing repository managed by Terraform"
  visibility  = "public"
}

