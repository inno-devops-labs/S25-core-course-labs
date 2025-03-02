```
terraform state list
```
```
Output:
docker_container.python_time_app
```

```
terraform state show docker_container.python_time_app
```
```
Output:
# docker_container.python_time_app:
resource "docker_container" "python_time_app" {
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
    hostname                                    = "6a2b1c673fa5"
    id                                          = "6a2b1c673fa53690844cfebc8ddad635a61370fa08ba99f5f5e49477f7c0ec24"
    image                                       = "sha256:3ef6bada6adba5892338485bf1df95716b5d68dfcb8a7d0f1672f4deab38bc4e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_time_app"
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
    user                                        = "appuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
terraform apply
```

```
Output:
docker_container.python_time_app: Refreshing state... [id=6a2b1c673fa53690844cfebc8ddad635a61370fa08ba99f5f5e49477f7c0ec24]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.python_time_app must be replaced
-/+ resource "docker_container" "python_time_app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "python",
          - "app.py",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "6a2b1c673fa5" -> (known after apply)
      ~ id                                          = "6a2b1c673fa53690844cfebc8ddad635a61370fa08ba99f5f5e49477f7c0ec24" -> (known after apply)
      ~ image                                       = "sha256:3ef6bada6adba5892338485bf1df95716b5d68dfcb8a7d0f1672f4deab38bc4e" -> "whatislav/moscow-time-app:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "python_time_app"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "appuser" -> null
      - working_dir                                 = "/app" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "6a2b1c673fa53690844cfebc8ddad635a61370fa08ba99f5f5e49477f7c0ec24" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.python_time_app: Destroying... [id=6a2b1c673fa53690844cfebc8ddad635a61370fa08ba99f5f5e49477f7c0ec24]
docker_container.python_time_app: Destruction complete after 0s
docker_container.python_time_app: Creating...
docker_container.python_time_app: Creation complete after 1s [id=322428bb2ba9b20552518a5c8ae87b48b6ac60791123ae8f96f9f12ca91e17b7]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "322428bb2ba9b20552518a5c8ae87b48b6ac60791123ae8f96f9f12ca91e17b7"
```

```
terraform output
```
```
Output:
container_id = "322428bb2ba9b20552518a5c8ae87b48b6ac60791123ae8f96f9f12ca91e17b7"
```



# Yandex Cloud Infrastructure with Terraform

---

## 1. Setup Steps

### 1.1 Create an Account on Yandex Cloud
1. Signed up for a free account on [Yandex Cloud](https://cloud.yandex.com/).

### 1.2 Obtain Yandex Cloud Credentials
1. Generated an OAuth token in the Yandex Cloud console under **API keys**.
2. Retrieved the `cloud_id` and `folder_id` from the Yandex Cloud console and set them to ENV.

### 1.3 Configure Terraform for Yandex Cloud
1. Created the following files in the `yandex_cloud` directory:
   - `main.tf`: Defines the infrastructure resources (network, subnet, VM).
   - `variables.tf`: Declares input variables for zone name

---

## 2. Configurations

### 2.1 `main.tf`
Defined the network, subnet, and VM resources.

### 2.2 `variables.tf`
Declared zone name.

---

## 3. Challenges Encountered

Very unclear tutorial with hidden instructions and undocumented errors.

---

## 4. Execution Steps

### 4.1 Initialize Terraform
```sh
terraform init
```

### 4.2 Plan the Infrastructure
```sh
terraform plan
```

### 4.3 Apply the Infrastructure
```sh
terraform apply
```

### 4.4 Destroyed VM
```sh
terraform destroy
```

---

# GitHub Terraform

```
terraform apply
```
```
Output:
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
  ~ update in-place

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
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      + description                 = "solutions for labs on Devops"
      + gitignore_template          = "VisualStudio"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
        name                        = "S25-core-course-labs"
        # (28 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 1s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONx_SX84DioTe]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```