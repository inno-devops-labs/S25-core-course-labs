terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.token
}

resource "github_repository" "repo" {
  name             = var.git_repo_name
  description      = var.git_repo_description
  visibility       = var.git_repo_visibility
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = var.git_license
}

resource "github_branch" "master" {
  repository = github_repository.repo.name
  branch     = var.git_repo_default_branch
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = github_branch.master.branch
}

resource "github_branch_protection" "default" {
  repository_id = github_repository.repo.id
  pattern       = github_branch_default.default.branch
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
  require_conversation_resolution = true
  enforce_admins                  = true
}

resource "github_repository" "S25-core-course-labs" {
  name        = var.git_existing_repo_name
  description = var.git_existing_repo_description
}
