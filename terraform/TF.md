# Terraform overview

## Best practices applied

- Using parameters in variables.tf, like sensitive, etc.
- .gitignore unnecessary terraform files
- Usage of terraform validate, terraform fmt

## Docker infra

### Command outputs

First, lets learn what components we have:

```bash
terraform state list
```

```bash
docker_container.custom_container_go
docker_container.custom_container_python
```

```bash
terraform state show docker_container.custom_container_python
```

```bash
# docker_container.custom_container_python:
resource "docker_container" "custom_container_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python3",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "03aeef20f52d"
    id                                          = "03aeef20f52dff433a0a7f622646f7dfbf2f899473293b49fa691e74ec8c3b29"
    image                                       = "sha256:05c124b3e087fcd32a9d348dfb2055b40bcd550b8b6389e22f94f15cafdde25f"
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
    user                                        = "service"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/service"

    ports {
        external = 8079
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```bash
terraform state show docker_container.custom_container_go
```

```bash
# docker_container.custom_container_go:
resource "docker_container" "custom_container_go" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "/app/service",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e2b6878666f0"
    id                                          = "e2b6878666f0816428b846d98d19e947cf4f241b35bae5619534e4907df4325c"
    image                                       = "sha256:fca0f9a76b1039f4f404d7358c4eaa4887ac948e8c3e1907dc9d924a32a51600"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_go"
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
        external = 7999
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```bash
terraform output
```

```bash
container_id_go = "e2b6878666f0816428b846d98d19e947cf4f241b35bae5619534e4907df4325c"
container_id_python = "03aeef20f52dff433a0a7f622646f7dfbf2f899473293b49fa691e74ec8c3b29"
container_image_go = "elonmaxx/app_go"
container_image_python = "elonmaxx/app_python"
container_name_go = "app_go"
container_name_python = "app_python"
container_port_go = tolist([
  {
    "external" = 7999
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_python = tolist([
  {
    "external" = 8079
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud infra

```bash
terraform state list
```

```bash
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```bash
terraform apply
```

```bash
yandex_vpc_network.network-1: Refreshing state... [id=enpaubk0a315e28aqsld]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "terraform-vm"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd83s8u085j3mq231ago"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
        }

      + metadata_options (known after apply)

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "Subnet1"
      + network_id     = "enpaubk0a315e28aqsld"
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 2s [id=e2lqpt51k6mvleu3e9ue]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [50s elapsed]
yandex_compute_instance.vm-1: Creation complete after 55s [id=epdnl0qc3tbs9bkft7ea]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

After that, we may simply `ssh` into the server:

```bash
ssh -l ubuntu 158.160.7.175

The authenticity of host '158.160.7.175 (158.160.7.175)' can't be established.
ED25519 key fingerprint is SHA256:A/navun3PWZmy2RDWI5XjAxfyN5oklVH/KpkCA4LKjM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '158.160.7.175' (ED25519) to the list of known hosts.

Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-92-generic x86_64)
```

## Github repo creation

Following the tutorial, a repository was issued automaticaly: `https://github.com/Processor228/devops-test`

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-test"
    }

  # github_branch_protection.repo_main will be created
  + resource "github_branch_protection" "repo_main" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
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
      + description                 = "DevOps test repository"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-test"
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

Plan: 3 to add, 0 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: deploy.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "deploy.tfplan"
github_repository.repo: Creating...
github_repository.repo: Creation complete after 6s [id=devops-test]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=devops-test]
github_branch_protection.repo_main: Creating...
github_branch_protection.repo_main: Creation complete after 5s [id=BPR_kwDON1JhZs4DiixB]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

Then, I've decided to change my own repo, and added my own repo in the `main.tf`, then used `terraform import`, and `terraform apply`, getting

```bash
github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]
github_repository.repo: Refreshing state... [id=devops-test]
github_branch_default.main: Refreshing state... [id=devops-test]
github_branch_protection.repo_main: Refreshing state... [id=BPR_kwDON1JhZs4DiixB]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_protection.repo_main_of_real_repo will be created
  + resource "github_branch_protection" "repo_main_of_real_repo" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_protection.repo_main_of_real_repo: Creating...
github_branch_protection.repo_main_of_real_repo: Creation complete after 5s [id=BPR_kwDONulVIc4Dii4D]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

## Github teams setup

First, I created `https://github.com/Smack-org` - my organization.

Then, run `terraform init` and `terraform apply`:

```bash
var.github_pat
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Refreshing state... [id=devops-test-team-repo]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may
have affected this plan:

  # github_repository.repo has been deleted
  - resource "github_repository" "repo" {
      - id                          = "devops-test-team-repo" -> null
      - name                        = "devops-test-team-repo" -> null
        # (18 unchanged attributes hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using
ignore_changes, the following plan may include actions to undo or respond to these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.repo_main will be created
  + resource "github_branch_default" "repo_main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-test-team-repo"
    }

  # github_branch_protection.repo_protection will be created
  + resource "github_branch_protection" "repo_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
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
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-test-team-repo"
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
        # (1 unchanged attribute hidden)

      + security_and_analysis (known after apply)
    }

  # github_team.developers will be created
  + resource "github_team" "developers" {
      + create_default_maintainer = false
      + description               = "The team that always does everything on the verge of deadline"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Development Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.devops will be created
  + resource "github_team" "devops" {
      + create_default_maintainer = false
      + description               = "The team that manages on time"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "DevOps Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.developers_repo will be created
  + resource "github_team_repository" "developers_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-test-team-repo"
      + team_id    = (known after apply)
    }

  # github_team_repository.devops_repo will be created
  + resource "github_team_repository" "devops_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-test-team-repo"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.developers: Creating...
github_team.devops: Creating...
github_repository.repo: Creating...
github_team.developers: Still creating... [10s elapsed]
github_team.devops: Still creating... [10s elapsed]
github_repository.repo: Still creating... [10s elapsed]
github_team.devops: Creation complete after 12s [id=12126067]
github_team.developers: Creation complete after 14s [id=12126066]
github_repository.repo: Creation complete after 15s [id=devops-test-team-repo]
github_team_repository.developers_repo: Creating...
github_team_repository.devops_repo: Creating...
github_branch_default.repo_main: Creating...
github_team_repository.devops_repo: Creation complete after 1s [id=12126067:devops-test-team-repo]
github_team_repository.developers_repo: Creation complete after 5s [id=12126066:devops-test-team-repo]
github_branch_default.repo_main: Creation complete after 6s [id=devops-test-team-repo]
github_branch_protection.repo_protection: Creating...
github_branch_protection.repo_protection: Creation complete after 4s [id=BPR_kwDON1KeM84Dii7I]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```
