# Terraform

## Best practices

1. **Secrets managements**: secrets are stored within environmental variables.
2. **Linting and analyzes**: .tf files are validated and formatted
  via `terraform validate` and `terraform fmt` respectively.
3. **VCS ignore**: .gitignore files hide unnecessary build files from git.

## Docker

* Output for first `terraform apply`:

```bash
Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # docker_container.app_flutter has been deleted
  - resource "docker_container" "app_flutter" {
      - id                                          = "93126484784a0500f33c8dec267ae3978695ea30f3871a0e49f9bbfac07159a3" -> null
        name                                        = "app_flutter"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include actions to undo or respond to
these changes.

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_flutter will be created
  + resource "docker_container" "app_flutter" {
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
      + image                                       = "sha256:723ebf289894da730657d28169d97f9385193a97c88790782a4fcac20725e3e6"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_flutter"
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
          + external = 7070
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.app_piton must be replaced
-/+ resource "docker_container" "app_piton" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python",
          - "-m",
          - "flask",
          - "run",
          - "--host=0.0.0.0",
          - "--port=8080",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "bf0453de625b" -> (known after apply)
      ~ id                                          = "bf0453de625b34eed93e27ee8016f6ecb8137046340d7a2b65d98f64ad6e937d" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_piton"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "appuser" -> null
      - working_dir                                 = "/app" -> null
        # (18 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

      ~ ports {
          ~ external = 6000 -> 6060 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 2 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id_flutter = (known after apply)
  ~ container_id_piton   = "bf0453de625b34eed93e27ee8016f6ecb8137046340d7a2b65d98f64ad6e937d" -> (known after apply)
2025-02-02T23:19:39.951+0300 [DEBUG] command: asking for input: "\nDo you want to perform these actions?"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_piton: Creation complete after 0s [id=46a9a19e2a742b134cdbe380a91cfecf57b427b61b077f4ed479ce05e24c22f5]
Apply complete! Resources: 2 added, 0 changed, 1 destroyed.

Outputs:

container_id_flutter = "69b6a794e1cf43ffdbb2338cccf0eba769ab7db387ef6c3b06fb8aee49866f2b"
container_id_piton = "46a9a19e2a742b134cdbe380a91cfecf57b427b61b077f4ed479ce05e24c22f5"
image_id_flutter = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601paranid5/app_piton:latest"
image_id_piton = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601paranid5/app_piton:latest"
```

* Output for `terraform show`:

```bash
# docker_container.app_flutter:
resource "docker_container" "app_flutter" {
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
    hostname                                    = "69b6a794e1cf"
    id                                          = "69b6a794e1cf43ffdbb2338cccf0eba769ab7db387ef6c3b06fb8aee49866f2b"
    image                                       = "sha256:723ebf289894da730657d28169d97f9385193a97c88790782a4fcac20725e3e6"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_flutter"
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
        external = 7070
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_container.app_piton:
resource "docker_container" "app_piton" {
    attach                                      = false
    bridge                                      = null
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "python",
        "-m",
        "flask",
        "run",
        "--host=0.0.0.0",
        "--port=8080",
    ]
    env                                         = []
    hostname                                    = "46a9a19e2a74"
    id                                          = "46a9a19e2a742b134cdbe380a91cfecf57b427b61b077f4ed479ce05e24c22f5"
    image                                       = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_piton"
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
        external = 6060
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_flutter:
resource "docker_image" "app_flutter" {
    id           = "sha256:723ebf289894da730657d28169d97f9385193a97c88790782a4fcac20725e3e6paranid5/app_flutter:latest"
    image_id     = "sha256:723ebf289894da730657d28169d97f9385193a97c88790782a4fcac20725e3e6"
    keep_locally = false
    name         = "paranid5/app_flutter:latest"
    repo_digest  = "paranid5/app_flutter@sha256:723ebf289894da730657d28169d97f9385193a97c88790782a4fcac20725e3e6"
}

# docker_image.app_piton:
resource "docker_image" "app_piton" {
    id           = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601paranid5/app_piton:latest"
    image_id     = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601"
    keep_locally = false
    name         = "paranid5/app_piton:latest"
    repo_digest  = "paranid5/app_piton@sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601"
}

```

* Output for `terraform state list`:

```bash
docker_container.app_flutter
docker_container.app_piton
docker_image.app_flutter
docker_image.app_piton
```

* Output for `terraform output`:

```bash
container_id_flutter = "69b6a794e1cf43ffdbb2338cccf0eba769ab7db387ef6c3b06fb8aee49866f2b"
container_id_piton = "46a9a19e2a742b134cdbe380a91cfecf57b427b61b077f4ed479ce05e24c22f5"
image_id_flutter = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601paranid5/app_piton:latest"
image_id_piton = "sha256:0d1f8ba8a57b1c812ca9ef6296df5b6a5eec9cbab5244d53698f1ada8b083601paranid5/app_piton:latest"
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