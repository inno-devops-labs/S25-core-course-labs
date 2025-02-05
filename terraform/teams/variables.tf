variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "organization_name" {
  description = "GitHub Organization Name"
  type        = string
}

variable "repository_name" {
  description = "GitHub Repository Name"
  type        = string
}

variable "teams" {
  description = "Teams with access levels"
  type        = map(object({
    description  = string
    permission   = string
  }))
  default = {
    "developers" = { description = "Development Team", permission = "push" }
    "qa"         = { description = "Quality Assurance Team", permission = "triage" }
    "admins"     = { description = "Admin Team", permission = "admin" }
    "viewers"    = { description = "Read-Only Access", permission = "pull" }
  }
}
