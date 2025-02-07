terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {}

# Add a user to the organization
#     - Visibility settings
#     - Default branch
#     - Branch protection rule for the default branch

resource "github_repository" "lab_repo" {
  name        = "S25-core-course-labs"
  description = "My take at DevOps Engineering course @ Innopolis University"
  visibility  = "public"
  has_issues  = true
  has_wiki    = false
  auto_init   = true

}


resource "github_branch_default" "default" {
  repository = github_repository.lab_repo.name
  branch     = "master"
}

resource "github_branch_protection" "push-protection" {
  
  repository_id = github_repository.lab_repo.name

  pattern          = "master"
  allows_deletions = false

  required_status_checks {
    strict   = true
    contexts = ["enforce-all-checks"]
  }
  allows_force_pushes = false
    required_pull_request_reviews {
    required_approving_review_count = 0
    }
}
