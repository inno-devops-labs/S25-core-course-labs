# docker_container.flask_app

resource "docker_container" "flask_app" {

    attach                                      = false
    bridge                                      = ^[[90mnull^[[0m^[[0m
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = ^[[90mnull^[[0m^[[0m
    cpu_shares                                  = 0
    domainname                                  = ^[[90mnull^[[0m^[[0m
    entrypoint                                  = [
        "python",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "42c967f8badd"
    id                                          = "42c967f8badd6f3630c2a4d8543737533271a9a0da0278ae250a088db5a5607b"
    image                                       = "sha256:dafe849347074a616f6067b41edec5514821becf41fa1e52f95e928fad97d8ca"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "running_container"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ^[[90mnull^[[0m^[[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ^[[90mnull^[[0m^[[0m
            mac_address               = "02:42:ac:11:00:03"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = ^[[90mnull^[[0m^[[0m
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
    stop_signal                                 = ^[[90mnull^[[0m^[[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "appuser"
    userns_mode                                 = ^[[90mnull^[[0m^[[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }}

# docker_image.my_image

    resource "docker_image" "my_image" {
    id           = "sha256:dafe849347074a616f6067b41edec5514821becf41fa1e52f95e928fad97d8camatveyplat/flask-app:latest"
    image_id     = "sha256:dafe849347074a616f6067b41edec5514821becf41fa1e52f95e928fad97d8ca"
    keep_locally = false
    name         = "matveyplat/flask-app:latest"
    repo_digest  = "matveyplat/flask-app@sha256:c62b6f2e26be381ab1b3d4affdc312226fc297323883b314cd7e6bd4a83d106d" }

# terraform state list

docker_container.flask_app
docker_image.my_image

# terraform output

container_id = "c1f1e1856ba932d67ab10f5c9488ba09f467b64829d8fe275d724a0424ecd916"

image_id = "sha256\:dafe849347074a616f6067b41edec5514821becf41fa1e52f95e928fad97d8camatveyplat/flask-app\:latest"

# Yandex Cloud setup

## I followed these steps for setup

1. Create an Account on Yandex Cloud

2. Install and Configure Yandex CLI

3. Create main.tf file  for a free VM in yandex/ folder

# Terraform best practices

## Use Environment Variables

- Sensitive information, like the GitHub token, is stored in environment variables instead of hardcoding them in the configuration files.
- Example: `export GITHUB_TOKEN="your_github_token"`

## Use Version Control

- Check my Terraform files but keep sensitive information out of version control.

## Regular State Backup

- Regularly backup my Terraform state files to prevent data loss.
