# terraform show
## Docker
```<docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "python",
    ]
    env                                         = []
    hostname                                    = "d70b99905c4b"
    id                                          = "d70b99905c4b8e4690283b1803995d715265d9af536f4cf590efc83fc508a311"
    image                                       = "sha256:e851ea3a6b34e7d73ac264a89c9af05f4137eee22ae7521b2641804d9e22c627"
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
    stop_signal                                 = null
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "docker-user"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:e851ea3a6b34e7d73ac264a89c9af05f4137eee22ae7521b2641804d9e22c627mirgasimovk/python-msk:latest"
    image_id     = "sha256:e851ea3a6b34e7d73ac264a89c9af05f4137eee22ae7521b2641804d9e22c627"
    keep_locally = false
    name         = "mirgasimovk/python-msk:latest"
    repo_digest  = "mirgasimovk/python-msk@sha256:3fd3c198220632bbc356db05af23252fe5bdc6652c7a61b036d7ed7701313e5e"
}
```

---

```
terraform state list
docker_container.app
docker_image.app
```

-------------------------

```
terraform output
container_id = "060a638a8e11aea7ef1de4a407acac32b6508a84d3f4a6d914425d63e9670941"
image_id = "sha256:e851ea3a6b34e7d73ac264a89c9af05f4137eee22ae7521b2641804d9e22c627mirgasimovk/python-msk:latest"
```
# Best practices applied
- Using enviroment variables for sensitive data and just for convenience
- Using `terraform fmt`, `terraform validate` to see if .tf file has problems and fix issues if any
- Enable branch protection (related to GitHub process)