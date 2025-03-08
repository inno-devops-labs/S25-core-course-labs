# Terraform

## 🐋 Docker

### List resources

```shell
terraform state list
```

<details>

**<summary>Output</summary>**

```text
docker_container.app_container
```

</details>

### Show the resource

```shell
terraform state show docker_container.app_container
```

<details>

**<summary>Output</summary>**

```terraform
# docker_container.app_container:
resource "docker_container" "app_container" {
  attach  = false
  bridge  = null
  command = [
    "app.py",
  ]
  container_read_refresh_timeout_milliseconds = 15000
  cpu_set                                     = null
  cpu_shares                                  = 0
  domainname                                  = null
  entrypoint                                  = [
    "python",
  ]
  env             = []
  hostname        = "e7400005ff39"
  id              = "e7400005ff39cda9875145e10933700f14d86b5da5f79717bd9b3404d3ae2543"
  image           = "sha256:7caed087779720215f64b4f6fbc635f6939e146bc61e26ef6554608baa99c6f4"
  init            = false
  ipc_mode        = "private"
  log_driver      = "json-file"
  logs            = false
  max_retry_count = 0
  memory          = 0
  memory_swap     = 0
  must_run        = true
  name            = "moscow-time-app"
  network_data    = [
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
  network_mode      = "default"
  pid_mode          = null
  privileged        = false
  publish_all_ports = false
  read_only         = false
  remove_volumes    = true
  restart           = "no"
  rm                = false
  runtime           = "runc"
  security_opts     = []
  shm_size          = 64
  start             = true
  stdin_open        = false
  stop_signal       = null
  stop_timeout      = 0
  tty               = false
  user              = "appuser"
  userns_mode       = null
  wait              = false
  wait_timeout      = 60
  working_dir       = "/app"

  ports {
    external = 8000
    internal = 5000
    ip       = "0.0.0.0"
    protocol = "tcp"
  }
}
```

</details>

### Applying changes

```shell
terraform apply
```

<details>

**<summary>Output</summary>**

```text
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
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
      + image                                       = "innoenjoyer/moscow-time-app:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "moscow-time-app"
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
          + external = 8000
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
docker_container.app_container: Creation complete after 1s [id=e7400005ff39cda9875145e10933700f14d86b5da5f79717bd9b3404d3ae2543]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

app_container_id = "e7400005ff39cda9875145e10933700f14d86b5da5f79717bd9b3404d3ae2543"
app_container_ports = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

### Read output variables

```shell
terraform output
```

<details>

**<summary>Output</summary>**

```text
app_container_id = "e7400005ff39cda9875145e10933700f14d86b5da5f79717bd9b3404d3ae2543"
app_container_ports = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

## 👾 GitHub

### Import current GitHub repository

```shell
terraform import "github_repository.repo" "S25-core-course-labs"
```

<details>

**<summary>Output</summary>**

```text
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

</details>

### Generate execution plan

```shell
terraform plan -out deploy.tfplan
```

<details>

**<summary>Output</summary>**

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "master"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
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
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "DevOps Engineering Labs"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "S25-core-course-labs"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: deploy.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "deploy.tfplan"
```

</details>

### Applying changes

```shell
terraform apply deploy.tfplan
```

<details>

**<summary>Output</summary>**

```text
github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONw9ncc4DigX-]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

</details>

### ✔️ Best practices
- Structuring of configurations
  - Split logically several files with `main.tf`, `variables.tf`, and `outputs.tf`
- Naming conventions
  - Use underscore instead of dash
  - Use lowercase letters
- Specify version constrains 
- Validating & Formatting .tf files
  - `terraform validate` & `terraform fmt`