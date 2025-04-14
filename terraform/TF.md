# Terraform Infrastructure Documentation

## Task 1: Introduction to Terraform

### 1. Getting Started

- Installed Terraform following official documentation
- Set up workspace in `terraform` folder
- Organized configurations into separate directories for each provider

### 2. Docker Infrastructure

#### Setup and Configuration

1. Initialized Terraform workspace:

    ```bash
    cd terraform/docker
    terraform init
    ```

2. State Commands Output:

    ```bash
    $ terraform state list
    docker_container.python_app
    docker_image.python_app

    $ terraform state show docker_container.python_app
    # docker_container.python_app:
    resource "docker_container" "python_app" {
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
        env                                         = [
            "TZ=Europe/Moscow",
        ]
        hostname                                    = "40203c61876b"
        id                                          = "40203c61876bcd7930fb39f1372abfe9b0cafad9f0cb0758b2adaf6835b097d8"
        image                                       = "sha256:edd5b508af4a96f3b20337e06b9bfdf3e4a6107253c9a92264be0ac0e4fed63e"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "python_app"
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
        restart                                     = "unless-stopped"
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
            external = 5001
            internal = 5000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }

    $ terraform state show image.python_app
    # docker_image.python_app:
    resource "docker_image" "python_app" {
        id           = "sha256:edd5b508af4a96f3b20337e06b9bfdf3e4a6107253c9a92264be0ac0e4fed63emazzz3r/app_python:latest"
        image_id     = "sha256:edd5b508af4a96f3b20337e06b9bfdf3e4a6107253c9a92264be0ac0e4fed63e"
        keep_locally = false
        name         = "mazzz3r/app_python:latest"
        repo_digest  = "mazzz3r/app_python@sha256:edd5b508af4a96f3b20337e06b9bfdf3e4a6107253c9a92264be0ac0e4fed63e"
    }
    ```

3. Applied Changes Log:

    ```bash
    $ terraform apply
    ...
    docker_container.python_app: Destroying... [id=81fd03ab0abb874ce7415688d0a2d08598bf42e1c0f6446602323d31e5ff6700]
    docker_container.python_app: Destruction complete after 0s
    docker_container.python_app: Creating...
    docker_container.python_app: Creation complete after 0s [id=40203c61876bcd7930fb39f1372abfe9b0cafad9f0cb0758b2adaf6835b097d8]

    Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

    Outputs:

    container_id = "40203c61876bcd7930fb39f1372abfe9b0cafad9f0cb0758b2adaf6835b097d8"
    image_id = "sha256:edd5b508af4a96f3b20337e06b9bfdf3e4a6107253c9a92264be0ac0e4fed63emazzz3r/app_python:latest"
    ```

4. Using Input Variables for Container Name:

    ```bash
    $ terraform apply -var="container_name=custom_name"

    $ docker ps

    CONTAINER ID   IMAGE          COMMAND           CREATED              STATUS              PORTS                    NAMES
    d734b258b0cc   edd5b508af4a   "python app.py"   About a minute ago   Up About a minute   0.0.0.0:5001->5000/tcp   custom_name
    ```

### 3. Yandex Cloud Infrastructure

#### Setup Process

1. Created Yandex Cloud account
2. Installed Yandex Cloud CLI:

    ```bash
    curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
    yc init
    ```

3. Configuration Steps:

    ```bash
    # Retrieved cloud configuration
    yc config get cloud-id
    yc config get folder-id

    export TF_VAR_token="yc-token"
    export TF_VAR_cloud_id="cloud-id"
    export TF_VAR_folder_id="folder-id"
    export TF_VAR_image_id="ubuntu-image-id"
    export TF_VAR_subnet_id="subnet-id"
    ```

4. Terraform Initialization:

    ```bash
    cd terraform/yandex
    terraform init
    terraform plan
    terraform apply
    ```

5. State Commands Output:

    ```bash
    $ terraform state list
    yandex_compute_instance.app_server

    $ terraform state show yandex_compute_instance.app_server
    # yandex_compute_instance.app_server:
    resource "yandex_compute_instance" "app_server" {
        created_at                = "2025-02-04T12:31:25Z"
        description               = null
        folder_id                 = "b1gg4c2h04a8ufroh2p7"
        fqdn                      = "fhmcj7hjv9ioestk2tef.auto.internal"
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
        id                        = "fhmcj7hjv9ioestk2tef"
        maintenance_grace_period  = null
        metadata                  = {
            "ssh-keys" = ...
        }
        name                      = "python-app-server"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        service_account_id        = null
        status                    = "running"
        zone                      = "ru-central1-a"

        boot_disk {
            auto_delete = true
            device_name = "fhmkppkr5n9ob4igvtvf"
            disk_id     = "fhmkppkr5n9ob4igvtvf"
            mode        = "READ_WRITE"

            initialize_params {
                block_size  = 4096
                description = null
                image_id    = "fd805qs1mn3n0casp7lt"
                kms_key_id  = null
                name        = null
                size        = 15
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
            ip_address         = "10.128.0.12"
            ipv4               = true
            ipv6               = false
            ipv6_address       = null
            mac_address        = "d0:0d:c9:9e:33:fa"
            nat                = true
            nat_ip_address     = "89.169.132.86"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9bg78md79nt3rg6m3cp"
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
    ```

