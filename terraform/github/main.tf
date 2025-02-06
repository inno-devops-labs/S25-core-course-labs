provider "github" {
  token = var.github_token
}

resource "github_repository" "s25_core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Repository for Terraform Lab"
  visibility  = "public"
  auto_init   = true
  has_issues  = true
  has_wiki    = false
  has_projects = true
  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
  delete_branch_on_merge = false
  vulnerability_alerts = true

  security_and_analysis {
    secret_scanning {
      status = "enabled"
    }
    secret_scanning_push_protection {
      status = "enabled"
    }
  }
}
