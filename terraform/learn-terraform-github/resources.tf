#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name               = "learn-terraform-github-lab4"
  description        = "This repository shows how to integrate terraform and github"
  visibility         = "public"
  has_issues         = false
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. 
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}



resource "github_repository" "S25-core-course-labs" {
  name        = "S25-core-course-labs"
  description = var.description

  visibility = "public"

}


#Create branch protection rule to protect the default branch.
resource "github_branch_protection" "S25-core-course-labs" {
  repository_id                   = github_repository.S25-core-course-labs.id
  pattern                         = "master"
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}