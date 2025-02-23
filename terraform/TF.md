# Terraform IaC report

## Task 1

### Docker Infrastructure

#### Log of the `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.python_app will be created
  + resource "docker_container" "python_app" {
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
      + name                                        = "python_app_container"
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
          + external = 8000
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.python_app will be created
  + resource "docker_image" "python_app" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "jodak628286/python_app:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

...

docker_image.python_app: Creating...
docker_image.python_app: Still creating... [10s elapsed]
docker_image.python_app: Still creating... [20s elapsed]
docker_image.python_app: Still creating... [30s elapsed]
docker_image.python_app: Still creating... [40s elapsed]
docker_image.python_app: Still creating... [50s elapsed]
docker_image.python_app: Creation complete after 52s [id=sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26bjodak628286/python_app:latest]
docker_container.python_app: Creating...
docker_container.python_app: Creation complete after 1s [id=bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc]
```

#### `terraform list`

```
docker_container.python_app
docker_image.python_app
```

#### `terraform show docker_container.python_app`

```
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bd6c6b52e60f"
    id                                          = "bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc"
    image                                       = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "worker"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### `terraform state show docker_image.python_app`

```
# docker_image.python_app:
resource "docker_image" "python_app" {
    id           = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26bjodak628286/python_app:latest"
    image_id     = "sha256:f79a65f431da5ffcb6d2f3c75a6debcc924998203a8f5d9142ce3956199bf26b"
    keep_locally = false
    name         = "jodak628286/python_app:latest"
    repo_digest  = "jodak628286/python_app@sha256:7089417a597644fc61d7bf9a7438ea9b76d023aee7d9d0486ee1ed8669059c50"
}
```

#### `terraform apply -var="container_name=python_app_var_name"`

```
...

docker_container.python_app: Destroying... [id=bd6c6b52e60fca2d171d0d84a175be487906a467cccdd87d12bc0420998366cc]
docker_container.python_app: Destruction complete after 0s
docker_container.python_app: Creating...
docker_container.python_app: Creation complete after 1s [id=25492da2aec93eef00ba2b2ffeb0740364f7e0fbeacee3269883126c4ae3fcea]
```

```
docker ps -a
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS                      PORTS                    NAMES
25492da2aec9   f79a65f431da                 "python app.py"          3 seconds ago   Up 3 seconds                0.0.0.0:8000->8080/tcp   python_app_var_name
```

#### `terraform output`

```
python_app_container_exposed_port = 8000
python_app_container_name = "python_app_container"
python_app_image_name = "jodak628286/python_app:latest"
```

### Yandex Cloud infrastructure

#### Setup

First, creating service account (I removed ids as in docs):

```
`--> yc iam service-account create --name terraform-sa

done (1s)
id: *********
folder_id: *********
created_at: "2025-02-14T21:53:31.791971343Z"
name: terraform-sa
```

Adding roles:

```
`--> yc resource-manager folder add-access-binding ********* --role admin --subject serviceAccount*********
done (3s)
effective_deltas:
  - action: ADD
    access_binding:
      role_id: admin
      subject:
        id: *********
        type: serviceAccount
```

Obtaining keys:

```
|--> yc iam key create \
|-> --service-account-id ********* \
|-> --folder-id ********* \
`-> --output key.json
id: *********
service_account_id: *********
created_at: "2025-02-14T22:22:29.411478552Z"
key_algorithm: RSA_2048
```

Configuring profile:

```
`--> yc config profile create terraform-sa
Profile 'terraform-sa' created and activated
.-(~/projects/S25-DevOps-labs/terraform/yandex)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------(artyom@laptop)-
`--> yc config set service-account-key key.json
.-(~/projects/S25-DevOps-labs/terraform/yandex)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------(artyom@laptop)-
`--> yc config set cloud-id *********                         
.-(~/projects/S25-DevOps-labs/terraform/yandex)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------(artyom@laptop)-
`--> yc config set folder-id *********
```

Adding env variables:

```
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
```

Setting up provider by modifying `~/.terraformrc`

```
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

### Planning and creating resources

```
`--> terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.ya_vm_disk_1 will be created
  + resource "yandex_compute_disk" "ya_vm_disk_1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd85hkli5dp6as39ali4"
      + name        = "app_vm-disk1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.ya_vm will be created
  + resource "yandex_compute_instance" "ya_vm" {
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
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAbugPOKUoAE6DMj4+7VO7WEKslem9gpGasaG+Tivd+b avshapos@gmail.com
            EOT
        }
      + name                      = "app_vm"
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

          + initialize_params (known after apply)
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

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address = (known after apply)
  + internal_ip_address = (known after apply)
```

```
`--> terraform apply

...


yandex_vpc_network.network-1: Creating...
yandex_compute_disk.ya_vm_disk_1: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enpr0dmkiihbsgjjamqb]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bf74e4viv3ieannru9]
yandex_compute_disk.ya_vm_disk_1: Still creating... [10s elapsed]
yandex_compute_disk.ya_vm_disk_1: Creation complete after 12s [id=fhms1vrfuncd3acjre6q]
yandex_compute_instance.ya_vm: Creating...
yandex_compute_instance.ya_vm: Still creating... [10s elapsed]
yandex_compute_instance.ya_vm: Still creating... [20s elapsed]
yandex_compute_instance.ya_vm: Still creating... [30s elapsed]
yandex_compute_instance.ya_vm: Still creating... [40s elapsed]
yandex_compute_instance.ya_vm: Creation complete after 43s [id=fhmkn8s6sd1g4bo914j6]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address = "51.250.13.236"
internal_ip_address = "192.168.10.21"
```

```

`--> yc compute instances list
+----------------------+--------+---------------+---------+----------------+---------------+
|          ID          |  NAME  |    ZONE ID    | STATUS  |  EXTERNAL IP   |  INTERNAL IP  |
+----------------------+--------+---------------+---------+----------------+---------------+
| fhmkn8s6sd1g4bo914j6 | app_vm | ru-central1-a | RUNNING | 51.250.13.236  | 192.168.10.21 |
+----------------------+--------+---------------+---------+----------------+---------------+
```

