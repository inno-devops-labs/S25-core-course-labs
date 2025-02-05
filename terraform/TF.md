# Docker Infrastructure Using Terraform

## 1. Terraform Installation

Commands for MacOS:

```bash
brew tap hashicorp/tap                             
brew install hashicorp/tap/terraform 
terraform --version
```

## 2. Terraform Initialization

```bash
terraform init
```

## 3. Applying Terraform Configuration

```bash
terraform apply -auto-approve
```

## 4. Terraform State List

```bash
terraform state list
```

#### Output of the command:

```bash
docker_container.app_container
docker_image.app_image
```

## 5. Terraform State Show

```bash
terraform state show docker_container.app_container 
```

#### Output of the command:

```bash                                                                                
# docker_container.app_container:
resource "docker_container" "app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "<hostname>"
    id                                          = "<id>"
    image                                       = "<image>"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-container"
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

## 6. Teraform Output

```bash
terraform output
```

#### Output of the command:

```bash
container_id = "<id>"
container_name = "moscow-time-container"
```

# Yandex Cloud Infrastracture Using Terraform

## 1. Install Yandex Cloud CLI

Commands fr MacOS:

```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
exec -l $SHELL
```

#### Verify Installation:

```bash
yc --version
```

#### Output of the command:

```bash
Yandex Cloud CLI 0.142.0 darwin/arm64
```

## 2. Authenticate Yandex Cloud CLI

```bash
yc init
```

#### Verify Configuration:

```bash
yc config list
```

#### Output of the command:

```bash
token: TOKEN
cloud-id: ID
folder-id: ID
compute-default-zone: ru-central1-a
```

## 3. Set Up Terraform for Yandex Cloud

Created Yandex Cloud Terraform configuration ```yandex_cloud.tf```.

## 4. Initialize and Apply Terraform

```bash
terraform init
```

```bash
terraform validate
```

#### Output of the command:

```bash
Success! The configuration is valid.
```

```bash
terraform apply -auto-approve
```

#### Output of the command:

```bash
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

vm_ip = IP
```

## 5. Connect to VM via SSH

```bash
ssh ubuntu@IP
```

# Best Practices Applied

 1. **Modularity**
    - Defined variables (```variables.tf```) to separate configuration details from logic which allows easy updates to resource parameters.
2. **Security**
    - Used environment variables to store secrets instead of hardcoding API tokens.
    - Service Account Authentication instead of personal credentials.
3. **State Management**
    - Used terraform state list and terraform state show to track resources.
    - Ensured state files are stored securely.
4. **Resource Optimization**
    - Used Yandex Free Tier VM to avoid unnecessary costs.
    - Defined CPU and RAM limits efficiently.
5. **Version Pinning**
    - Specified Terraform provider versions.

# Challenges Faced

1. **Permission Errors in Yandex Cloud**

    *Issue:* Received ```PermissionDenied``` error while applying Terraform.
    
    *Fix:* Manually granted the required IAM permissions on Yandex Cloud account.

2. **SSH Authentication Failing**

    *Issue:* Could not connect to VM via SSH.
    
    *Fix:* Manually generated rsa key pair:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "<mail>"
    ```

3. **Subnet ID Identification**

    *Issue:* Could not find the subnet id.
    
    *Fix:* Manually found the subnet id:

    ```bash
    yc vpc subnet list
    ```

4. **Image ID Identification**

    *Issue:* Could not find the image id.
    
    *Fix:* Manually found the image id:

    ```bash
    yc compute image list
    ```
