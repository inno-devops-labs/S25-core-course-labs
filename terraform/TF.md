# Terraform

## Creating the Container

**Command:**

```sh
  terraform state list
```

**Output:**

```sh
  docker_container.app_python
```

**Command:**

 ```sh
  terraform state show docker_container.app_python
```

**Output:**

```sh
  # docker_container.app_python:
  resource "docker_container" "app_python" {
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
      hostname                                    = "96c015fe133f"
      id                                          = "96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508"
      image                                       = "sha256:de4f047721fee1e47ab5a3be2dc3236d4e5104060db786b2b6a5c16ad7620840"
      init                                        = false
      ipc_mode                                    = "private"
      log_driver                                  = "json-file"
      logs                                        = false
      max_retry_count                             = 0
      memory                                      = 0
      memory_swap                                 = 0
      must_run                                    = true
      name                                        = "app_python_container"
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
      working_dir                                 = "/home/appuser"

      ports {
          external = 8000
          internal = 80
          ip       = "0.0.0.0"
          protocol = "tcp"
      }
  } 
```

## Changing the Port Number

```sh
  docker_container.app_python: Refreshing state... [id=96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508]

  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
  following symbols:
  -/+ destroy and then create replacement

  Terraform will perform the following actions:

    # docker_container.app_python must be replaced
  -/+ resource "docker_container" "app_python" {
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
        ~ hostname                                    = "96c015fe133f" -> (known after apply)
        ~ id                                          = "96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508" -> (known after apply)
        ~ image                                       = "sha256:de4f047721fee1e47ab5a3be2dc3236d4e5104060db786b2b6a5c16ad7620840" -> "anyarylova/app_python" # forces replacement
        ~ init                                        = false -> (known after apply)
        ~ ipc_mode                                    = "private" -> (known after apply)
        ~ log_driver                                  = "json-file" -> (known after apply)
        - log_opts                                    = {} -> null
        - max_retry_count                             = 0 -> null
        - memory                                      = 0 -> null
        - memory_swap                                 = 0 -> null
          name                                        = "app_python_container"
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
        - working_dir                                 = "/home/appuser" -> null
          # (17 unchanged attributes hidden)

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

  docker_container.app_python: Destroying... [id=96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508]
  docker_container.app_python: Destruction complete after 1s
  docker_container.app_python: Creating...
  docker_container.app_python: Creation complete after 0s [id=afd45f1fea4de5c76c690072420c9ccbbc80d816a0d58fdfdbe26ec3d2460c80]

  Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Output

```sh
  terraform output
```

```sh
  container_id = "588bfa1adc84b770c096b5f37bbce3964de2eb924a6751962a7a1d917e9dbeed"
  image_id = "anyarylova/app_python"
```
