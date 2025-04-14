terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {}

resource "github_repository" "core-course-labs" {
  name        = "S25-core-course-labs"
  description = "Repo for doint tasks on DevOps course in Innopolis University"
  visibility  = "public"

  has_issues    = true
  has_wiki      = true
  has_downloads = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  
  delete_branch_on_merge = false
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.core-course-labs.node_id
  pattern       = "master"
  enforce_admins = true
  required_status_checks {
    strict = true
    contexts = ["build"]
  }
}`