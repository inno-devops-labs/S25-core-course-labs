output "repository_url" {
  description = "URL of the created repository"
  value       = github_repository.core-course-labs.html_url
}

output "repository_git_clone_url" {
  description = "Git clone URL of the repository"
  value       = github_repository.core-course-labs.git_clone_url
}

output "repository_default_branch" {
  description = "Default branch of the repository"
  value       = github_branch_default.master.branch
}
