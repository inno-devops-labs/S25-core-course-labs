# Task 1

1. **terraform state list**

```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
```

2. **terraform show**

```bash
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
    hostname                                    = "312a6e3c7d93"
    id                                          = "312a6e3c7d93dd37dbaaf48da2c0bda19bfc3791094cdf538c66b524235f86bf"
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
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}

```

3 .**output of the `terraform output`**

```bash
$terraform output
container_id = "625c4bfcffb864b43553f0b950219ee5530ac0142f0860b8c43031d80a9a8e55"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_status = "sha256:0273b5126ef6c39b678e6b7714a4d9e6532a16906d69db73eea132bda289c836decafattic/moscow-time-app:latest"
```

## Task 2

## Terraform GitHub Infrastructure

## Best Practices Applied

- **GitHub Token stored as an environment variable (`TF_VAR_github_token`)**
- **Branch protection rules added for security**
- **Automatic repository management using Terraform**
- **Existing repository imported instead of creating a new one**

## Terraform Commands Used

```sh
terraform init
terraform import github_repository.s25_core_course_labs Damncaf-goin-crazy/S25-core-course-labs
terraform apply -auto-approve
terraform state list
terraform state show github_repository.s25_core_course_labs



