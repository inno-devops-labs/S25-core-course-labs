# Infrastructure as Code

## Docker

```sh
terraform state show
```

```sh
PS C:\Users\Adel\Desktop\devops\S25-core-course-labs\terraform\docker> C:\Users\Adel\Desktop\devops\terraform show
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python3",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "dae9cb6c83d1"
    id                                          = "dae9cb6c83d191c56cd4acf36a26ec820031d8504e8187bb667f370f875ab8ab"
    image                                       = "sha256:a8ef13c99cb18398cec9646bd4ec44a7850709fc0bbae7753858b0ea03532668"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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


Outputs:

container_id = "dae9cb6c83d191c56cd4acf36a26ec820031d8504e8187bb667f370f875ab8ab"
```

```sh
terraform state list
```

```sh
PS C:\Users\Adel\Desktop\devops\S25-core-course-labs\terraform\docker> C:\Users\Adel\Desktop\devops\terraform state list

docker_container.app_python
```

## Yandex Cloud

### 1. Setup Steps

- Created a free accout on [Yandex Cloud](https://cloud.yandex.com/)

- Get YC Credentials

- Generated an OAuth token in the YC console.

- Got `cloud_id` and `folder_id` from the YC console.

- Configure Terraform for Yandex Cloud:

- Created the following files in the `yandex_cloud` directory:

- `main.tf`: Defines the infrastructure resources (network, subnet, VM).

- `variables.tf`: Declares input variables for zone name

### 2. Configurations

- Define VM res, net and subnet in `main.tf`

- Declare local variables in `main.tf`

### 3. Challenges Encountered

Find vpn, sometimes unclear tutorial.

## 4. Execution Steps

- ```sh
    terraform init
    ```

- ```sh
    terraform plan
    ```

- ```sh
    terraform apply
    ```

- ```sh
    terraform destroy
    ```

## GitHub Terraform

```sh
terraform apply
```

Output:

```sh
PS C:\Users\Adel\Desktop\devops\S25-core-course-labs\terraform\github> C:\Users\Adel\Desktop\devops\terraform apply
var.token
  GITHUB_TOKEN

  Enter a value:

github_repository.repo: Refreshing state... [id=S25-core-course-labs-dbg]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:

- create

Terraform will perform the following actions:

\# github_branch_default.main will be created

- resource "github_branch_default" "main" {
      - branch     = "main"
      - id         = (known after apply)
      - repository = "S25-core-course-labs-dbg"
    }

  \# github_branch_protection.default will be created

  - resource "github_branch_protection" "default" {
    - allows_deletions                = false
      - allows_force_pushes             = false
      - blocks_creations                = false
      - enforce_admins                  = true
      - id                              = (known after apply)
      - pattern                         = "main"
      - repository_id                   = "S25-core-course-labs-dbg"
      - require_conversation_resolution = true
      - require_signed_commits          = false
      - required_linear_history         = false

      - required_pull_request_reviews {
        - required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=S25-core-course-labs-dbg]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDON4lpb84DjY7F]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

```
