# TF.md

## Docker

I followed all the instructions by terraform to launch my app, and I've done it. Web-app is launching with no errors via this method.

### `terraform state list`

<details>
<summary>State list</summary>

```cmd
terraform state list
docker_container.flask_app_container
```

</details>

### `terraform state show`

<details>
<summary>State of <code>flask_app_container</code></summary>

```cmd
terraform state show docker_container.flask_app_container
# docker_container.flask_app_container:
resource "docker_container" "flask_app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "f4aa116f5aa8"
    id                                          = "f4aa116f5aa88acc6ade61f244ef8e0cb02f13d4fcd79af18a421a7048a468fc"
    image                                       = "sha256:c4b78c415a558b0fe5acc51adfdf486c86e5434bea6b5636424a4a7e7f052c43"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "flask-app"
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
    user                                        = "nonrootuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
</details>

### `terraform apply`

<details>
<summary>Applied terraform</summary>

```cmd
terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.flask_app_container will be created
  + resource "docker_container" "flask_app_container" {
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
      + image                                       = "synavtora/flask-app:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "flask-app"
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
  + flask_app_container_id_output    = (known after apply)
  + flask_app_container_ports_output = [
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

docker_container.flask_app_container: Creating...
docker_container.flask_app_container: Creation complete after 1s [id=f4aa116f5aa88acc6ade61f244ef8e0cb02f13d4fcd79af18a421a7048a468fc]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

flask_app_container_id_output = "f4aa116f5aa88acc6ade61f244ef8e0cb02f13d4fcd79af18a421a7048a468fc"
flask_app_container_ports_output = tolist([
  {
    "external" = 5000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

### `terraform output`

<details>
<summary>Returned output</summary>

```cmd
terraform output
flask_app_container_id_output = "f4aa116f5aa88acc6ade61f244ef8e0cb02f13d4fcd79af18a421a7048a468fc"
flask_app_container_ports_output = tolist([
  {
    "external" = 5000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

## Yandex Cloud

The instruction provided by YC was terrible. The interface of console is completely not user friendly even if you follow the instuctions directly. As a result, I have got not working terraform and I've got no idea what went wrong.

### `terraform plan`

<details>
<summary>Resources planning</summary>

```cmd
terraform plan
data.template_file.default: Reading...
data.template_file.default: Read complete after 0s [id=15dfa216f2841afebc169c5ec07cee08743a0edde1461fc2f37d35c864f59e8e]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.disk-1 will be created
  + resource "yandex_compute_disk" "disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fv4keno1d1omjp0bgq5q"
      + name        = "disk-1"
      + product_ids = (known after apply)
      + size        = 50
      + status      = (known after apply)
      + type        = "network-nvme"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.default will be created
  + resource "yandex_compute_instance" "default" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = "<my_server_name>"
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #ps1
                # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

                # logging
                Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
                "Bootstrap script started" | Write-Host

                # inserting value's from terraform
                $MyUserName = "<my_user>"
                $MyPlainTextPassword = "<my_password>"
                if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
                    "Create user" | Write-Host
                    $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                    $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
                    $MyUser | Add-LocalGroupMember -Group 'Administrators'
                    $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
                }

                # inserting value's from terraform
                $MyAdministratorPlainTextPassword = "<my_password>"
                if (-not [string]::IsNullOrEmpty($MyAdministratorPlainTextPassword)) {
                    "Set local administrator password" | Write-Host
                    $MyAdministratorPassword = $MyAdministratorPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                    # S-1-5-21domain-500 is a well-known SID for Administrator
                    # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
                    $MyAdministrator = Get-LocalUser | Where-Object -Property "SID" -like "S-1-5-21-*-500"
                    $MyAdministrator | Set-LocalUser -Password $MyAdministratorPassword
                }

                "Bootstrap script ended" | Write-Host
            EOT
        }
      + name                      = "<my_server_name>"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-d"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = (known after apply)
              + name        = (known after apply)
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
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
          + memory        = 4
        }

      + scheduling_policy (known after apply)

      + timeouts {
          + create = "10m"
          + delete = "10m"
        }
    }

  # yandex_vpc_network.default will be created
  + resource "yandex_vpc_network" "default" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "ya-network"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.default will be created
  + resource "yandex_vpc_subnet" "default" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "ya-network"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-d"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + address = (known after apply)
  + name    = "<my_server_name>"

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

</details>

### `terraform apply`

<details>
<summary>Applied terraform</summary>

```cmd
terraform apply
data.template_file.default: Reading...
data.template_file.default: Read complete after 0s [id=15dfa216f2841afebc169c5ec07cee08743a0edde1461fc2f37d35c864f59e8e]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.disk-1 will be created
  + resource "yandex_compute_disk" "disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fv4keno1d1omjp0bgq5q"
      + name        = "disk-ubuntu-24-04-lts-1739271629844"
      + product_ids = (known after apply)
      + size        = 50
      + status      = (known after apply)
      + type        = "network-nvme"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.default will be created
  + resource "yandex_compute_instance" "default" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = "<my_server_name>"
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #ps1
                # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

                # logging
                Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
                "Bootstrap script started" | Write-Host

                # inserting value's from terraform
                $MyUserName = "<my_user>"
                $MyPlainTextPassword = "<my_password>"
                if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
                    "Create user" | Write-Host
                    $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                    $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
                    $MyUser | Add-LocalGroupMember -Group 'Administrators'
                    $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
                }

                # inserting value's from terraform
                $MyAdministratorPlainTextPassword = "<my_password>"
                if (-not [string]::IsNullOrEmpty($MyAdministratorPlainTextPassword)) {
                    "Set local administrator password" | Write-Host
                    $MyAdministratorPassword = $MyAdministratorPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                    # S-1-5-21domain-500 is a well-known SID for Administrator
                    # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
                    $MyAdministrator = Get-LocalUser | Where-Object -Property "SID" -like "S-1-5-21-*-500"
                    $MyAdministrator | Set-LocalUser -Password $MyAdministratorPassword
                }

                "Bootstrap script ended" | Write-Host
            EOT
        }
      + name                      = "<my_server_name>"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-d"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = (known after apply)
              + name        = (known after apply)
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
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
          + memory        = 4
        }

      + scheduling_policy (known after apply)

      + timeouts {
          + create = "10m"
          + delete = "10m"
        }
    }

  # yandex_vpc_network.default will be created
  + resource "yandex_vpc_network" "default" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.default will be created
  + resource "yandex_vpc_subnet" "default" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "default-ru-central1-d"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-d"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + address = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.default: Creating...
yandex_compute_disk.disk-1: Creating...
╷
│ Error: Error while requesting API to create network: server-request-id = baebfc0d-3a30-4d38-afed-25fde2df3aab server-trace-id = 95b689ad25185c09:107120895efd8a8f:95b689ad25185c09:1 client-request-id = 36e0e8b5-1375-4438-b05b-ff63eacf2756 client-trace-id = cc875058-0476-42ba-8c7c-49000cdc3ea4 rpc error: code = PermissionDenied desc = Operation is not permitted in the folder
│
│   with yandex_vpc_network.default,
│   on main.tf line 13, in resource "yandex_vpc_network" "default":
│   13: resource "yandex_vpc_network" "default" {
│
╵
╷
│ Error: Error while requesting API to create disk: server-request-id = 027d54f5-3c55-4542-ab73-8ea2f8a9517c server-trace-id = 24788949cb4ebc98:75581d0233d042c6:24788949cb4ebc98:1 client-request-id = e80f2a79-0374-426a-a57a-da5193bfb478 client-trace-id = cc875058-0476-42ba-8c7c-49000cdc3ea4 rpc error: code = FailedPrecondition desc = Image "fv4keno1d1omjp0bgq5q" not found
│
│   with yandex_compute_disk.disk-1,
│   on main.tf line 24, in resource "yandex_compute_disk" "disk-1":
│   24: resource "yandex_compute_disk" "disk-1" {
│
╵
```

</details>

### `terraform output`
I got no output because terraform apply caused errors.

## Github

### `terraform import`

<details>
<summary>Importing repo</summary>

```cmd
terraform import github_repository.s25_repo S25-core-course-labs
github_repository.s25_repo: Importing from ID "S25-core-course-labs"...
github_repository.s25_repo: Import prepared!
  Prepared github_repository for import
github_repository.s25_repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

</details>

### `terraform plan`

<details>
<summary>Planned terraform resources</summary>

```cmd
D:\terraform\terraform\github>terraform plan -out deploy.tfplan
github_repository.s25_repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
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
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: deploy.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "deploy.tfplan"
```

</details>

### `terraform apply`

<details>
<summary>Applied terraform</summary>

```cmd
terraform apply deploy.tfplan
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONwHA_84DjLsf]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

</details>
