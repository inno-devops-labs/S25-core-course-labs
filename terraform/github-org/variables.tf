variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}

variable "org_name" {
  type    = string
  default = "terrain-corp"
}

variable "org_editors_name" {
  type    = string
  default = "terrainers"
}

variable "org_editors_description" {
  type    = string
  default = "Some cool team of terrainers who create terrains from the beginning of computer era."
}

variable "org_editors_privacy" {
  type    = string
  default = "closed"
}
variable "org_editors_permission" {
  type    = string
  default = "push"
}

variable "org_viewers_name" {
  type    = string
  default = "watchers"
}

variable "org_viewers_description" {
  type    = string
  default = "Team of watchers who do nothing but watch"
}

variable "org_viewers_privacy" {
  type    = string
  default = "closed"
}
variable "org_viewers_permission" {
  type    = string
  default = "pull"
}

variable "org_repo_name" {
  type    = string
  default = "terrain"
}

variable "org_repo_description" {
  type    = string
  default = "This is the terrain. Old one."
}

variable "org_repo_visibility" {
  type    = string
  default = "public"
}

variable "org_repo_license" {
  type    = string
  default = "mit"
}

variable "org_repo_default_branch" {
  type    = string
  default = "master"
}