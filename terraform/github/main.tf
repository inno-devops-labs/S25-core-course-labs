# Terraform provider block
terraform {
  required_providers {
    github = {
      source  = "hashicorp/github"
      version = "~> 4.0"
    }
  }
}

# GitHub provider configuration
provider "github" {
  token = var.github_token
  owner = "maksalena"  
}

# GitHub repository resource
resource "github_repository" "terraform" {
  name        = "S25-core-course-labs"
  description = "This is a sample repository created using Terraform."
  visibility  = "public" 
  default_branch = "master"

  # Enable branch protection for the default branch
  branch_protection {
    pattern = "master"

    required_status_checks {
      strict   = true
      contexts = ["ci/cd"]
    }

    enforce_admins = true
    required_pull_request_reviews {
      dismissal_restrictions {
        users = ["user1", "user2"]
      }
      require_code_owner_reviews = true
    }
  }
}
