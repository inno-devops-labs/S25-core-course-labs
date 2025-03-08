TERRAFORM BEST PRACTICES:
Use of Input Variables:
Defined variables to make configurations flexible and reusable.

Defining Outputs:
Added output blocks to expose key resource attributes helping in verification and integration with other tools.

Step-by-Step Deployment:
Followed the proper sequence of terraform init, terraform plan, and terraform apply to ensure controlled and reviewable changes.

```bash
terraform state show docker_container.nginx
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
    hostname                                    = "db7226e8f6f9"
    id                                          = "db7226e8f6f9a5f1a282706e1e12063e60b83f5fec450effe69539ee11673fd0"
    image                                       = "sha256:92b11f67642b62bbb98e7e49169c346b30e20cd3c1c034d31087e46924b9312e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "var.docker_image_name"
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


terraform state list
docker_container.nginx
docker_image.nginx
meowal@meowal-1-2:~/S25-core-course-labs/terraform/docker-project$ 


terraform output
image_id = "sha256:92b11f67642b62bbb98e7e49169c346b30e20cd3c1c034d31087e46924b9312enginx:latest"
nginx_container_id = "826cc47bb765f52b1b05aec22a825618b8b23308776ac77e7c5b3b59d35dc439"
nginx_container_name = "var.docker_image_name"

```

YANDEX CLOUD
1. created a Yandex Cloud account
2. created a default folder
3. added my account and gave it all roles 
4. installed 
```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
Downloading yc 0.142.0
```
inicialized 
```bash
yc init
```
token: y0__xCG2u***ravnvBw
cloud-id: b1g***95lj9n
folder-id: b1g**aovvg9
compute-default-zone: ru-central1-a
5. aploaded ubuntu img to yandex cloud to select it in main.tf
6. applied configuration

Challenges encoutered
1. connection issues even with vpn from time to time

Best practices applied
1. used terraform.tfvars for sencitive variables
2. no hardcoded credentials
