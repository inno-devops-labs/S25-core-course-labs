# Terraform

## Docker Infrastructure Using Terraform

### 1. Terraform Installation

Commands for MacOS:

```bash
brew tap hashicorp/tap                             
brew install hashicorp/tap/terraform 
terraform --version
```

### 2. Terraform Initialization

```bash
terraform init
```

### 3. Applying Terraform Configuration

```bash
terraform apply -auto-approve
```

### 4. Terraform State List

```bash
terraform state list
```

#### Output of the command

```bash
docker_container.app_container
docker_image.app_image
```

### 5. Terraform State Show

```bash
terraform state show docker_container.app_container 
```

#### Output of the command

```bash
# docker_container.app_container:
resource "docker_container" "app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "uvicorn",
        "app:app",
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
    hostname                                    = "<hostname>"
    id                                          = "<id>"
    image                                       = "<image>"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-container"
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
    user                                        = null
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

### 6. Teraform Output

```bash
terraform output
```

#### Output of the command

```bash
container_id = "<id>"
container_name = "moscow-time-container"
```

## Yandex Cloud Infrastracture Using Terraform

### 1. Install Yandex Cloud CLI

Commands fr MacOS:

```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
exec -l $SHELL
```

#### Verify Installation

```bash
yc --version
```

#### Output of the command

```bash
Yandex Cloud CLI 0.142.0 darwin/arm64
```

### 2. Authenticate Yandex Cloud CLI

```bash
yc init
```

#### Verify Configuration

```bash
yc config list
```

#### Output of the command

```bash
token: TOKEN
cloud-id: ID
folder-id: ID
compute-default-zone: ru-central1-a
```

### 3. Set Up Terraform for Yandex Cloud

Created Yandex Cloud Terraform configuration ```yandex_cloud.tf```.

### 4. Initialize and Apply Terraform

```bash
terraform init
```

```bash
terraform validate
```

#### Output of the command

```bash
Success! The configuration is valid.
```

```bash
terraform apply -auto-approve
```

#### Output of the command

```bash
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

vm_ip = IP
```

#### State List

```bash
terraform state list
```

#### Output of the command

```bash
yandex_compute_instance.vm
```

#### State Show

```bash
terraform state show yandex_compute_instance.vm 
```

#### Output of the command

```bash
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2025-02-05T18:23:08Z"
    description               = null
    folder_id                 = "b1grrrgtgiho0qcnbua1"
    fqdn                      = "fhmfv0dlia93ek56v0qu.auto.internal"
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
    id                        = "fhmfv0dlia93ek56v0qu"
    maintenance_grace_period  = null
    name                      = "my-yandex-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm225mosfsmv46s5pn8"
        disk_id     = "fhm225mosfsmv46s5pn8"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd86jl8gechvgkabt374"
            kms_key_id  = null
            name        = null
            size        = 5
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
        ip_address         = "10.128.0.4"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:ff:81:b5:92"
        nat                = true
        nat_ip_address     = "51.250.83.48"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bgph0mo40nut6fn2no"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 20
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}
```

### 5. Connect to VM via SSH

```bash
ssh ubuntu@IP
```

### Best Practices Applied

 1. **Modularity**
    - Defined variables (```variables.tf```) to separate configuration details from logic which allows easy updates to resource parameters.
 2. **Security**
    - Used environment variables to store secrets instead of hardcoding API tokens.
    - Service Account Authentication instead of personal credentials.
 3. **State Management**
    - Used terraform state list and terraform state show to track resources.
    - Ensured state files are stored securely.
 4. **Resource Optimization**
    - Used Yandex Free Tier VM to avoid unnecessary costs.
    - Defined CPU and RAM limits efficiently.
 5. **Version Pinning**
    - Specified Terraform provider versions.

## Challenges Faced

1. **Permission Errors in Yandex Cloud**

    *Issue:* Received ```PermissionDenied``` error while applying Terraform.

    *Fix:* Manually granted the required IAM permissions on Yandex Cloud account.

2. **SSH Authentication Failing**

    *Issue:* Could not connect to VM via SSH.

    *Fix:* Manually generated rsa key pair:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "<mail>"
    ```

3. **Subnet ID Identification**

    *Issue:* Could not find the subnet id.

    *Fix:* Manually found the subnet id:

    ```bash
    yc vpc subnet list
    ```

4. **Image ID Identification**

    *Issue:* Could not find the image id.

    *Fix:* Manually found the image id:

    ```bash
    yc compute image list
    ```

## Terraform for GitHub

### 1. Initialize and Apply Terraform

```bash
terraform init
```

#### Output of the command

```bash
...
Terraform has been successfully initialized!
...
```

```bash
terraform import github_repository.core_course_labs S25-core-course-labs 
```

#### Output of the command

```bash
github_repository.core_course_labs: Importing from ID "S25-core-course-labs"...
github_repository.core_course_labs: Import prepared!
  Prepared github_repository for import
github_repository.core_course_labs: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

#### Verify the Import

```bash
terraform state list
```

#### Output of the command

```bash
github_repository.core_course_labs
```

#### Apply Terraform Changes

```bash
terraform apply -auto-approve
```

#### Output of the command

```bash
github_repository.core_course_labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "core_course_labs"
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

  # github_repository.core_course_labs will be updated in-place
  ~ resource "github_repository" "core_course_labs" {
      ~ auto_init                   = false -> true
      + description                 = "Terraform-managed repository for DevOps labs"
      + gitignore_template          = "VisualStudio"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
      ~ name                        = "S25-core-course-labs" -> "core_course_labs"
        # (28 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.
github_repository.core_course_labs: Modifying... [id=S25-core-course-labs]
github_repository.core_course_labs: Modifications complete after 3s [id=core_course_labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=core_course_labs]
...
```

### Best Practices Applied

1. **Security**
    - Used environment variables to store secrets instead of hardcoding API tokens.

2. **State Mangement**
    - Ensured an existing repo is managed by Terraform instead of creating a new one.
