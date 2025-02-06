resource "github_repository" "core-course-labs" {
  name        = "S25-core-course-labs"
  description = "Repository for managing core course labs"
  visibility  = "public"
  has_issues  = true
  has_wiki    = false
  has_projects = false
}

resource "github_branch_default" "master" {
  repository = github_repository.core-course-labs.name
  branch     = "master"
}