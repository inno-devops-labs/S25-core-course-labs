# Infrastructure as Code Lab

## Docker infrastructure using Terraform

### Terraform state show

Command:

```bash
terraform state show
```

Output:

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
    hostname                                    = "257d251cccf5"
    id                                          = "257d251cccf5c9d14ed22ce58f2134c82c91d130630ceeb90a69f1b44077f59b"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
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

### Terraform state list

Command:

```bash
terraform state list
```

Output:

```bash
docker_container.nginx
docker_image.nginx
```

### Terraform apply

Command:

```bash
terraform apply
```

Output:

```bash
Terraform used the selected providers to generate the following execution plan. Resource
actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "tutorial"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 23s [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=257d251cccf5c9d14ed22ce58f2134c82c91d130630ceeb90a69f1b44077f59b]
```

### Terraform output

Command:

```bash
terraform output
```

Output:

```bash
container_id = "<container_id>"
image_id = "<image_id>"
```

## **Yandex Cloud Infrastructure Using Terraform**

### **1. Prepare Yandex Cloud Environment**

- **Sign up** for Yandex Cloud: [console.cloud.yandex](https://console.cloud.yandex.com/)
- **Create a Cloud and Folder** using the Yandex Cloud Console.
- **Ensure a billing account is active.**

### **1. Install Yandex Cloud CLI**

To begin, I install the Yandex Cloud CLI by running:

```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```

### **3. Configure Yandex Cloud Authentication**

#### **Install Yandex CLI**

```bash
curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
yc init
```

#### **Create a Service Account**

```bash
yc iam service-account create --name terraform-sa
```

#### **Assign Required Roles**

```bash
yc resource-manager folder add-access-binding <folder_id> \
  --role <role> \
  --subject serviceAccount:<service_account_id>
```

### **Set Environment Variables**

```bash
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
export YC_SERVICE_ACCOUNT_ID=$(yc iam service-account list --format json | jq -r '.[0].id')
```

## **4. Configure Terraform**

I write main.tf file according to guide.

## **5. Run Terraform**

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

## Challenges encountered & solutions

### **Determining which roles to assign**

- Initially, I was unsure which roles were required for Terraform to work correctly with Yandex Cloud.
- **Solution:** I researched Yandex Cloud IAM roles and assigned the following:
  - `editor` for general management
  - `vpc.privateAdmin` for network operations
  - `compute.admin` for managing VM instances

### **Incorrect image ID for VM**

- **Problem:** My VM creation failed because the image ID was incorrect.
- **Solution:** I ran the following command to get the correct **image ID** for Ubuntu:

  ```bash
  yc compute image list --folder-id standard-images
  ```

### **Finding the correct subnet ID**

- **Problem:** The Terraform configuration required a subnet ID, which I didn’t have.
- **Solution:** I listed available subnets using:

  ```bash
  yc vpc subnet list
  ```
  
## Best practices for Terraform in GitHub infrastructure

### Use environment variables for secrets

- Store sensitive tokens like `GITHUB_TOKEN` as environment variables, **not** in `.tf` files.
- Example: `export GITHUB_TOKEN="your_token_here"`

### Use the `terraform import` command for existing repositories

- Avoid creating a duplicate repository if one already exists.
- Use `terraform import github_repository.<resource_name> <repo_name>`.

### Keep terraform code in a separate repository or directory

- Use a dedicated **Terraform repository** or a `github-terraform/` directory to **separate code infrastructure from project code**.

### Use `.gitignore` to exclude sensitive files

- Add `.terraform/` and `.terraform.tfstate` to `.gitignore` to avoid committing Terraform state files.

### **Always run `terraform plan` before `apply`**

- Helps preview infrastructure changes before execution.
- Example:

  ```bash
  terraform plan
  terraform apply -auto-approve
  ```
