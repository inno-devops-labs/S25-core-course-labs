# Configure the GitHub provider
terraform {
  required_providers {
    github = {
      source = "integrations/github"
      version = "5.0.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = var.github_organization  
}

# Import the existing repository into Terraform state
import {
  to = github_repository.core-course-labs
  id = "DevOps-2025-lab4/core-course-labs"  
}

# Define the repository resource
resource "github_repository" "core-course-labs" {
  name               = "core-course-labs"
  description        = "Lab assignments for Core Course"
  visibility         = "public"
  auto_init          = true
  license_template   = "mit"
}

# Create teams in the organization
resource "github_team" "admins" {
  name        = "admins"
  description = "Admin team with full access"
  privacy     = "closed"
}

resource "github_team" "maintainers" {
  name        = "maintainers"
  description = "Maintainers with push access"
  privacy     = "closed"
}

resource "github_team" "contributors" {
  name        = "contributors"
  description = "Contributors with read access"
  privacy     = "closed"
}

# Assign teams to the repository with permissions
resource "github_team_repository" "admins_access" {
  team_id    = github_team.admins.id
  repository = github_repository.core-course-labs.name
  permission = "admin"  # Full access
}

resource "github_team_repository" "maintainers_access" {
  team_id    = github_team.maintainers.id
  repository = github_repository.core-course-labs.name
  permission = "push"   # Write access
}

resource "github_team_repository" "contributors_access" {
  team_id    = github_team.contributors.id
  repository = github_repository.core-course-labs.name
  permission = "pull"   # Read-only access
}
