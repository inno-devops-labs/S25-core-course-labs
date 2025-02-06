output "repository_id" {
  value = github_repository.repo.id
}

output "repository_name" {
  value = github_repository.repo.name
}

output "repository_url" {
  value = github_repository.repo.html_url
}

output "default_branch" {
  value = github_branch_default.default.branch
}
