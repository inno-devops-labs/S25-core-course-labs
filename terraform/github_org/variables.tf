variable "github_token" {
  description = "GitHub token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Name of the GitHub repository"
  type        = string
  default     = "devops-lab-v2"
}

variable "repository_description" {
  description = "Description of the GitHub repository"
  type        = string
  default     = "Repo for DevOps course lab"
}

variable "visibility" {
  description = "Visibility of the GitHub repository"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch of the GitHub repository"
  type        = string
  default     = "main"
}

variable "auto_init" {
  description = "Auto init"
  type        = bool
  default     = true
}

variable "fork" {
  description = "Whether the repository is a fork"
  type        = bool
  default     = false
}

variable "organization" {
  description = "Name of the GitHub organization"
  type        = string
  default     = "devops-team-lab"
}

variable "teams" {
  description = "List of teams"
  type = list(object({
    name        = string
    description = string
    permission  = string
  }))
  default = [
    {
      name        = "admins2"
      description = "Team with admin access"
      permission  = "admin"
    },
    {
      name        = "developers2"
      description = "Team with write access"
      permission  = "push"
    },
    {
      name        = "readers2"
      description = "Team with read access"
      permission  = "pull"
    }
  ]
}
