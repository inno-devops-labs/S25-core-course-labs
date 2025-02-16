terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}
provider "github" {
  token = var.github_token       
}

resource "github_repository" "core_course_labs" {
  name           = "S25-core-course-labs"
  description    = "Repository for core DevOps course labs"
  visibility     = "public"

  has_issues    = true
  has_wiki      = true
  has_projects  = true
  has_downloads = true  
  
  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
}

resource "github_branch_default" "master" {
  repository     = github_repository.core_course_labs.name
  branch         = "master"
}

resource "github_branch_protection" "default" {
  repository_id  = github_repository.core_course_labs.node_id
  pattern = github_branch_default.master.branch
  enforce_admins = true

  required_status_checks {
    strict   = true
    contexts = []
  }
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
