terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = "s25-devops-terraform-lab"
}

# New repository
resource "github_repository" "mock" {
  name        = "tf-mock"
  description = "This is a mock repository for testing purposes."
  visibility  = "public"
}

# Read-only team
resource "github_team" "reader" {
  name        = "reader"
  description = "This team has read-only access to the repositories."
  privacy     = "closed"
}

resource "github_team_members" "reader" {
  team_id = github_team.reader.id

  members {
    username = "saleemasekrea000"
    role     = "member"
  }
}

# Write team
resource "github_team" "writer" {
  name        = "writer"
  description = "This team has write access to the repositories."
}

resource "github_team_members" "writer" {
  team_id = github_team.writer.id

  members {
    username = "saleemasekrea000"
    role     = "member"
  }
}
