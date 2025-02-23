# Terraform

## Best practices

- **Using variables for secret management**
- **Using `terraform validate` and `terraform fmt` for formatting and checking configs**

## Docker

1. `terraform state list`

```console
docker_container.app_python
docker_container.app_rust
```

2. `terraform state show docker_container.app_python`

```console
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "uvicorn",
        "main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "ea5123370b9e"
    id                                          = "ea5123370b9efc93097f808ae395e295a0e6210b3637d9c2c6d625f50a412fe5"
    image                                       = "sha256:ad0c1b559d7b3ad95010e099d5d1da963d7e06c2563ba7d4be8396cf07b9d37a"
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
    user                                        = "appuser:appgroup"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

3. `terraform state show docker_container.app_rust`

```console
# docker_container.app_rust:
resource "docker_container" "app_rust" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "./app_rust",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "1baa7a19b80a"
    id                                          = "1baa7a19b80ad1934d41d506c686af910051b10dd8f15dc61d828e9d30443957"
    image                                       = "sha256:8eedc48600d29510d478189d50eb99653acdde91476d38ca94d7e7d002e7b7fd"
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
    user                                        = "appuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

4. `terraform apply`

```console
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_python will be created
  + resource "docker_container" "app_python" {
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
      + image                                       = "2imt/app_python:latest"
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
          + external = 8000
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.app_rust will be created
  + resource "docker_container" "app_rust" {
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
      + image                                       = "2imt/app_rust:latest"
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
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id_python    = (known after apply)
  + container_id_rust      = (known after apply)
  + container_image_python = "2imt/app_python:latest"
  + container_image_rust   = "2imt/app_rust:latest"
  + container_name_python  = "app_python"
  + container_name_rust    = "app_rust"
  + container_port_python  = [
      + {
          + external = 8000
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]
  + container_port_rust    = [
      + {
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_rust: Creating...
docker_container.app_python: Creating...
docker_container.app_python: Still creating... [10s elapsed]
docker_container.app_rust: Still creating... [10s elapsed]
docker_container.app_python: Creation complete after 12s [id=ea5123370b9efc93097f808ae395e295a0e6210b3637d9c2c6d625f50a412fe5]
docker_container.app_rust: Creation complete after 12s [id=1baa7a19b80ad1934d41d506c686af910051b10dd8f15dc61d828e9d30443957]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id_python = "ea5123370b9efc93097f808ae395e295a0e6210b3637d9c2c6d625f50a412fe5"
container_id_rust = "1baa7a19b80ad1934d41d506c686af910051b10dd8f15dc61d828e9d30443957"
container_image_python = "2imt/app_python:latest"
container_image_rust = "2imt/app_rust:latest"
container_name_python = "app_python"
container_name_rust = "app_rust"
container_port_python = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_rust = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

5. `terraform output`

```console
container_id_python = "ea5123370b9efc93097f808ae395e295a0e6210b3637d9c2c6d625f50a412fe5"
container_id_rust = "1baa7a19b80ad1934d41d506c686af910051b10dd8f15dc61d828e9d30443957"
container_image_python = "2imt/app_python:latest"
container_image_rust = "2imt/app_rust:latest"
container_name_python = "app_python"
container_name_rust = "app_rust"
container_port_python = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_rust = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud

There are no Free Tier options for virtual machines in Yandex Cloud.

The `.tf` files for Yandex Cloud are implemented using tutorials but are not tested as it was not possible.

## Github

1. `terraform import github_repository.repo S25-core-course-labs`

```console
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

2. `terraform apply`

```console
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
      + description                 = "DevOps Engineering Labs"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (31 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONvxQzs4Diek3]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## GitHub teams

Link: <https://github.com/2imt-inno-devops-course>

1. `terraform apply`

```console
github_team.contributors: Refreshing state... [id=12122565]
github_team.maintainers: Refreshing state... [id=12122566]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main_branch will be created
  + resource "github_branch_default" "main_branch" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "2imt-inno-devops-course"
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

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "2imt-inno-devops-course"
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
      + name                        = "2imt-inno-devops-course"
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

  # github_team_repository.contributors will be created
  + resource "github_team_repository" "contributors" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "2imt-inno-devops-course"
      + team_id    = "12122565"
    }

  # github_team_repository.maintainers will be created
  + resource "github_team_repository" "maintainers" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "2imt-inno-devops-course"
      + team_id    = "12122566"
    }

Plan: 5 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Creating...
github_repository.repo: Creation complete after 6s [id=2imt-inno-devops-course]
github_team_repository.maintainers: Creating...
github_branch_default.main_branch: Creating...
github_team_repository.contributors: Creating...
github_branch_protection.repo_protection: Creating...
github_team_repository.maintainers: Creation complete after 5s [id=12122566:2imt-inno-devops-course]
github_branch_default.main_branch: Creation complete after 6s [id=2imt-inno-devops-course]
github_team_repository.contributors: Creation complete after 6s [id=12122565:2imt-inno-devops-course]
github_branch_protection.repo_protection: Creation complete after 8s [id=BPR_kwDON07t4c4Dier5]

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```
