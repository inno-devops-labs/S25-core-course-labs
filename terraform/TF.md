# Applied Best Practices

* **Use `.gitignore` for terraform files**: it is bad practice to include `.terraform` folder with its lock and also
  `terraform.tfstate`.

* **Use `terraform fmt`**: ensures that configs are formatted properly.

* **Use `terraform plan`**: it allows to analyze the future state before applying new changes.

* **Configure `outputs.tf`**: it is useful for automation.

* **Configure `variables.tf`**: it is always bad practice to hardcode values that can be configured, because
  configuration provides more flexibility.

* **Use `sensitive = true` property at sensitive information like tokens:** it prevents displaying of such data in
  outputs or logs, enhancing security.

# `Docker`

## `terraform init`:

```
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

## `terraform apply`:

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.time_app_py will be created
  + resource "docker_container" "time_app_py" {
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
      + image                                       = "unileonid/time-app-py"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "unileonid_time_app_py"
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
          + external = 80
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + time_app_py_container_id    = (known after apply)
  + time_app_py_container_image = "unileonid/time-app-py"
  + time_app_py_container_name  = "unileonid_time_app_py"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.time_app_py: Creating...
docker_container.time_app_py: Creation complete after 0s [id=cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

time_app_py_container_id = "cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd"
time_app_py_container_image = "unileonid/time-app-py"
time_app_py_container_name = "unileonid_time_app_py"
```

## `terraform state list`:

```
docker_container.time_app_py
```

## `terraform state show "docker_container.time_app_py"`:

```
# docker_container.time_app_py:
resource "docker_container" "time_app_py" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "sh",
        "-c",
        "python app_start.py -t \"${APP_TIMEZONE}\"",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "dc821dbcc3df"
    id                                          = "dc821dbcc3dfd4a74a7e9ef1a0e5b2c93fdecc2b676676aeb17c7cb424eff66f"
    image                                       = "sha256:cb7e6d9ad19509ad71a2d03e0c37d531308f8d5db277e4409c14477c128c7574"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "unileonid_time_app_py"
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
    user                                        = "app"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 80
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## `terraform output`:

```
time_app_py_container_id = "cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd"
time_app_py_container_image = "unileonid/time-app-py"
time_app_py_container_name = "unileonid_time_app_py"
```

# `Yandex.Cloud`

## To complete this task:

1. I register at Yandex.Cloud, create new cloud and service account in it
2. Connect service account at CLI
3. Get familiar with config for Yandex.Cloud
4. Configure network, subnet and virtual machine

## Encountered challenges:

1. There was some problems with service accounts due to permission problems
2. It took me a long time to find how to properly configure network and subnet

## `terraform init`:

```
Initializing the backend...
Initializing provider plugins...
- Finding latest version of yandex-cloud/yandex...
- Installing yandex-cloud/yandex v0.136.0...
- Installed yandex-cloud/yandex v0.136.0 (self-signed, key ID E40F590B50BB8E40)
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

## `terraform apply`:

```
var.cloud_id
  Cloud ID in Yandex.Cloud

  Enter a value:


var.folder_id
  Foder ID in Yandex.Cloud

  Enter a value:


var.iam_token
  IAM token in Yandex Cloud

  Enter a value:



Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
      + name                      = "terraform-1"
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
              + image_id    = "fd8bpal18cm4kprpjc2m"
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
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "default"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enphatt0r4mu1pu91pr9]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2lgu1146mc76h665kit]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 35s [id=epd705hur0ap18v01qk7]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

# `GitHub`

I have faced with many problems when trying to
configure [UniLeonid/S25-core-course-labs](https://github.com/UniLeonid/S25-core-course-labs) repository, so I
configured [S25-core-course-labs-terraform](http://github.com/UniLeonid/S25-core-course-labs-terraform) instead of it.

## `terraform init`:

```
Initializing the backend...
Initializing provider plugins...
- Finding integrations/github versions matching "~> 6.0"...
- Installing integrations/github v6.5.0...
- Installed integrations/github v6.5.0 (signed by a HashiCorp partner, key ID 38027F80D7FD5FB2)
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

## `terraform apply`:

```
var.github_token
  Personal access token for GitHub

  Enter a value:



Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch.main will be created
  + resource "github_branch" "main" {
      + branch        = "main"
      + etag          = (known after apply)
      + id            = (known after apply)
      + ref           = (known after apply)
      + repository    = "S25-core-course-labs-terraform"
      + sha           = (known after apply)
      + source_branch = "main"
      + source_sha    = (known after apply)
    }

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "S25-core-course-labs-terraform"
    }

  # github_branch_protection.core_repo will be created
  + resource "github_branch_protection" "core_repo" {
      + allows_deletions                = true
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

  # github_repository.core_repo will be created
  + resource "github_repository" "core_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "such dirty legend like"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "S25-core-course-labs-terraform"
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

Plan: 4 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.core_repo: Creating...
github_repository.core_repo: Creation complete after 5s [id=S25-core-course-labs-terraform]
github_branch.main: Creating...
github_branch.main: Creation complete after 2s [id=S25-core-course-labs-terraform:main]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=S25-core-course-labs-terraform]
github_branch_protection.core_repo: Creating...
github_branch_protection.core_repo: Creation complete after 4s [id=BPR_kwDON1Atuc4Difxv]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```
