# Output of the commands:

1. > terraform state list

```bash
docker_container.nginx
docker_image.nginx
```

2. > terraform state show docker_container.nginx

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
    hostname                                    = "063e7aecb5cc"
    id                                          = "063e7aecb5ccb1be4be8e8eb83d065e6e0b4a8e0b07c6be300390e0903291428"
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

3. > terraform state show docker_image.nginx

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

4. > terraform output

```bash
container_id = "e87f8a5d2fbc7a2bf9c98c7c06a9d3872baa6dee5ee0a5afd689db660dade728"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```

# Steps of setup process I conducted for task 4 from the lab:

1. Created the authorization key

```bash
yc iam key create --service-account-id <my folder id> --folder-name default --output key.json
```

2. Created CLI profile and set a key, cloud id and folder id:

```bash
yc config profile create mangocandle
yc config set service-account-key key.json
yc config set cloud-id devopslabsinno
yc config set folder-id <my folder id>
```

3. Added authentication data to the environment variables:
   export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
   export YC_FOLDER_ID=$(yc config get folder-id)

4. Changed configuration file - added info about yandex cloud provider and added data source (look at the curent main.tf file).

5. Run the command to apply changes:

```bash
terraform plan
terraform apply
```

6. Checked the results using

```bash
terraform output
```

## The result:

```bash
container_id = "879adf930a17cf510252fae7ba9cccced9d49daf648a5d2f58919b6b8788440b"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
my_image_id = "fd8j3fo8lqh4730j2ftd"
```
