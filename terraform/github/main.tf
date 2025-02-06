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
  name             = "S25-core-course-lab4-TF"
  description      = "Lab 4 repository, which is connected to the Terraform config."
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch" "master" {
  repository = github_repository.repo.name
  branch     = "master"
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
  name        = "S25-core-course-labs"
  description = "This description was changed by the Terraform config."
}