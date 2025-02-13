terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = "NikaChek"
}

variable "github_token" {
  description = "GitHub API Token"
  type        = string
  default     = ""
  sensitive   = true
}

resource "github_branch_default" "default" {
  repository = github_repository.core_course_labs.name
  branch     = "master"
}

resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Infrastructure as Code with Terraform"
  visibility  = "public"
  has_issues  = true
  has_wiki    = false
  auto_init   = true
}

resource "github_branch_protection" "master" {
  repository_id = github_repository.core_course_labs.name
  pattern       = "master"
  
  required_status_checks {
    strict   = true
    contexts = ["ci/circleci"]
  }
  
  enforce_admins = true
  required_pull_request_reviews {
    dismiss_stale_reviews      = true
    require_code_owner_reviews = true
  }
  
}

