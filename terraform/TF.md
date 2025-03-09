# Infrastructure as Code (IAC) using Terraform

## Best practices

1. Sensitive information is securely stored as environment variables.
2. The terraform directory follows a well-organized structure, with separate folders for docker, yandex, and github configurations.
3. Terraform files are named logically and consistently: main.tf for primary configurations, variables.tf for variable definitions, and outputs.tf for output specifications.
4. As a best practice, terraform fmt and terraform validate commands are always executed prior to terraform apply, ensuring the configuration's formatting and validity before implementation.

## Docker

### terraform show

```plaintext
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
    hostname                                    = "e957d13db6d9"
    id                                          = "e957d13db6d9d74c3b264582686f55f264a085bd78c6d000b185b7ab54d27afd"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my-nginx-container"
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
    network_mode                                = "default"
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
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}


Outputs:

container_id = "e957d13db6d9d74c3b264582686f55f264a085bd78c6d000b185b7ab54d27afd"
container_name = "my-nginx-container"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
image_name = "nginx:latest"
```

### terraform state list

```plaintext
docker_container.nginx
docker_image.nginx
```

### terraform output

```plaintext
container_id = "e957d13db6d9d74c3b264582686f55f264a085bd78c6d000b185b7ab54d27afd"
container_name = "my-nginx-container"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
image_name = "nginx:latest"
```

## Yandex Cloud

### Setup instructions

1. Visit [https://console.yandex.cloud/](https://console.yandex.cloud/)
2. Create billing account. It should have status either `ACTIVE` or `TRIAL_ACTIVE`
3. Install YC and configure user

    ```sh
   yc config profile create <profile_name>
   yc config set service-account-key key.json
   yc config set cloud-id <cloud_ID>
   yc config set folder-id <folder_ID>
    ```

4. Export variables

    ```sh
    $Env:YC_TOKEN=$(yc iam create-token)
    $Env:YC_CLOUD_ID=$(yc config get cloud-id)
    $Env:YC_FOLDER_ID=$(yc config get folder-id)
    ```

5. Configure SSH key for user: I did this on the site using GUI.
6. Prepare workspace for Terraform for YandexCloud (main.tf, variables.tf)
7. Select image for VM

    ```bash
    yc compute image list --folder-id standard-images
    ```

### terraform init

```plaintext
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of yandex-cloud/yandex from the dependency lock file
- Using previously-installed yandex-cloud/yandex v0.136.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### terraform validate

```plaintext
Success! The configuration is valid.
```

### terraform plan

```plaintext
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # yandex_compute_instance.vm_1 will be created
  + resource "yandex_compute_instance" "vm_1" {
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
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL5kj6SdleOJffuGDFaK66CbiK9HC6Sna645CZSKx4kv bakin@SUPERSOF_Home
            EOT
        }
      + name                      = "terraform-vm-1"
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
              + image_id    = "fd800c7s2p483i648ifv"
              + name        = (known after apply)
              + size        = 20
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

  # yandex_vpc_network.network_1 will be created
  + resource "yandex_vpc_network" "network_1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet_1 will be created
  + resource "yandex_vpc_subnet" "subnet_1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

### terraform apply  

```plaintext
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # yandex_compute_instance.vm_1 will be created
  + resource "yandex_compute_instance" "vm_1" {
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
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL5kj6SdleOJffuGDFaK66CbiK9HC6Sna645CZSKx4kv bakin@SUPERSOF_Home
            EOT
        }
      + name                      = "terraform-vm-1"
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
              + image_id    = "fd800c7s2p483i648ifv"
              + name        = (known after apply)
              + size        = 20
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

  # yandex_vpc_network.network_1 will be created
  + resource "yandex_vpc_network" "network_1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet_1 will be created
  + resource "yandex_vpc_subnet" "subnet_1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network_1: Creating...
yandex_vpc_network.network_1: Creation complete after 4s [id=enphijhc00ckb2l62lc6]
yandex_vpc_subnet.subnet_1: Creating...
yandex_vpc_subnet.subnet_1: Creation complete after 0s [id=e9bu7upu460dm1msggah]
yandex_compute_instance.vm_1: Creating...
yandex_compute_instance.vm_1: Still creating... [40s elapsed]
yandex_compute_instance.vm_1: Still creating... [50s elapsed]
yandex_compute_instance.vm_1: Creation complete after 53s [id=fhmd4bbgku8edv603m40]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "158.160.33.11"
internal_ip_address_vm_1 = "192.168.20.4"
```

### `terraform state list` command

```plaintext
yandex_compute_instance.vm_1
yandex_vpc_network.network_1
yandex_vpc_subnet.subnet_1
```

### terraform state show

```plaintext
Exactly one argument expected.
Usage: terraform [global options] state show [options] ADDRESS

  Shows the attributes of a resource in the Terraform state.

  This command shows the attributes of a single resource in the Terraform
  state. The address argument must be used to specify a single resource.
  You can view the list of available resources with "terraform state list".

Options:

  -state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.

```

## Github

### terraform import "github_repository.repo" "S25-devops-engineering-labs"

```plaintext
github_repository.repo: Importing from ID "S25-devops-engineering-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-devops-engineering-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### `terraform apply` command line

```plaintext
github_repository.repo: Refreshing state... [id=S25-devops-engineering-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default will be created
  + resource "github_branch_default" "default" {
      + branch     = "lab4"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "S25-devops-engineering-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "lab4"
      + repository_id                   = "S25-devops-engineering-labs"
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
      + description                 = "Bakina Sofia"
      + gitignore_template          = "Python"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      ~ has_wiki                    = true -> false
        id                          = "S25-devops-engineering-labs"
      + license_template            = "mit"
        name                        = "S25-devops-engineering-labs"
        # (31 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.default: Creating...
github_branch_default.default: Creation complete after 2s [id=S25-devops-engineering-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOFodRr84Dig9l]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
