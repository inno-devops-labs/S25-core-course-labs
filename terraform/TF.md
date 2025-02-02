# Terraform

## Docker

* Output for first `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
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
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "nginx-container"
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
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Creation complete after 19s [id=sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206anginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=6e69126b0d6ae0356ecaf17a5b7cf36b2bfc7c2401fe2cd0c6ad86fb2d283129]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
(.venv) paranid5@paranid5s-MacBook-Pro terraform % terraform fmt
(.venv) paranid5@paranid5s-MacBook-Pro terraform % terraform validate
Success! The configuration is valid.
```

* Output for `terraform show`:

```bash
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "557a961142e0"
    id                                          = "557a961142e00c30f9e8fd3949d3b208da10bdbe7b53345c3d045ef56c38276a"
    image                                       = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "nginx-container"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4nginx:1.27.3-alpine"
    image_id     = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4"
    keep_locally = false
    name         = "nginx:1.27.3-alpine"
    repo_digest  = "nginx@sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4"
}
```

* Output for `terraform state list`:

```bash
docker_container.nginx
docker_image.nginx
```

* Output for final `terraform apply`:

```bash
docker_image.nginx: Refreshing state... [id=sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4nginx:1.27.3-alpine]
docker_container.nginx: Refreshing state... [id=50a2ce5e76513bbed81d5c0cf7ac9e93bfc302fdf51dda3c9bf5fc54225f7d40]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "50a2ce5e7651" -> (known after apply)
      ~ id                                          = "50a2ce5e76513bbed81d5c0cf7ac9e93bfc302fdf51dda3c9bf5fc54225f7d40" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "nginx-container"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - working_dir                                 = "/" -> null
        # (19 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4nginx:1.27.3-alpine"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=50a2ce5e76513bbed81d5c0cf7ac9e93bfc302fdf51dda3c9bf5fc54225f7d40]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=beb4eabfb164891f71ba172816eae503ac6a193838e40a16fbe7fb95720efbc2]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "beb4eabfb164891f71ba172816eae503ac6a193838e40a16fbe7fb95720efbc2"
image_id = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4nginx:1.27.3-alpine"
```

* Output for `terraform output`:

```bash
container_id = "beb4eabfb164891f71ba172816eae503ac6a193838e40a16fbe7fb95720efbc2"
image_id = "sha256:814a8e88df978ade80e584cc5b333144b9372a8e3c98872d07137dbf3b44d0e4nginx:1.27.3-alpine"
```

## GitHub

### Single

* Output for `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_protection.master_branch_protection will be created
  + resource "github_branch_protection" "master_branch_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "master"
      + repository_id                   = "R_kgDONvYleA"
      + require_conversation_resolution = false
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + dismiss_stale_reviews           = true
          + require_code_owner_reviews      = true
          + required_approving_review_count = 1
        }

      + required_status_checks {
          + contexts = [
              + "ci",
            ]
          + strict   = true
        }
    }

  # github_repository.devops will be updated in-place
  ~ resource "github_repository" "devops" {
      ~ allow_merge_commit          = true -> false
      ~ auto_init                   = false -> true
      ~ delete_branch_on_merge      = false -> true
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "devops"
        name                        = "devops"
        # (27 unchanged attributes hidden)
    }

Plan: 1 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.devops: Modifying... [id=devops]
github_repository.devops: Modifications complete after 3s [id=devops]
github_branch_protection.master_branch_protection: Creating...
github_branch_protection.master_branch_protection: Creation complete after 3s [id=BPR_kwDONvYleM4DiBGe]

Apply complete! Resources: 1 added, 1 changed, 0 destroyed.
```

### Teams

Created repository for teams: https://github.com/paranid5-devops/devops

* Output for `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team_repository.developers_push_access will be created
  + resource "github_team_repository" "developers_push_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops"
      + team_id    = "12091360"
    }

  # github_team_repository.qa_pull_access will be created
  + resource "github_team_repository" "qa_pull_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "devops"
      + team_id    = "12091359"
    }

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```