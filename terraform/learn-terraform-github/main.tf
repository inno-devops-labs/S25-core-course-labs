terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  # The token is provided through the environment variable.
  token = var.github_token

}

resource "github_repository" "repo" {
  name               = "S25-core-course-labs"
  description        = "My-test-repo"
  visibility         = "public"
  has_issues         = false
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}

#Set default branch 'master'
resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}