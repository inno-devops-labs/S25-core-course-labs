## `terraform init`:

```
Initializing the backend...
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (self-signed, key ID BD080C4571C6104C)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

## `terraform apply`:

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.time_app_py will be created
  + resource "docker_container" "time_app_py" {
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
      + image                                       = "unileonid/time-app-py"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "unileonid_time_app_py"
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
          + external = 80
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + time_app_py_container_id    = (known after apply)
  + time_app_py_container_image = "unileonid/time-app-py"
  + time_app_py_container_name  = "unileonid_time_app_py"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.time_app_py: Creating...
docker_container.time_app_py: Creation complete after 0s [id=cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

time_app_py_container_id = "cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd"
time_app_py_container_image = "unileonid/time-app-py"
time_app_py_container_name = "unileonid_time_app_py"
```

## `terraform state list`:

```
docker_container.time_app_py
```

## `terraform state show "docker_container.time_app_py"`:

```
# docker_container.time_app_py:
resource "docker_container" "time_app_py" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "sh",
        "-c",
        "python app_start.py -t \"${APP_TIMEZONE}\"",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "dc821dbcc3df"
    id                                          = "dc821dbcc3dfd4a74a7e9ef1a0e5b2c93fdecc2b676676aeb17c7cb424eff66f"
    image                                       = "sha256:cb7e6d9ad19509ad71a2d03e0c37d531308f8d5db277e4409c14477c128c7574"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "unileonid_time_app_py"
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
    user                                        = "app"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 80
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## `terraform output`:

```
time_app_py_container_id = "cbef0d2f8a1017c61461a3baf84b72f5e34d0913eea98b2883aaf9d94bb8a5cd"
time_app_py_container_image = "unileonid/time-app-py"
time_app_py_container_name = "unileonid_time_app_py"
```
