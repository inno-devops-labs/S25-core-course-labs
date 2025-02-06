terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.github_token
}

# team for maintainers with 'maintain' permissions
resource "github_team" "repo_maintainers" {
  name        = "Maintainers Team"
  description = "Team responsible for maintaining the repository"
  privacy     = "closed"
}

# team for contributors with 'push' permissions
resource "github_team" "repo_contributors" {
  name        = "Contributors Team"
  description = "Team contributing to the repository"
  privacy     = "closed"
}

# GitHub repository
resource "github_repository" "devops_labs" {
  name        = "S25-core-course-labs"
  description = "Repository for DevOps labs"
  visibility  = "public"
  has_issues  = true
  auto_init   = true
}

# default branch is 'lab3'
resource "github_branch_default" "default_branch" {
  repository = github_repository.devops_labs.name
  branch     = "lab3"
}

# Protect the default branch
resource "github_branch_protection" "branch_protection" {
  repository_id                   = github_repository.devops_labs.id
  pattern                         = github_branch_default.default_branch.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  # pull request reviews before merging
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

# 'maintain' permissions to the maintainers team
resource "github_team_repository" "team_maintainers" {
  team_id    = github_team.repo_maintainers.id
  repository = github_repository.devops_labs.name
  permission = "maintain"
}

# 'push' permissions to the contributors team
resource "github_team_repository" "team_contributors" {
  team_id    = github_team.repo_contributors.id
  repository = github_repository.devops_labs.name
  permission = "push"
}
