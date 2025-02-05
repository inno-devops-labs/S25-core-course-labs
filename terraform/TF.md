# Terraform 

### Best practices


## Docker

### `terraform state list`

```
docker_container.node_app
docker_container.python_app
docker_image.node_app
docker_image.python_app
```

* ### `terraform state show docker_container.python_app`

```
# docker_container.python_app:
resource "docker_container" "python_app" {
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
    hostname                                    = "8fd2f30cca87"
    id                                          = "8fd2f30cca87534eecb45529ca7da9c1480e5130384ae93f120d4c1b2d5d7c93"
    image                                       = "sha256:1f60cf72a6c610abebcceb0dc5f251d8583b9d5704b5c5e6914339cb545730d7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-msk-time"
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
    network_mode                                = "default"
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
        internal = 50
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```


* ### `terraform state show docker_container.node_app`

```
# docker_container.node_app:
resource "docker_container" "node_app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "node",
        "server.js",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/usr/bin/tini",
        "--",
    ]
    env                                         = []
    hostname                                    = "1e67ea338f77"
    id                                          = "1e67ea338f772e0821e444e2319d3816d15fcec9b9147bfa1a92e9d52ac4f272"
    image                                       = "sha256:f64483641fccde2e8c58e52b11cd1a46e1b3e75b19256b3999e408eb36ef3f79"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "js-cities-dist"
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
    network_mode                                = "default"
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
        external = 3000
        internal = 30
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

### `terraform output`

```
container_id_node = "1e67ea338f772e0821e444e2319d3816d15fcec9b9147bfa1a92e9d52ac4f272"
container_id_py = "8fd2f30cca87534eecb45529ca7da9c1480e5130384ae93f120d4c1b2d5d7c93"
image_id_node = "sha256:f64483641fccde2e8c58e52b11cd1a46e1b3e75b19256b3999e408eb36ef3f79nickolaus899/js-cities-dist:latest"
image_id_py = "sha256:1f60cf72a6c610abebcceb0dc5f251d8583b9d5704b5c5e6914339cb545730d7nickolaus899/python-msk-time:latest"
```

## Yandex Cloud
