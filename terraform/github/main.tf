terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.GITHUB_TOKEN
}

resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Core course labs for DevOps training"
  visibility  = "public"

  has_issues    = true
  has_wiki      = true
  has_projects  = true
  has_downloads = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  auto_init         = false
}

resource "github_branch_default" "main" {
  repository = github_repository.core_course_labs.name
  branch     = "master"
}

resource "github_branch_protection" "master" {
  repository_id = github_repository.core_course_labs.node_id
  pattern       = "master"

  required_status_checks {
    strict = true
    contexts = ["Python CI"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    required_approving_review_count = 1
  }

  enforce_admins = false
} 