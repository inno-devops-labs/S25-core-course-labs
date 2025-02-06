output "repositories" {
  value = [
    {
      name           = github_repository.repo.name
      default_branch = github_branch_default.main.branch
      id             = github_repository.repo.id
    },
  ]
}