```commandline
terraform state show docker_container.app_python
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
    hostname                                    = "46e2c0817410"
    id                                          = "46e2c0817410c1c603a86fd3ca092c23c3cbcf02b59e10399b545870684fc8a1"
    image                                       = "sha256:469d66940a5e2d4ae489c60147753565831c1f5c7549ff4d2b311fe5ebfa49ea"
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
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

```commandline
terraform state list
docker_container.app_python
```

```commandline
 terraform output
app_python_container_id = "46e2c0817410c1c603a86fd3ca092c23c3cbcf02b59e10399b545870684fc8a1"
```