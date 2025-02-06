## Best practices applied

1. **Code organization**
    - The code is devided into separate files (`main.tf`, `variables.tf`, and `outputs.tf`) for modularity purpouses.

2. **Security**
    - Sensitive information like tokens and passwords are not explicitly used in code.

3. **Version Control**
    - Versions of Terraform and other requirements are specified, to avoid possible conflict.


## Docker

### Outputs

<details>
<summary>Output for `terraform state show "docker_container.my_container"`</summary>

```cmd
terraform\docker> terraform state show "docker_container.my_container"
# docker_container.my_container:
resource "docker_container" "my_container" {
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
    hostname                                    = "ef57d5b7c159"
    id                                          = "ef57d5b7c1598d30607ed3a353b6de0b9e887f8c19362f76ce0922b33b4f77ca"
    image                                       = "sha256:08cf57906fd5ee7249306429874745f4bdd8e8c39704f2a7fe5aed1d732f6573"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
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
    user                                        = "appuser"
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
</details>


<details>
<summary>Output for `terraform state list "docker_container.my_container"`</summary>

```cmd
terraform\docker> terraform state list "docker_container.my_container"
docker_container.my_container
```
</details>


## Yandex Cloud 

To create terraform for Yandex, I followed [this Yandex Quickstart Guide](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1). I had some issues regarding tokens and setting up a service account, so I used my own. Installing Terraform as well as Yandex Cloud CLI was simple and fast. I created the needed files according to the guide and made some changes later.