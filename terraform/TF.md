# Task 1: Introduction to Terraform

## 1. Installing terraform

## 2. Docker configuraion

1. terraform state list

```bash
$ cd terrafrom/docker
$ terraform state list
docker_container.python_app
docker_image.python_app
```

2. commands output:

```bash
$ terraform state show docker_container.python_app
# docker_container.nginx_container:
# docker_container.python_app:
resource "docker_container" "python_app" {
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
    hostname                                    = "d3b6216c8e9e"
    id                                          = "d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a"
    image                                       = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_web_app"
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
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

$ terraform state show docker_image.nginx 
# docker_image.python_app:
resource "docker_image" "python_app" {
    id           = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
    image_id     = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
    keep_locally = false
    name         = "jlfkajlkifj/app_python:latest"
    repo_digest  = "jlfkajlkifj/app_python@sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
}

```

3. terraform apply log

```bash
docker_image.nginx: Refreshing state... [id=sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcefnginx]
docker_container.nginx_container: Refreshing state... [id=c32efdcff7910807f6382be46315febcccfdbcdea62ab430c8daa3170d406f1b]

...

[id=c32efdcff7910807f6382be46315febcccfdbcdea62ab430c8daa3170d406f1b]
docker_image.python_app: Creating...
docker_container.nginx_container: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcefnginx]
docker_image.nginx: Destruction complete after 1s
docker_image.python_app: Still creating... [10s elapsed]
docker_image.python_app: Creation complete after 11s [id=sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest]
docker_container.python_app: Creating...
docker_container.python_app: Creation complete after 3s [id=d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

container_id = "d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_status = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
```

4. utilizing input variables to rename docker container

```bash
$ terraform apply -var="container_name=whatever"

$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                    NAMES
59f1bebfbbdc   ce9d72aa69bf   "uvicorn app:app --h…"   7 seconds ago   Up 6 seconds   0.0.0.0:8000->8000/tcp   whatever
```

5.output of the `terraform output`

```bash
$ terraform output
container_id = "59f1bebfbbdcdf22a12cd8856a622b257f3002fc3570d5d36e256c68079d3ee0"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_status = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
```

## 3. Yandex Cloud

1. get yandex cloud account
2. Following instructions from official documentation (instructions with the use of yandex cli tool)

```bash
$ yc iam service-account create --name terraform-user
$ yc resource-manager folder add-access-binding default --role editor --subject serviceAccount:$(yc iam service-account get terraform-user --format=json | jq -r '.id')
$ yc iam key create --service-account-name terraform-user --output key.json
$ yc config profile create sa-terraform
$ yc config set cloud-id <ID>
$ yc config set folder-id <ID>

# using command with prefilled .env file (cp .env.example .env)
$ export $(grep -v '^#' .env | tr -d '\r' | xargs)

```

3. prepare and run terraform

```bash
$ terraform init
$ terraform plan
$ terraform apply
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Still creating... [40s elapsed]
yandex_compute_instance.vm: Creation complete after 43s [id=fhm198ofngo67keno0oo]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

external_ip = "62.84.114.182"
internal_ip = "10.128.0.20"
vm_id = "fhm198ofngo67keno0oo"

$ terraform state list
yandex_compute_instance.vm
$ terraform state show yandex_compute_instance.vm
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2025-02-06T07:33:47Z"
    description               = null
    folder_id                 = "b1gi6gaakrk344s01bdb"
    fqdn                      = "fhm198ofngo67keno0oo.auto.internal"
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
    id                        = "fhm198ofngo67keno0oo"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa 
        EOT
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm0258udefiejbena7o"
        disk_id     = "fhm0258udefiejbena7o"
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
        ip_address         = "10.128.0.20"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:14:a3:0f:bc"
        nat                = true
        nat_ip_address     = "62.84.114.182"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bdrdmagsihu74fvkp5"
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

# vm destory to not loose money
$ terraform destroy
```
![alt text](image.png)

VM setup: 
- 2 cores
- 2GB RAM
- Ubuntu 20.04 LTS
- NAT enabled for external access
- SSH key authentication


## Task 2: Terraform for Github
Provider setup with environment variables:
```
$ terraform init
$ terraform import github_repository.S25-core-course-labs S25-core-course-labs
github_repository.S25-core-course-labs: Importing from ID "S25-core-course-labs"...
github_repository.S25-core-course-labs: Import prepared!
  Prepared github_repository for import
github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]

$ terraform apply
github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_protection.main will be created
  + resource "github_branch_protection" "main" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = false
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "R_kgDONywcqw"
      + require_conversation_resolution = false
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + dismiss_stale_reviews           = true
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }

      + required_status_checks {
          + contexts = [
              + "build",
            ]
          + strict   = true
        }
    }

  # github_repository.S25-core-course-labs will be updated in-place
  ~ resource "github_repository" "S25-core-course-labs" {
      ~ auto_init                   = false -> true
      + description                 = "A GitHub repository managed with Terraform"
      ~ has_issues                  = false -> true
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 1 to change, 0 to destroy.
github_repository.S25-core-course-labs: Modifying... [id=S25-core-course-labs]
github_repository.S25-core-course-labs: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_protection.main: Creating...
github_branch_protection.main: Creation complete after 3s [id=BPR_kwDONywcq84Dijjm]

Apply complete! Resources: 1 added, 1 changed, 0 destroyed.

Outputs:

repository_id = "R_kgDONywcqw"
repository_url = "https://github.com/Poxidq/S25-core-course-labs"

$ terraform state list
github_branch_protection.main
github_repository.S25-core-course-labs

$  terraform state show github_repository.S25-core-course-labs
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
    description                 = "A GitHub repository managed with Terraform"
    etag                        = "W/\"744850763ba13d6a5cb548a134e4ba94743eff41cadd32e67647ff2cfe5e726e\""
    full_name                   = "Poxidq/S25-core-course-labs"
    git_clone_url               = "git://github.com/Poxidq/S25-core-course-labs.git"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = true
    has_projects                = true
    has_wiki                    = true
    homepage_url                = null
    html_url                    = "https://github.com/Poxidq/S25-core-course-labs"
    http_clone_url              = "https://github.com/Poxidq/S25-core-course-labs.git"
    id                          = "S25-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S25-core-course-labs"
    node_id                     = "R_kgDONywcqw"
    primary_language            = null
    private                     = false
    repo_id                     = 925637803
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Poxidq/S25-core-course-labs.git"
    svn_url                     = "https://github.com/Poxidq/S25-core-course-labs"
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

```

## Terraform Best Practices Applied
### 1. Securely Managing Secrets Using Environment Variables
Stored GitHub Token in .env file instead of directly defining it in main.tf.
Used TF_VAR_github_token to load variables securely.

Example (.env file):

```bash
TF_VAR_github_token="ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

load the .env file securely?
```bash
export $(grep -v '^#' .env | tr -d '\r' | xargs)
```

### 2. Importing Existing GitHub Repositories Instead of Recreating
Used terraform import to sync Terraform with an existing GitHub repository.
Command to Import an Existing Repository:

```bash
terraform import github_repository.my_repo my-existing-repo
```

### 3. Preventing Accidental Repository Deletion
Terraform can destroy resources, so we protect critical repositories.

Used `lifecycle.prevent_destroy = true` to avoid accidental deletion of repositories.

### 4. Separating variables and config data into separate file
Used `variables.tf` to store variables used in `main.tf`