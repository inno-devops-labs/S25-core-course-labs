terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
}

# public GitHub repository
resource "github_repository" "devops_labs" {
  name               = "S25-core-course-labs"
  description        = "DevOps Labs Repository"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = false
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

# default branch is 'lab4'
resource "github_branch_default" "default_branch" {
  repository = github_repository.devops_labs.name
  branch     = "lab4"
}

# protect the default branch with branch protection rules
resource "github_branch_protection" "branch_protection" {
  repository_id                   = github_repository.devops_labs.id
  pattern                         = github_branch_default.default_branch.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  # require pull request reviews before merging
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
