# Terraform Documentation

## Docker Infrastructure

### Setup
```bash
terraform init
terraform fmt
terraform validate
terraform apply
```

### Command Outputs

#### 1.terraform show
```terraform
terraform show
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "d701c8cc01cd"
    id                                          = "d701c8cc01cdc99f932cea3e3b6e7c4a6266a6f3bb8750882291842976b22236"
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
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.4"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:04"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
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
    wait                                        = false
    wait_timeout                                = 60

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
#### 2.terraform state list
```terraform
terraform state list
docker_container.nginx
docker_image.nginx
```
#### 3.terraform output
```terraform
terraform output
container_id = "9e305df115139d00608cd0cec907f298d7b3265302235a7d706f41b33319ddbc"
container_name = "deedjei"
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

## Yandex Cloud Infrastructure

### Setup Process
1. Created Yandex Cloud account
2. Enabled Cloud Compute service
3. Generated IAM service account key
4. Configured Terraform provider

### Challenges Faced
1. Finding compatible free-tier image ID
2. Network configuration for public access
3. Resource availability in specific zones
4. Very uncomfortable and ugly guide

### Running terraform state list :
```terraform
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Running terraform output:
```terrafrom
external_ip_address_vm_1 = "130.193.48.225"
internal_ip_address_vm_1 = "192.168.10.3"
```