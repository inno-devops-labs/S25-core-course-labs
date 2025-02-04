# Terraform

## Best practices

- Use variables for hiding secrets.
- Use separate `.gitignore` for Terraform.
- Use `terraform validate` and `terraform fmt` for well-written HCL code.

## Docker

1. List: `terraform state list`

```bash
~ terraform state list
docker_container.moscow_time_python
docker_container.moscow_time_rust
```

2. For python application: `terraform state show docker_container.moscow_time_python`

```bash
~ terraform state show docker_container.moscow_time_python
# docker_container.moscow_time_python:
resource "docker_container" "moscow_time_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "--bind",
        "0.0.0.0:8000",
        "app:wsgi_app",
        "--chdir",
        "app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "gunicorn",
    ]
    env                                         = []
    hostname                                    = "de18b54d1e70"
    id                                          = "de18b54d1e707f1cffa6d1a7dfe957c5fc985954b6efef1d641fd091f341224d"
    image                                       = "sha256:f210f39f86106d747a9b12923c93fb0520e5d13a0508a1bfa07de894a58c0db4"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:03"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = null
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "python_usr"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

3. For Rust application: `terraform state show docker_container.moscow_time_rust`

```bash
~ terraform state show docker_container.moscow_time_rust
# docker_container.moscow_time_rust:
resource "docker_container" "moscow_time_rust" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "./app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "49ee41abdc39"
    id                                          = "49ee41abdc3925871e8f42fb6ad842954b68bc14c057a266f2f261e1e05012e8"
    image                                       = "sha256:fe3e72229651406fcf6c6b5e779450854afd69c9ae08b82a3711b8d3f0961d68"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_rust"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = null
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "appuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 8081
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

4. Apply changes: `terraform apply`

```bash
~ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.moscow_time_python will be created
  + resource "docker_container" "moscow_time_python" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = "raleksan/app_python:v0.1"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_python"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.moscow_time_rust will be created
  + resource "docker_container" "moscow_time_rust" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = "raleksan/app_rust:v0.1"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_rust"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 8081
          + internal = 8081
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id_python    = (known after apply)
  + container_id_rust      = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.moscow_time_rust: Creating...
docker_container.moscow_time_python: Creating...
docker_container.moscow_time_rust: Creation complete after 0s [id=b565fd900ae4a781e05f290696771196f5957c21ab21114c11b3ea54e9111367]
docker_container.moscow_time_python: Creation complete after 0s [id=7c2ffed804eb7deda4d35768bf734fe654b54af9ee85614c6b299c2884e820bd]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

5. Show outputs: `terraform output`

```bash
~ terraform output 
container_id_python = "7c2ffed804eb7deda4d35768bf734fe654b54af9ee85614c6b299c2884e820bd"
container_id_rust = "b565fd900ae4a781e05f290696771196f5957c21ab21114c11b3ea54e9111367"
container_image_python = "raleksan/app_python:v0.1"
container_image_rust = "raleksan/app_rust:v0.1"
container_name_python = "app_python"
container_name_rust = "app_rust"
container_port_python = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_rust = tolist([
  {
    "external" = 8081
    "internal" = 8081
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud

I have implemented configuration using manual of Yandex Cloud and examples from Github, but I do not found any opportunity to
get some compute instance in Yandex Cloud without any fee and without connecting bank card.

## Github
0. Prerequisites: import a GitHub access token (fine-grained is better)

```bash
export TF_VAR_token="your_github_personal_access_token"
```

1. Importing repo: `terraform import github_repository.repo S25-core-course-labs`

```bash
~ terraform import github_repository.repo S25-core-course-labs
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

2. Apply changes: `terraform apply`

```bash
~ terraform apply
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (32 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONuj7fc4DiS-8]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

```

## GitHub teams

Link into GitHub team: <https://github.com/Raleksan-devops-teams>

0. Prerequisites: import a GitHub access token (fine-grained is better)

```bash
export TF_VAR_github_token="your_github_personal_access_token"
```

1. Apply changes: `terraform apply`

```bash
~ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main_branch will be created
  + resource "github_branch_default" "main_branch" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-teams-test"
    }

  # github_branch_protection.repo_protection will be created
  + resource "github_branch_protection" "repo_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repository will be created
  + resource "github_repository" "repository" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Collaborative project for test"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = false
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-teams-test"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false

      + security_and_analysis (known after apply)
    }

  # github_team.contributors will be created
  + resource "github_team" "contributors" {
      + create_default_maintainer = false
      + description               = "Well-known open-source contributors"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Project contributors"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.maintainers will be created
  + resource "github_team" "maintainers" {
      + create_default_maintainer = false
      + description               = "Core project developers"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Project maintainers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.contributors will be created
  + resource "github_team_repository" "contributors" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-teams-test"
      + team_id    = (known after apply)
    }

  # github_team_repository.maintainers will be created
  + resource "github_team_repository" "maintainers" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-teams-test"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.contributors: Creating...
github_team.maintainers: Creating...
github_repository.repository: Creating...
github_team.contributors: Still creating... [10s elapsed]
github_team.maintainers: Still creating... [10s elapsed]
github_repository.repository: Still creating... [10s elapsed]
github_team.maintainers: Creation complete after 14s [id=12108696]
github_team.contributors: Creation complete after 15s [id=12108699]
github_repository.repository: Creation complete after 15s [id=devops-teams-test]
github_team_repository.contributors: Creating...
github_team_repository.maintainers: Creating...
github_branch_default.main_branch: Creating...
github_branch_protection.repo_protection: Creating...
github_branch_default.main_branch: Creation complete after 6s [id=devops-teams-test]
github_team_repository.maintainers: Creation complete after 7s [id=12108696:devops-teams-test]
github_team_repository.contributors: Creation complete after 7s [id=12108699:devops-teams-test]
github_branch_protection.repo_protection: Creation complete after 9s [id=BPR_kwDON0QM1M4DiTgk]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

```