#### Infrastructure Details

- VM Configuration:
  - 2 cores
  - 2GB RAM
  - Ubuntu 20.04 LTS
  - NAT enabled for external access
  - SSH key authentication

#### Challenges Encountered and Solutions

1. **Authentication**:
   - Challenge: Secure token management
   - Solution: Used environment variables for sensitive data

## Task 2: Terraform for GitHub

### 1. GitHub Infrastructure Setup

#### Configuration Details

1. Provider setup with environment variables:

    ```bash
    export TF_VAR_github_token="<token>"
    ```

2. Repository Import:

    ```bash
    $ terraform import github_repository.S25-core-course-labs S25-core-course-labs
    github_repository.S25-core-course-labs: Importing from ID "S25-core-course-labs"...
    github_repository.S25-core-course-labs: Import prepared!
    Prepared github_repository for import
    github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]

    Import successful!

    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.
    ```

3. Applied Configuration:

    ```bash
    terraform plan
    terraform apply
    ```

4. State Commands Output:

    ```bash
    $ terraform state list
    github_branch_protection.main
    github_repository.S25-core-course-labs

    $ terraform state show github_repository.S25-core-course-labs
    # github_repository.S25-core-course-labs:
    resource "github_repository" "S25-core-course-labs" {
        allow_auto_merge            = false
        allow_merge_commit          = true
        allow_rebase_merge          = true
        allow_squash_merge          = true
        allow_update_branch         = false
        archived                    = false
        auto_init                   = true
        default_branch              = "master"
        delete_branch_on_merge      = false
        description                 = "Repository for Core Course Labs"
        etag                        = "..."
        full_name                   = "mazzz3r/S25-core-course-labs"
        git_clone_url               = "git://github.com/mazzz3r/S25-core-course-labs.git"
        has_discussions             = false
        has_downloads               = true
        has_issues                  = true
        has_projects                = true
        has_wiki                    = true
        homepage_url                = null
        html_url                    = "https://github.com/mazzz3r/S25-core-course-labs"
        http_clone_url              = "https://github.com/mazzz3r/S25-core-course-labs.git"
        id                          = "S25-core-course-labs"
        is_template                 = false
        merge_commit_message        = "PR_TITLE"
        merge_commit_title          = "MERGE_MESSAGE"
        name                        = "S25-core-course-labs"
        node_id                     = "R_kgDONu369Q"
        primary_language            = null
        private                     = false
        repo_id                     = 921565941
        squash_merge_commit_message = "COMMIT_MESSAGES"
        squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        ssh_clone_url               = "git@github.com:mazzz3r/S25-core-course-labs.git"
        svn_url                     = "https://github.com/mazzz3r/S25-core-course-labs"
        topics                      = []
        visibility                  = "public"
        vulnerability_alerts        = false
        web_commit_signoff_required = false

        security_and_analysis {
            secret_scanning {
                status = "enabled"
            }
            secret_scanning_push_protection {
                status = "enabled"
            }
        }
    }

    $ terraform state show github_branch_protection.main
    # github_branch_protection.main:
    resource "github_branch_protection" "main" {
        allows_deletions                = false
        allows_force_pushes             = false
        blocks_creations                = false
        enforce_admins                  = false
        id                              = "BPR_kwDONu369c4DiRUH"
        lock_branch                     = false
        pattern                         = "main"
        repository_id                   = "R_kgDONu369Q"
        require_conversation_resolution = false
        require_signed_commits          = false
        required_linear_history         = false

        required_pull_request_reviews {
            dismiss_stale_reviews           = true
            require_code_owner_reviews      = false
            require_last_push_approval      = false
            required_approving_review_count = 1
            restrict_dismissals             = false
        }

        required_status_checks {
            contexts = [
                "build",
            ]
            strict   = true
        }
    }
    ```

#### Repository Settings

- Name: core-course-labs
- Visibility: Public
- Features: Issues, Wiki, Downloads, Projects enabled
- Branch protection rules implemented

## Best Practices Implemented

### 1. Security

- Environment variables for sensitive data
- No hardcoded credentials
- SSH key authentication
- Branch protection rules

### 2. State Management

- Separate state files for each infrastructure
- Regular state backups
- State commands documented

### 3. Code Organization

- Modular structure
- Clear separation of concerns
- Consistent naming conventions

### 4. Resource Management

- Minimal resource allocation
- Proper tagging
- Clear documentation

### 5. Version Control

- .gitignore for sensitive files
- Documentation in markdown
- Clear commit messages

## Common Operations

### Initialize Infrastructure

```bash
terraform init
```

### Plan Changes

```bash
terraform plan -out=tfplan
```

### Apply Changes

```bash
terraform apply tfplan
```

### Destroy Infrastructure

```bash
terraform destroy
```

## Future Improvements

1. Implement remote state storage
2. Add monitoring and logging
3. Implement automatic backups
4. Add more security measures
5. Implement CI/CD pipeline integration
