# Terraform

## ✅ Best Practices

TODO

## 🐳 Docker

### `terraform state list`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform state list
docker_container.go_webapp_container
docker_container.python_webapp_container
```

</details>

### `terraform state show`

<details>
<summary>Open output for <code>go_webapp_container</code></summary>

```cmd
terraform\docker> terraform state show "docker_container.go_webapp_container"
# docker_container.go_webapp_container:
resource "docker_container" "go_webapp_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "./main",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bca5ec05c65b"
    id                                          = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5"
    image                                       = "sha256:6d0d98f28c37ef4532818791d4ab3dbfff3c1a44ef5ec659a0049e0c2d0902da"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "simple-go-web-app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:03"
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
    user                                        = "65532"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8889
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

</details>

<details>
<summary>Open output for <code>python_webapp_container</code></summary>

```cmd
terraform\docker> terraform state show "docker_container.python_webapp_container"
# docker_container.python_webapp_container:
resource "docker_container" "python_webapp_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "python3",
        "-m",
        "uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    env                                         = []
    hostname                                    = "086c159c3c0f"
    id                                          = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd"
    image                                       = "sha256:59ec04c580e02fa680d711283a4453ed3ef952efcf2254349b6f0b3642bf164d"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "simple-python-web-app"
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
    user                                        = "65532"
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

### `terraform apply`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform apply
docker_container.go_webapp_container: Refreshing state... [id=bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5]
docker_container.python_webapp_container: Refreshing state... [id=086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.go_webapp_container must be replaced
-/+ resource "docker_container" "go_webapp_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "./main",
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
      ~ hostname                                    = "bca5ec05c65b" -> (known after apply)
      ~ id                                          = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5" -> (known after apply)
      ~ image                                       = "sha256:6d0d98f28c37ef4532818791d4ab3dbfff3c1a44ef5ec659a0049e0c2d0902da" -> "magicwinnie/simple-go-web-app-distroless:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "simple-go-web-app"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.3"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:03"
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
      - user                                        = "65532" -> null
      - working_dir                                 = "/app" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

  # docker_container.python_webapp_container must be replaced
-/+ resource "docker_container" "python_webapp_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python3",
          - "-m",
          - "uvicorn",
          - "src.main:app",
          - "--host",
          - "0.0.0.0",
          - "--port",
          - "8000",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "086c159c3c0f" -> (known after apply)
      ~ id                                          = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd" -> (known after apply)
      ~ image                                       = "sha256:59ec04c580e02fa680d711283a4453ed3ef952efcf2254349b6f0b3642bf164d" -> "magicwinnie/simple-python-web-app-distroless:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "simple-python-web-app"
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
      - user                                        = "65532" -> null
      - working_dir                                 = "/app" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ go_webapp_container_id        = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5" -> (known after apply)
  ~ python_webapp_container_id    = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.python_webapp_container: Destroying... [id=086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd]
docker_container.go_webapp_container: Destroying... [id=bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5]
docker_container.python_webapp_container: Destruction complete after 1s
docker_container.python_webapp_container: Creating...
docker_container.go_webapp_container: Destruction complete after 1s
docker_container.go_webapp_container: Creating...
docker_container.python_webapp_container: Creation complete after 1s [id=9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879]
docker_container.go_webapp_container: Creation complete after 1s [id=4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

go_webapp_container_id = "4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496"
go_webapp_container_ports = tolist([
  {
    "external" = 8889
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_webapp_container_id = "9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879"
python_webapp_container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

### `terraform output`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform output
go_webapp_container_id = "4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496"
go_webapp_container_ports = tolist([
  {
    "external" = 8889
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_webapp_container_id = "9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879"
python_webapp_container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

## ☁️ Yandex Cloud

TODO

## 👾 Github

TODO

## 🤝 Github Teams

TOOD
