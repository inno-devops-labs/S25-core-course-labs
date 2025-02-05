# Terraform

## Table of Contents
- [Terraform](#terraform)
  - [Table of Contents](#table-of-contents)
  - [Docker](#docker)
    - [Building the infrastructure](#building-the-infrastructure)
    - [List of states](#list-of-states)
    - [Outputs](#outputs)

## Docker

### Building the infrastructure

```bash
terraform init
terraform fmt
terraform validate
terraform apply
```

`terraform apply`
<details>
<summary>output</summary>

```cmd
devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/terraform/docker$ terraform apply
docker_image.app_python: Refreshing state... [id=sha256:d8a0b68df6bb582874c17b2e62fdbb907d8a46d8b4bc86122c831ce5cfc2d73bsaleemasekrea/app_python:latest]
docker_container.app_python: Refreshing state... [id=56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python must be replaced
-/+ resource "docker_container" "app_python" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "gunicorn",
          - "app_python.app:app",
          - "--workers",
          - "4",
          - "--worker-class",
          - "uvicorn.workers.UvicornWorker",
          - "--bind",
          - "0.0.0.0:8000",
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
      ~ hostname                                    = "56f585e2bf4a" -> (known after apply)
      ~ id                                          = "56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "python-app"
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
      - user                                        = "app_user" -> null
      - working_dir                                 = "/app" -> null
        # (18 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ python-container-id    = "56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python: Destroying... [id=56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7]
docker_container.app_python: Destruction complete after 0s
docker_container.app_python: Creating...
docker_container.app_python: Creation complete after 1s [id=17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

python-container-id = "17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522"
python-container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])

```
</details>

### List of states

`terraform state list`

<details>
<summary>output<code></code></summary>

```cmd
devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/terraform/docker$ terraform state list
docker_container.app_python
docker_image.app_python
```
</details>

`terraform state show`

<details>
<summary>output</summary>

```cmd
devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/terraform/docker$ terraform state show "docker_container.app_python"
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "gunicorn",
        "app_python.app:app",
        "--workers",
        "4",
        "--worker-class",
        "uvicorn.workers.UvicornWorker",
        "--bind",
        "0.0.0.0:8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "56f585e2bf4a"
    id                                          = "56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7"
    image                                       = "sha256:d8a0b68df6bb582874c17b2e62fdbb907d8a46d8b4bc86122c831ce5cfc2d73b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-app"
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
    user                                        = "app_user"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8888
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
</details>

### Outputs
`terraform output`
<details>
<summary>output</summary>

```cmd
devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/terraform/docker$ terraform output
python-container-id = "17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522"
python-container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```
</details>