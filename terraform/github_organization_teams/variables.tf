variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Github Organization"
  default     = "InnopolisUniversityGlebBugaev"
}

variable "repo_config" {
  type = object({
    name          = string
    desc          = string
    visibility    = string
    has_downloads = bool
    has_projects  = bool
    has_wiki      = bool
    auto_init     = bool
  })
  default = {
    name          = "TestRepository"
    desc          = "DevOps lab test"
    visibility    = "public"
    has_downloads = true
    has_projects  = true
    has_wiki      = true
    auto_init     = true
  }
}

variable "default_branch" {
  type        = string
  description = "Default branch"
  default     = "main"
}

variable "require_conversation_resolution" {
  type        = bool
  description = "Require conversation resolution before merging"
  default     = true
}

variable "enforce_admins" {
  type        = bool
  description = "Enforce branch protection for admins"
  default     = true
}



variable "team_1_config" {
  type = object({
    name       = string
    desc       = string
    privacy    = string
    permission = string
  })
  default = {
    name       = "Team 1"
    desc       = "The first team"
    privacy    = "closed"
    permission = "push"
  }
}

variable "team_2_config" {
  type = object({
    name       = string
    desc       = string
    privacy    = string
    permission = string
  })
  default = {
    name       = "Team 2"
    desc       = "The second team"
    privacy    = "closed"
    permission = "triage"
  }
}
