# TF
## Docker
### Command ```terraform state show```

resource "docker_image" "db" :
```
terraform state show docker_image.db
# docker_image.db:
resource "docker_image" "db" {
    id          = "sha256:2b859916b2379745fefaef854f0ad561264a24f5d62f7bd34d9069d5b3ddd2e7jmartynova123/dev-lab3-db:latest"
    image_id    = "sha256:2b859916b2379745fefaef854f0ad561264a24f5d62f7bd34d9069d5b3ddd2e7"
    name        = "jmartynova123/dev-lab3-db:latest"
    repo_digest = "jmartynova123/dev-lab3-db@sha256:2b859916b2379745fefaef854f0ad561264a24f5d62f7bd34d9069d5b3ddd2e7"
}
```
resource "docker_container" "db":
```
# docker_container.db:
resource "docker_container" "db" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "postgres",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "docker-entrypoint.sh",
    ]
    env                                         = (sensitive value)
    hostname                                    = "083ed46f2f06"
    id                                          = "083ed46f2f0675867f049b057dbacb589630627af41a6b154059e63e72a23cab"
    image                                       = "sha256:2b859916b2379745fefaef854f0ad561264a24f5d62f7bd34d9069d5b3ddd2e7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "db"
    network_data                                = [
        {
            gateway                   = "172.18.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.18.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "4e:39:e8:60:43:27"
            network_name              = "times-network"
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
    stop_signal                                 = "SIGINT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    healthcheck {
        interval     = "30s"
        retries      = 5
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "pg_isready -U myuser -d times",
        ]
        timeout      = "10s"
    }

    networks_advanced {
        aliases      = []
        ipv4_address = null
        ipv6_address = null
        name         = "times-network"
    }

    ports {
        external = 5432
        internal = 5432
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
resource "docker_image" "backend"
```
# docker_image.backend:
resource "docker_image" "backend" {
    id          = "sha256:2e19f594e0edbb48596d13754881998663a46cad904aa09af252a2749d37b18fjmartynova123/dev-lab3-back:latest"
    image_id    = "sha256:2e19f594e0edbb48596d13754881998663a46cad904aa09af252a2749d37b18f"
    name        = "jmartynova123/dev-lab3-back:latest"
    repo_digest = "jmartynova123/dev-lab3-back@sha256:2e19f594e0edbb48596d13754881998663a46cad904aa09af252a2749d37b18f"
}
```
resource "docker_container" "backend"
```
# docker_container.backend:
resource "docker_container" "backend" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python3",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = (sensitive value)
    hostname                                    = "ceb50827f019"
    id                                          = "ceb50827f019e25079cd38fa2960d446c044b872177fad26cf212b08c7cec1d5"
    image                                       = "sha256:2e19f594e0edbb48596d13754881998663a46cad904aa09af252a2749d37b18f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "backend"
    network_data                                = [
        {
            gateway                   = null
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = null
            ip_prefix_length          = 0
            ipv6_gateway              = null
            mac_address               = null
            network_name              = "times-network"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "unless-stopped"
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
    working_dir                                 = "/usr/local/app"

    healthcheck {
        interval     = "30s"
        retries      = 5
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "curl -f http://localhost:8080/times || exit 1",
        ]
        timeout      = "10s"
    }

    networks_advanced {
        aliases      = []
        ipv4_address = null
        ipv6_address = null
        name         = "times-network"
    }
}
```
resource "docker_image" "frontend":
```
# docker_image.frontend:
resource "docker_image" "frontend" {
    id          = "sha256:8d8a1dc4083d5efa2f627b7fbea36ea9180951a6beb88a1355e724969d707b45jmartynova123/dev-lab3-front:latest"
    image_id    = "sha256:8d8a1dc4083d5efa2f627b7fbea36ea9180951a6beb88a1355e724969d707b45"
    name        = "jmartynova123/dev-lab3-front:latest"
    repo_digest = "jmartynova123/dev-lab3-front@sha256:8d8a1dc4083d5efa2f627b7fbea36ea9180951a6beb88a1355e724969d707b45"
}
```
resource "docker_container" "frontend":
```
# docker_container.frontend:
resource "docker_container" "frontend" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "yarn",
        "start",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "ac4239d405ad"
    id                                          = "ac4239d405add9fb3f30bfca715f6cb5ba44a930143875af42523c1675924afc"
    image                                       = "sha256:8d8a1dc4083d5efa2f627b7fbea36ea9180951a6beb88a1355e724969d707b45"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "frontend"
    network_data                                = [
        {
            gateway                   = "172.18.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.18.0.4"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "fa:ce:3a:2c:dd:7d"
            network_name              = "times-network"
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
    user                                        = "myuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/usr/local/app/frontend"

    healthcheck {
        interval     = "30s"
        retries      = 5
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "curl -f http://localhost:3000 || exit 1",
        ]
        timeout      = "10s"
    }

    networks_advanced {
        aliases      = []
        ipv4_address = null
        ipv6_address = null
        name         = "times-network"
    }

    ports {
        external = 3000
        internal = 3000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
### Command ```terraform state list```

```
docker_container.db
docker_image.backend
docker_image.db
docker_image.frontend
docker_network.app_network
```
So, it means that all the containers are in work. 

## Yandex Cloud
So, I  do this to setup yandex cloud:
1. I create Yandex Cloud Account
2. I get an authetication data
3. I install CLI to manage repositories and configure the CLI profile
```
 yc iam key create \
 --service-account-id <service_account_id> \
 --folder-name <repository_name_of_service_acount> \
 --output key.json 
```
4. I create service account
```
yc config profile create <profile_name>
```
5. I set up my profile configurations:
```
yc config set service-account-key key.json
yc config set cloud-id <cloud_id>
yc config set folder-id <repository_id>
```
6. I created main.tf file in cloud directory to make new VM in my account
7. I specified the name of VM, RAM, cores, id of disk image in the variables.tf file to provide security and flexibility
10. To create the vm in my yandex cloud account I use the commands:
```
terraform init
terraform apply -var="token=mytoken"
```
## Github
### Best practicies that I applied
1. First of all I used environment variables to secure the system:
```
export TF_VAR_token = "my github-token"
```
2. I use variables.tf file to store the name and type of repository and specified the token variable as sensitive. 
3. I use terraform import to manage terraform resources
```
terraform import github_repository.repo JulyMartynova/SoftArch9
```
4. Before running I used validate practicies
```
terraform fmt #for code style
terraform validate #to check the configuration
```
6. I used destroy command for Safe CleanUp
```
terraform destroy
```









