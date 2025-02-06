# Terraform configuration

After running

```bash
terraform init
terraform apply
```

the terraform created two resources - docker image and docker container as desired from *.tf* file.
`terraform state show` for the resources:

- **docker_image.msk_time**

```text
resource "docker_image" "msk_time" {
    id           = "sha256:b66dcd218a37ec60010fac2a80ea1dda7352604da38cc5f8c6031df29fcc8181absorian/s25-devops-msk-time:latest"
    image_id     = "sha256:b66dcd218a37ec60010fac2a80ea1dda7352604da38cc5f8c6031df29fcc8181"
    keep_locally = false
    name         = "absorian/s25-devops-msk-time:latest"
    repo_digest  = "absorian/s25-devops-msk-time@sha256:0e52142af26e70555c52e9711df4fcf746d32629884271e33623142d9ef6e79d"
}
```

- **docker_container.msk_time**

```text
resource "docker_container" "msk_time" {
    attach                                      = false
    bridge                                      = null
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "./entrypoint.sh",
    ]
    env                                         = [
        "APP_HOST=0.0.0.0",
        "APP_PORT=8000",
    ]
    hostname                                    = "968dad6ae52d"
    id                                          = "968dad6ae52d66b1939797d8a003618893a4750a7d0fb4437100302721c522a2"
    image                                       = "sha256:b66dcd218a37ec60010fac2a80ea1dda7352604da38cc5f8c6031df29fcc8181"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "terraform_msk_time"
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
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
