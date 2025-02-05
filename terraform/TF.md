# Terraform Best Practices:

1. **Avoid Hardcoding Secrets**
   - Used environment variables (`export GITHUB_TOKEN=...`, `export YC_TOKEN=...`) instead of storing sensitive information in `.tf` files.
   - Ensured API tokens were securely stored using system-level environment variables.

2. **Use Version Control for Terraform Files**
   - Stored Terraform configurations in Git repositories for change tracking.

3. **Use `terraform import` for Existing Resources**
   - Avoided duplications by importing existing Yandex Cloud VMs, Docker containers, and GitHub repositories into Terraform.
   - Used `terraform state rm` before re-importing when conflicts arose.

4. **Apply Branch Protection Rules Carefully in GitHub**
   - Ensured proper visibility settings to align with Terraform's capabilities.

5. **Keep Terraform State Secure**
   - Used **remote backends** (e.g., S3 for AWS, Yandex Object Storage) to store Terraform state securely.
   - Enabled state locking to prevent multiple users from making conflicting changes.

6. **Use Input Variables for Customization**
   - Defined `variables.tf` for modular configurations (e.g., repository name, VM size, container name).
   - Avoided hardcoded values to allow flexibility across environments.

7. **Use Modules for Better Organization**
   - Separated Yandex Cloud, Docker, and GitHub configurations into dedicated Terraform modules.
   - Improved reusability and maintainability of Terraform code.
     
---

# Docker Setup: Steps and Challenges

## **Steps Taken**
1. **Installing Terraform and VPN on Ubuntu**
   - Faced issues with installing Terraform due to missing dependencies.
   - Resolved by updating system packages and using official HashiCorp repository:
     ```sh
     sudo apt update && sudo apt install -y gnupg software-properties-common
     wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
     echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
     sudo apt update && sudo apt install terraform
     ```
   - Installed VPN to bypass network restrictions for Terraform provider downloads.

2. **Setting Up Terraform for Docker**
   - Created `main.tf` with the Docker provider configuration.
   - Used Docker provider to create an Nginx container.

3. **Applying Terraform Configuration**
   - Initialized Terraform with:
     ```sh
     terraform init
     ```
   - Applied the configuration successfully:
     ```sh
     terraform apply -auto-approve
     ```

## **Challenges Faced and Solutions**
- **Challenge:** Terraform installation issues
- *Solution: Used official HashiCorp repository and updated packages*
- **Challenge:** VPN needed for provider downloads
- *Solution: Installed VPN to bypass restrictions*
- **Challenge:** Docker daemon not running
- *Solution: Restarted Docker*

## Terraform show - docker
```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "d07f604cf6c4"
    id                                          = "d07f604cf6c4991332199d3914932c8611657829062c53d3c450f41f69b7e31d"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "terraform_nginx"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = [90mnull[0m[0m
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
    user                                        = [90mnull[0m[0m
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = [90mnull[0m[0m

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

```
## Terraform state list - docker
```
docker_container.nginx
docker_image.nginx
```

## Part of the log - docker
```
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
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
      + image                                       = "nginx:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "terraform_nginx"
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
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.
docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 30s [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=68596c6853d8abb473109f91e2d5b91fa3f7ef1bd6736da8efd411e4f09764bb]
```

