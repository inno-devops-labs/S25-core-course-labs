# Terraform

## Docker

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (self-signed, key ID BD080C4571C6104C)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_container will be created
  + resource "docker_container" "app_container" {
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
      + image                                       = "darrpyy/app_python:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + app_container_id    = (known after apply)
  + app_container_ports = [
      + {
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform
apply" now.
```

```
terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_container will be created
  + resource "docker_container" "app_container" {
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
      + image                                       = "darrpyy/app_python:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + app_container_id    = (known after apply)
  + app_container_ports = [
      + {
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_container: Creating...
docker_container.app_container: Still creating... [10s elapsed]
docker_container.app_container: Creation complete after 16s [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

app_container_id = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a"
app_container_ports = tolist([
  {
    "external" = 5000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

```
docker ps
CONTAINER ID   IMAGE                       COMMAND            CREATED          STATUS          PORTS                    NAMES
7541fccc95e2   darrpyy/app_python:latest   "python main.py"   36 seconds ago   Up 35 seconds   0.0.0.0:5000->5000/tcp   app
```

```
terraform destroy
docker_container.app_container: Refreshing state... [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # docker_container.app_container will be destroyed
  - resource "docker_container" "app_container" {
      - attach                                      = false -> null
      - command                                     = [] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      - entrypoint                                  = [
          - "python",
          - "main.py",
        ] -> null
      - env                                         = [] -> null
      - group_add                                   = [] -> null
      - hostname                                    = "7541fccc95e2" -> null
      - id                                          = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a" -> null
      - image                                       = "sha256:af78391c56a05c0e85dcf9e98fa9527b8969fa101fe6334f90fd4ca41b0bcd66" -> null
      - init                                        = false -> null
      - ipc_mode                                    = "private" -> null
      - log_driver                                  = "json-file" -> null
      - log_opts                                    = {} -> null
      - logs                                        = false -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      - must_run                                    = true -> null
      - name                                        = "app" -> null
      - network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - network_mode                                = "bridge" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      - read_only                                   = false -> null
      - remove_volumes                              = true -> null
      - restart                                     = "no" -> null
      - rm                                          = false -> null
      - runtime                                     = "runc" -> null
      - security_opts                               = [] -> null
      - shm_size                                    = 64 -> null
      - start                                       = true -> null
      - stdin_open                                  = false -> null
      - stop_timeout                                = 0 -> null
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - tty                                         = false -> null
      - user                                        = "appuser" -> null
      - wait                                        = false -> null
      - wait_timeout                                = 60 -> null
      - working_dir                                 = "/code" -> null
        # (6 unchanged attributes hidden)

      - ports {
          - external = 5000 -> null
          - internal = 5000 -> null
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null
        }
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  - app_container_id    = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a" -> null
  - app_container_ports = [
      - {
          - external = 5000
          - internal = 5000
          - ip       = "0.0.0.0"
          - protocol = "tcp"
        },
    ] -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

docker_container.app_container: Destroying... [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]
docker_container.app_container: Destruction complete after 0s

Destroy complete! Resources: 1 destroyed.
```

```
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Yandex Cloud



## GitHub

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding integrations/github versions matching "~> 4.0"...
- Installing integrations/github v4.31.0...
- Installed integrations/github v4.31.0 (signed by a HashiCorp partner, key ID 38027F80D7FD5FB2)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
terraform import "github_repository.repository" "S25-core-course-labs"
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Importing from ID "S25-core-course-labs"...
github_repository.repository: Import prepared!
  Prepared github_repository for import
github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be created
  + resource "github_branch_protection" "default_branch_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.repository will be updated in-place
  ~ resource "github_repository" "repository" {
      + description                 = "Repository for the S25 core course labs"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repository: Modifying... [id=S25-core-course-labs]
github_repository.repository: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.default_branch: Creating...
github_branch_protection.default_branch_protection: Creating...
github_branch_protection.default_branch_protection: Creation complete after 6s [id=BPR_kwDONxWB-84Dkwxc]
╷
│ Error: PATCH https://api.github.com/repos/darrpyy/S25-core-course-labs: 422 Validation Failed [{Resource:Repository Field:default_branch Code:invalid Message:The branch main was not found. Please push that ref first or create it via the Git Data API.}]
│ 
│   with github_branch_default.default_branch,
│   on main.tf line 20, in resource "github_branch_default" "default_branch":
│   20: resource "github_branch_default" "default_branch" {
│ 
╵
```

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Refreshing state... [id=BPR_kwDONxWB-84Dkwxc]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be updated in-place
  ~ resource "github_branch_protection" "default_branch_protection" {
        id                              = "BPR_kwDONxWB-84Dkwxc"
      ~ pattern                         = "main" -> "master"
        # (9 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.default_branch: Creating...
github_branch_protection.default_branch_protection: Modifying... [id=BPR_kwDONxWB-84Dkwxc]
github_branch_default.default_branch: Creation complete after 3s [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Modifications complete after 7s [id=BPR_kwDONxWB-84Dkwxc]

Apply complete! Resources: 1 added, 1 changed, 0 destroyed.
```

```
terraform destroy
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]
github_branch_default.default_branch: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Refreshing state... [id=BPR_kwDONxWB-84Dkwxc]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # github_branch_default.default_branch will be destroyed
  - resource "github_branch_default" "default_branch" {
      - branch     = "master" -> null
      - id         = "S25-core-course-labs" -> null
      - repository = "S25-core-course-labs" -> null
    }

  # github_branch_protection.default_branch_protection will be destroyed
  - resource "github_branch_protection" "default_branch_protection" {
      - allows_deletions                = false -> null
      - allows_force_pushes             = false -> null
      - blocks_creations                = false -> null
      - enforce_admins                  = true -> null
      - id                              = "BPR_kwDONxWB-84Dkwxc" -> null
      - pattern                         = "master" -> null
      - push_restrictions               = [] -> null
      - repository_id                   = "S25-core-course-labs" -> null
      - require_conversation_resolution = true -> null
      - require_signed_commits          = false -> null
      - required_linear_history         = false -> null

      - required_pull_request_reviews {
          - dismiss_stale_reviews           = false -> null
          - dismissal_restrictions          = [] -> null
          - pull_request_bypassers          = [] -> null
          - require_code_owner_reviews      = false -> null
          - required_approving_review_count = 1 -> null
          - restrict_dismissals             = false -> null
        }
    }

  # github_repository.repository will be destroyed
  - resource "github_repository" "repository" {
      - allow_auto_merge            = false -> null
      - allow_merge_commit          = true -> null
      - allow_rebase_merge          = true -> null
      - allow_squash_merge          = true -> null
      - archived                    = false -> null
      - auto_init                   = false -> null
      - branches                    = [
          - {
              - name      = "lab1"
              - protected = false
            },
          - {
              - name      = "lab2"
              - protected = false
            },
          - {
              - name      = "lab3"
              - protected = false
            },
          - {
              - name      = "lab4"
              - protected = false
            },
          - {
              - name      = "master"
              - protected = false
            },
        ] -> null
      - default_branch              = "master" -> null
      - delete_branch_on_merge      = false -> null
      - description                 = "Repository for the S25 core course labs" -> null
      - etag                        = "W/\"c3728206ce2eaad86737a82536de6306e2f0bf9aea3626bdd4f4543a35b0c3d0\"" -> null
      - full_name                   = "darrpyy/S25-core-course-labs" -> null
      - git_clone_url               = "git://github.com/darrpyy/S25-core-course-labs.git" -> null
      - has_downloads               = false -> null
      - has_issues                  = false -> null
      - has_projects                = false -> null
      - has_wiki                    = false -> null
      - html_url                    = "https://github.com/darrpyy/S25-core-course-labs" -> null
      - http_clone_url              = "https://github.com/darrpyy/S25-core-course-labs.git" -> null
      - id                          = "S25-core-course-labs" -> null
      - is_template                 = false -> null
      - merge_commit_message        = "PR_TITLE" -> null
      - merge_commit_title          = "MERGE_MESSAGE" -> null
      - name                        = "S25-core-course-labs" -> null
      - node_id                     = "R_kgDONxWB-w" -> null
      - private                     = false -> null
      - repo_id                     = 924156411 -> null
      - squash_merge_commit_message = "COMMIT_MESSAGES" -> null
      - squash_merge_commit_title   = "COMMIT_OR_PR_TITLE" -> null
      - ssh_clone_url               = "git@github.com:darrpyy/S25-core-course-labs.git" -> null
      - svn_url                     = "https://github.com/darrpyy/S25-core-course-labs" -> null
      - topics                      = [] -> null
      - visibility                  = "public" -> null
      - vulnerability_alerts        = false -> null
        # (1 unchanged attribute hidden)
    }

Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

github_branch_default.default_branch: Destroying... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Destroying... [id=BPR_kwDONxWB-84Dkwxc]
github_branch_default.default_branch: Destruction complete after 1s
github_branch_protection.default_branch_protection: Destruction complete after 2s
github_repository.repository: Destroying... [id=S25-core-course-labs]
github_repository.repository: Destruction complete after 2s

Destroy complete! Resources: 3 destroyed.
```
