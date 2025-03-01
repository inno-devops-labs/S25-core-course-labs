### Output for the command ```terraform state list```
```bash
docker_container.nginx
docker_image.nginx
```

### Output for the command ```terraform state show docker_container.nginx```
```bash
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
    hostname                                    = "ab8bf7edeb0d"
    id                                          = "ab8bf7edeb0de050d9226f9c9e71e8629d045387d63a009d7652eec0d97f6d22"
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

### Output for the command ```terraform state show docker_image.nginx```
```bash 
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```

### Output for the command ```terraform output```

```bash
container_id = "5aea7b91d6e4d40e2986d7c38c014f4e9f11698fa18f804a3572dce22ab53564"
container_name = "tutorial"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 80
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
```

### Best practices have been applied 

- Avoid Hardcoding Secrets: Use environment variables and secrets   
- Use Version Constraints for Providers: Specify version constraints for providers to ensure compatibility and avoid unexpected behavior.  
- Separate Variables and Logic: Keep variables in a separate file (e.g., `variables.tf`) for better modularity and maintainability.  
- Validate and Plan Before Applying: Always run `terraform validate` and `terraform plan` before applying changes.  
- Use Environment Variables for Sensitive Data
- Enforce Branch Protection Rules: Configure branch protection rules to enforce code quality and collaboration standards.  