## Part of the log after utilized input variables
```
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
      ~ hostname                                    = "894b98ab3325" -> (known after apply)
      ~ id                                          = "894b98ab3325e8b02b0ac08882328465819cdec41be1bb659147b94364598ee6" -> (known after apply)
      ~ image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b" -> "nginx:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "custom_nginx"
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
        # (19 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + contain_name = "custom_nginx"
  + container_id = (known after apply)
docker_container.nginx: Destroying... [id=894b98ab3325e8b02b0ac08882328465819cdec41be1bb659147b94364598ee6]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=4e996e40274cb4c51e4c1a07eaf8543e4da01493d31242928d951d86b6abf125]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Terraform output - docker
```
contain_name = "custom_nginx"
container_id = "4e996e40274cb4c51e4c1a07eaf8543e4da01493d31242928d951d86b6abf125"
```
---

# Yandex Cloud Setup: Steps and Challenges

## **Steps Taken**
1. **Setting Up Yandex Cloud Account**
   - Created a Yandex Cloud account and set up a billing account.
   - Enabled the required APIs for Terraform integration.

2. **Configuring IAM Roles and Permissions**
   - Initially faced permission issues while creating resources via Terraform.
   - Required additional IAM roles (`vpc.publicAdmin`, `compute.editor`).
   - Granted the necessary roles using the command:
     ```sh
     yc resource-manager folder add-access-binding default \
       --role vpc.publicAdmin --subject userAccount:<user-id>
     ```

3. **Subnet and Network Creation**
   - Faced issues when trying to create a VM without a subnet.
   - Created a Virtual Private Cloud (VPC) and a subnet using:
     ```sh
     yc vpc network create --name terraform-network
     yc vpc subnet create \
       --name terraform-subnet \
       --network-name terraform-network \
       --range 10.128.0.0/24 \
       --zone ru-central1-a
     ```
   - Used the obtained subnet ID in Terraform.

4. **Image ID Issues**
   - Encountered an error: `Image ID not found`.
   - Resolved by listing available images:
     ```sh
     yc compute image list --folder-id standard-images
     ```
   - Used `image_family = "ubuntu-22-04-lts"` in Terraform instead of a fixed image ID.

5. **Deploying the VM via Terraform**
   - Successfully applied Terraform configuration to create a VM.
   - Verified VM status using:
     ```sh
     yc compute instance list
     ```

## **Challenges Faced and Solutions**
- **Challenge:** Missing IAM permissions
- *Solution: Added `vpc.publicAdmin` & `compute.editor` roles manually*
- **Challenge:** Subnet required for VM
- *Solution: Created a subnet using CLI and assigned it to Terraform*
- **Challenge:** Image ID not found
- *Solution: Used `yc compute image list` to find valid images*
- **Challenge:** Permission denied in CLI
- *Solution: Re-authenticated using `yc init` and verified IAM roles*
- **Challenge:** Billing not activated
- *Solution: Linked a billing account to enable resource creation*


## Terraform show - yandex cloud
```
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2025-02-05T14:41:17Z"
    description               = null
    folder_id                 = "b1g7qk6ml5o8aifii5ui"
    fqdn                      = "epd58u88rg84d6p3oh0h.auto.internal"
    gpu_cluster_id            = null
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    hostname                  = null
    id                        = "epd58u88rg84d6p3oh0h"
    maintenance_grace_period  = null
    name                      = "terraform-instance"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epd4fgdat3io3rj9vqp9"
        disk_id     = "epd4fgdat3io3rj9vqp9"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd86idv7gmqapoeiq5ld"
            kms_key_id  = null
            name        = null
            size        = 10
            snapshot_id = null
            type        = "network-hdd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "10.129.0.22"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:54:79:08:dc"
        nat                = true
        nat_ip_address     = "158.160.88.42"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2lle94hhbsqjigo1rgm"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}


Outputs:

