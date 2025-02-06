provider "github" {
  token = var.token
}

resource "github_repository" "terraform-course" {
  name             = "terraform-course"
  description      = "Test terraform for multiple teams"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

# Set default branch to "main"
resource "github_branch_default" "main" {
  repository = github_repository.terraform-course.name
  branch     = "main"
}

# Create branch protection rule to protect the default branch
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.terraform-course.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "workers" {
  name        = "workers"
  description = "Casual workers"
}

resource "github_team" "admins" {
  name        = "admins"
  description = "Casual admins"
}

resource "github_team_repository" "workers" {
  team_id    = github_team.workers.id
  repository = github_repository.terraform-course.name
  permission = "push"
}

resource "github_team_repository" "admins" {
  team_id    = github_team.admins.id
  repository = github_repository.terraform-course.name
  permission = "admin"
}