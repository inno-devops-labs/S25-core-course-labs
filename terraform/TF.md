## Terraform

Commands outputs:
- `terraform show`
```
        $ terraform show
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
            hostname                                    = "b94d8e21c785"
            id                                          = "b94d8e21c78561f1c50678076eb05d2d767e6022ee54f5689c57d84441dfb88b"
            image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            init                                        = false
            ipc_mode                                    = "private"
            log_driver                                  = "json-file"
            logs                                        = false
            max_retry_count                             = 0
            memory                                      = 0
            memory_swap                                 = 0
            must_run                                    = true
            name                                        = "tutorial"
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
                external = 8000
                internal = 80
                ip       = "0.0.0.0"
                protocol = "tcp"
            }
        }

        # docker_image.nginx:
        resource "docker_image" "nginx" {
            id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
            image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            keep_locally = false
            name         = "nginx:latest"
            repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
        }
```
        
    
- `terraform state list`
```
        $ terraform state list
        docker_container.nginx
        docker_image.nginx
```
- `terraform state show docker_container.nginx`
```
        $ terraform state show docker_container.nginx
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
            hostname                                    = "a600411b43fa"
            id                                          = "a600411b43faf367befb2a05e4a176e44f8dbf7064c2c593b0a73c0f08e84ea1"
            image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            init                                        = false
            ipc_mode                                    = "private"
            log_driver                                  = "json-file"
            logs                                        = false
            max_retry_count                             = 0
            memory                                      = 0
            memory_swap                                 = 0
            must_run                                    = true
            name                                        = "tutorial"
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
                external = 8000
                internal = 80
                ip       = "0.0.0.0"
                protocol = "tcp"
            }
        }
```
- `terraform state show docker_image.nginx`
```
        $ terraform state show docker_image.nginx
        # docker_image.nginx:
        resource "docker_image" "nginx" {
            id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
            image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            keep_locally = false
            name         = "nginx:latest"
            repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
        }
```
## Changes

```
$ sudo terraform apply
docker_image.nginx: Refreshing state... [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_container.nginx: Refreshing state... [id=b553078798c82e6b6f78e92523c3ab098515f2977f1ca587ede461b18e4558df]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
-/+ destroy and then create replacement

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
      ~ hostname                                    = "b553078798c8" -> (known after apply)
      ~ id                                          = "b553078798c82e6b6f78e92523c3ab098515f2977f1ca587ede461b18e4558df" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
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
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=b553078798c82e6b6f78e92523c3ab098515f2977f1ca587ede461b18e4558df]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=ba3545c857a6f08a48ae9aeb1d011e4fdda33ca87c9099cdd5c7b23fdb84909d]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

After changing
```
$ terraform show
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
    hostname                                    = "ba3545c857a6"
    id                                          = "ba3545c857a6f08a48ae9aeb1d011e4fdda33ca87c9099cdd5c7b23fdb84909d"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```
## Destroy

```
$ sudo terraform destroy
docker_image.nginx: Refreshing state... [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_container.nginx: Refreshing state... [id=ba3545c857a6f08a48ae9aeb1d011e4fdda33ca87c9099cdd5c7b23fdb84909d]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  - destroy

Terraform will perform the following actions:

  # docker_container.nginx will be destroyed
  - resource "docker_container" "nginx" {
      - attach                                      = false -> null
      - command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      - entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> null
      - env                                         = [] -> null
      - group_add                                   = [] -> null
      - hostname                                    = "ba3545c857a6" -> null
      - id                                          = "ba3545c857a6f08a48ae9aeb1d011e4fdda33ca87c9099cdd5c7b23fdb84909d" -> null
      - image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e" -> null
      - init                                        = false -> null
      - ipc_mode                                    = "private" -> null
      - log_driver                                  = "json-file" -> null
      - log_opts                                    = {} -> null
      - logs                                        = false -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      - must_run                                    = true -> null
      - name                                        = "tutorial" -> null
      - network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - network_mode                                = "bridge" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      - read_only                                   = false -> null
      - remove_volumes                              = true -> null
      - restart                                     = "no" -> null
      - rm                                          = false -> null
      - runtime                                     = "runc" -> null
      - security_opts                               = [] -> null
      - shm_size                                    = 64 -> null
      - start                                       = true -> null
      - stdin_open                                  = false -> null
      - stop_signal                                 = "SIGQUIT" -> null
      - stop_timeout                                = 0 -> null
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - tty                                         = false -> null
      - wait                                        = false -> null
      - wait_timeout                                = 60 -> null
        # (7 unchanged attributes hidden)

      - ports {
          - external = 8080 -> null
          - internal = 80 -> null
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null
        }
    }

  # docker_image.nginx will be destroyed
  - resource "docker_image" "nginx" {
      - id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest" -> null
      - image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e" -> null
      - keep_locally = false -> null
      - name         = "nginx:latest" -> null
      - repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null
    }

Plan: 0 to add, 0 to change, 2 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

docker_container.nginx: Destroying... [id=ba3545c857a6f08a48ae9aeb1d011e4fdda33ca87c9099cdd5c7b23fdb84909d]
docker_container.nginx: Destruction complete after 0s
docker_image.nginx: Destroying... [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_image.nginx: Destruction complete after 0s

Destroy complete! Resources: 2 destroyed.
```

## Renamin with variable

```
$ sudo terraform apply -var "container_name=RenamedContainer"
docker_image.nginx: Refreshing state... [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_container.nginx: Refreshing state... [id=f63fd6b29b23ce8d5e19d44bd611865c21b50d54507cc665283593defd54fc0e]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
-/+ destroy and then create replacement

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
      ~ hostname                                    = "f63fd6b29b23" -> (known after apply)
      ~ id                                          = "f63fd6b29b23ce8d5e19d44bd611865c21b50d54507cc665283593defd54fc0e" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "DefaultValue" -> "RenamedContainer" # forces replacement
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
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=f63fd6b29b23ce8d5e19d44bd611865c21b50d54507cc665283593defd54fc0e]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=30701d8018c39702bd062eb8ba47ee18555114b3b1d6c61e32e864089f56f209]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Outpust

```
$ terraform output
container_id = "b4e14789a33a93afb867a7bc9a087ee44a679dab1f117f1b618f257d9ac67b54"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```
