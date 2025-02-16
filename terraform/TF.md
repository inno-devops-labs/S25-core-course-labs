# TF.md

## Docker Infrastructure

###  ```terraform state list```
```
docker_container.nginx
docker_image.nginx
```


### ```terraform state show docker_image.nginx```
```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```


### ```terraform state show docker_container.nginx```
```
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
    hostname                                    = "aac88e6fd61d"
    id                                          = "aac88e6fd61d785f4e6ff3d4da112fbf8d393acdf5e4d9ac6563e8dd81c719be"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my_devops_container"
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
```

### Logging for applied changes
```
Terraform used the selected providers to generate the following execution plan. Resource   
actions are indicated with the following symbols:
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
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my_devops_container"
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

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 9s [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=aac88e6fd61d785f4e6ff3d4da112fbf8d393acdf5e4d9ac6563e8dd81c719be]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```


### terraform output
```
container_id = "881bab2fae20b61f23a532bfaf4092601b3279ea326a3f98ccef9ed5703d4b19"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```

## Yandex Cloud Infrastructure

### Setup Steps
1. Created an account on Yandex Cloud.
2. Followed the Yandex Quickstart Guide to set up Terraform.
3. Downloaded and installed yandex-cli.
4. Configured Yandex Cloud Infrastructure.
5. Created VM instances, and generated SSH keys.
5. Configured the necessary resources.

### Used Commands :
- yc cli configurations:
- `yc config set service-account-key key.json` 
- `yc config set cloud-id <cloud_ID>`
- `yc config set folder-id <folder_ID>`
- `yc config profile create <profile_name>`

- create auth key for service account in Yandex Cloud
```bash
  yc iam key create \
  --service-account-id <service_account_ID> \
  --folder-name <service_account_folder_name> \
  --output key.json
```
- `yc compute image list`- available vm images
- `yc compute zone list`- available cloud zones
- `yc vpc subnet list`- subnet
- `yc vpc network list`- network list
- `terraform init`
- `terraform plan`
- `terraform apply -auto-approve`

### Challenges
- Encountered issues with authentication.
- Encountered issues with VM creation and management. 
- Non clear documentation on some points.
- Specific provider version requirement.
- Solution : Solved issues by reading forums, searching documentation, and trying multiple approaches, and configurations.

## GitHub infrastructure

### Setup and configuration

1. **Provider setup**
```hcl
terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}
provider "github" {
  token = var.github_token       
}
```

2. **Authentication**
   - Created GitHub Personal Access Token (PAT)
   - Gave necessary permissions to PAT for Terraform to manage GitHub resources
   - Token is stored as environment variable.

3. **Repository configuration and protection rules**

```hcl
resource "github_repository" "core_course_labs" {
  name           = "S25-core-course-labs"
  description    = "Repository for core DevOps course labs"
  visibility     = "public"

  has_issues    = true
  has_wiki      = true
  has_projects  = true
  has_downloads = true  
  
  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
}

resource "github_branch_default" "master" {
  repository     = github_repository.core_course_labs.name
  branch         = "master"
}

resource "github_branch_protection" "default" {
  repository_id  = github_repository.core_course_labs.node_id
  pattern = github_branch_default.master.branch
  enforce_admins = true

  required_status_checks {
    strict   = true
    contexts = []
  }
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
```
4. **Importing resources**

```hcl
   terraform import "github_repository.core_course_labs" "S25-core-course-labs"
```

5. **Planning and applying**
```bash
terraform plan -var="github_token=YOUR_GITHUB_TOKEN"
terraform apply -var="github_token=YOUR_GITHUB_TOKEN"
```

### Best Practices
- applied environment variables to hide sensitive and important information.
- Gave the bare minimum of privilege for GitHub PAT token permissions.
- Applied branch protection rules.
- Required pull request reviews.
- Modular structure configurations.
- proper folder structure.
- proper naming conventions.
- proper documentation.
- implented state locking.