vm_external_ip = "158.160.88.42"
vm_id = "epd58u88rg84d6p3oh0h"
vm_internal_ip = "10.129.0.22"
vm_name = "terraform-instance"
vm_status = "running"
```
## Terraform state list - yandex cloud
```
yandex_compute_instance.vm
```

## Part of the log
```
Terraform will perform the following actions:

  # yandex_compute_instance.vm will be created
  + resource "yandex_compute_instance" "vm" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + name                      = "terraform-instance"
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
              + image_id    = "fd86idv7gmqapoeiq5ld"
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
          + subnet_id          = "e2lle94hhbsqjigo1rgm"
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + vm_external_ip = (known after apply)
  + vm_id          = (known after apply)
  + vm_internal_ip = (known after apply)
  + vm_status      = (known after apply)
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Still creating... [40s elapsed]
yandex_compute_instance.vm: Still creating... [50s elapsed]
yandex_compute_instance.vm: Still creating... [1m0s elapsed]
yandex_compute_instance.vm: Creation complete after 1m3s [id=epd58u88rg84d6p3oh0h]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```
## Terraform output - yandex cloud
```
vm_external_ip = "158.160.88.42"
vm_id = "epd58u88rg84d6p3oh0h"
vm_internal_ip = "10.129.0.22"
vm_name = "terraform-instance"
vm_status = "running"
```
---

# GitHub Setup: Steps and Challenges

## **Steps Taken**
1. **Setting Up Terraform for GitHub**
   - Created a new directory `terraform/github` to manage GitHub repositories.
   - Configured Terraform provider for GitHub.
   - Created `.tf` files to define repository attributes such as:
     - Repository name
     - Description
     - Visibility
     - Default branch
     - Branch protection rules

2. **Authenticating with GitHub**
   - Avoided storing tokens in `.tf` files and used an environment variable:
     ```sh
     export GITHUB_TOKEN="my_github_token_here"
     ```
3  **Create Repository and apply changes**
   ```bash
   terraform apply -auto-approve
   ```

4. **Importing an Existing Repository**
   - Used Terraform import to manage an existing repo:
     ```sh
     terraform import github_repository.my_repo S25-core-course-labs
     ```

4. **Applying Terraform Configuration**
   - Initialized Terraform with:
     ```sh
     terraform init
     ```
   - Applied changes successfully:
     ```sh
     terraform apply -auto-approve
     ```

## **Challenges Faced and Solutions**
- **Challenge:** Branch protection misconfigurations
- *Solution: Ensured proper branch protection rules in `.tf`*
- **Challenge:** Repository rename error
- *Solution: Kept the existing repository name or used `terraform state rm`*


## Terraform show - GitHub
```
# github_repository.my_repo:
resource "github_repository" "my_repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "master"
    delete_branch_on_merge      = false
    description                 = "Repository managed via Terraform"
    etag                        = "W/\"f364fca143c9b1c1eea187080f5e2c8e81996d10bfa3e633022ea40137fe02fd\""
    full_name                   = "DoryShibkova/terraform-managed-repo"
    git_clone_url               = "git://github.com/DoryShibkova/terraform-managed-repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    homepage_url                = null
    html_url                    = "https://github.com/DoryShibkova/terraform-managed-repo"
    http_clone_url              = "https://github.com/DoryShibkova/terraform-managed-repo.git"
    id                          = "terraform-managed-repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "terraform-managed-repo"
    node_id                     = "R_kgDON02JRw"
    primary_language            = null
    private                     = true
    repo_id                     = 927828295
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:DoryShibkova/terraform-managed-repo.git"
    svn_url                     = "https://github.com/DoryShibkova/terraform-managed-repo"
    topics                      = []
    visibility                  = "private"
    vulnerability_alerts        = false
    web_commit_signoff_required = false
}


Outputs:

repository_id = "R_kgDON02JRw"
repository_name = "terraform-managed-repo"
repository_url = "https://github.com/DoryShibkova/terraform-managed-repo"
```

## Terraform state list - GitHub
```
github_repository.my_repo
```

## Part of the log
```
Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_protection.main_branch[0] will be created
  + resource "github_branch_protection" "main_branch" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = false
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + dismiss_stale_reviews           = true
          + require_code_owner_reviews      = true
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }

      + required_status_checks {
          + strict = true
        }
    }

  # github_repository.my_repo will be created
  + resource "github_repository" "my_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Repository managed via Terraform"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "terraform-managed-repo"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "private"
      + web_commit_signoff_required = false

      + security_and_analysis (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repository_id   = (known after apply)
  + repository_name = "terraform-managed-repo"
  + repository_url  = (known after apply)
github_repository.my_repo: Creating...
github_repository.my_repo: Creation complete after 7s [id=terraform-managed-repo]
github_branch_protection.main_branch[0]: Creating...
```

## Terraform output - GitHub
```
repository_id = "R_kgDON02JRw"
repository_name = "terraform-managed-repo"
repository_url = "https://github.com/DoryShibkova/terraform-managed-repo"
```

## After - Import Existing Repository
```
Terraform will perform the following actions:

  # github_repository.my_repo will be updated in-place
  ~ resource "github_repository" "my_repo" {
      ~ auto_init                   = false -> true
      + description                 = "Repository managed via Terraform"
      ~ full_name                   = "DoryShibkova/S25-core-course-labs" -> (known after apply)
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "S25-core-course-labs"
      ~ name                        = "S25-core-course-labs" -> "terraform-managed-repo"
      ~ visibility                  = "public" -> "private"
        # (29 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  ~ repository_name = "S25-core-course-labs" -> "terraform-managed-repo"
github_repository.my_repo: Modifying... [id=S25-core-course-labs]
```
---

# GitHub Teams Setup: Steps and Challenges

## **Steps Taken**

1. **Upgrading to a GitHub Organization**
- Converted the personal GitHub account into an organization to enable team management.

2. ***Defining Teams in Terraform**
- Created teams with different access levels:

3. **Applying Team Configuration**
- Applied Terraform changes to add teams and grant access:
  ```sh
  terraform apply -auto-approve
  ```
- Verified team permissions in GitHub settings.

## **Challenges Faced and Solutions**

- **Challenge** Authentication issues due to incorrect token scope.
- *Solution: Generated a new token with `repo` and `admin:org` scopes from GitHub.*


## Terraform show - GitHub Teams
```
# github_team.teams["admins"]:
resource "github_team" "teams" {
    create_default_maintainer = false
    description               = "Admin Team"
    etag                      = "W/\"1b9c3f4a9f5f468c7228272bdfc427667af277d2ac44c4466e78220bbc545ab1\""
    id                        = "12122396"
    ldap_dn                   = null
    members_count             = 0
    name                      = "admins"
    node_id                   = "T_kwDOC8y4YM4AuPkc"
    parent_team_id            = null
    parent_team_read_id       = null
    parent_team_read_slug     = null
    privacy                   = "closed"
    slug                      = "admins"
}

# github_team.teams["developers"]:
resource "github_team" "teams" {
    create_default_maintainer = false
    description               = "Development Team"
    etag                      = "W/\"3cc679f92861fd51c4daa4d25c9690c0f5dc25a4e642c9925660c5984c269e98\""
    id                        = "12122395"
    ldap_dn                   = null
    members_count             = 0
    name                      = "developers"
    node_id                   = "T_kwDOC8y4YM4AuPkb"
    parent_team_id            = null
    parent_team_read_id       = null
    parent_team_read_slug     = null
    privacy                   = "closed"
    slug                      = "developers"
}

# github_team.teams["qa"]:
resource "github_team" "teams" {
    create_default_maintainer = false
    description               = "Quality Assurance Team"
    etag                      = "W/\"9a6b520fef63b8f7d5d3d5dd6325403757776f9623f9c46f4251cb887d4c7256\""
    id                        = "12122398"
    ldap_dn                   = null
    members_count             = 0
    name                      = "qa"
    node_id                   = "T_kwDOC8y4YM4AuPke"
    parent_team_id            = null
    parent_team_read_id       = null
    parent_team_read_slug     = null
    privacy                   = "closed"
    slug                      = "qa"
}

# github_team.teams["viewers"]:
resource "github_team" "teams" {
    create_default_maintainer = false
    description               = "Read-Only Access"
    etag                      = "W/\"2a06f7017a6278ec5f304b0781d671fd41769716169fbcd2c74a04dfb8fb986d\""
    id                        = "12122399"
    ldap_dn                   = null
    members_count             = 0
    name                      = "viewers"
    node_id                   = "T_kwDOC8y4YM4AuPkf"
    parent_team_id            = null
    parent_team_read_id       = null
    parent_team_read_slug     = null
    privacy                   = "closed"
    slug                      = "viewers"
}


Outputs:

repository_access = {
    "12122395" = "push"
    "12122396" = "admin"
    "12122398" = "triage"
    "12122399" = "pull"
}
team_ids = {
    admins     = "12122396"
    developers = "12122395"
    qa         = "12122398"
    viewers    = "12122399"
}
```

## Terraform state list - GitHub Teams
```
github_team.teams["admins"]
github_team.teams["developers"]
github_team.teams["qa"]
github_team.teams["viewers"]
```

## Part of the log - GitHub Teams
```
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team_repository.team_access["admins"] will be created
  + resource "github_team_repository" "team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "Terraform_lab4"
      + team_id    = "12122396"
    }

  # github_team_repository.team_access["developers"] will be created
  + resource "github_team_repository" "team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "Terraform_lab4"
      + team_id    = "12122395"
    }

  # github_team_repository.team_access["qa"] will be created
  + resource "github_team_repository" "team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "triage"
      + repository = "Terraform_lab4"
      + team_id    = "12122398"
    }

  # github_team_repository.team_access["viewers"] will be created
  + resource "github_team_repository" "team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "Terraform_lab4"
      + team_id    = "12122399"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repository_access = {
      + "12122395" = "push"
      + "12122396" = "admin"
      + "12122398" = "triage"
      + "12122399" = "pull"
    }
github_team_repository.team_access["admins"]: Creating...
github_team_repository.team_access["developers"]: Creating...
github_team_repository.team_access["qa"]: Creating...
github_team_repository.team_access["viewers"]: Creating...
```

## Terraform output - GitHub
```
repository_access = {
  "12122395" = "push"
  "12122396" = "admin"
  "12122398" = "triage"
  "12122399" = "pull"
}
team_ids = {
  "admins" = "12122396"
  "developers" = "12122395"
  "qa" = "12122398"
  "viewers" = "12122399"
}
```
