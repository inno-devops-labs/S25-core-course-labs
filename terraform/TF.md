nika@nika:~/study/devops/S25-core-course-labs/terraform$ terraform apply

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





terraform state show
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





terraform state list
docker_container.nginx
docker_image.nginx


terraform output
container_id = "52fe25ff5ffe7f1a6295a931430c90baf8d916cb6f078c8186d44182bdd5e60d"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"













# **Yandex Cloud Infrastructure Using Terraform**

## **1. Install Yandex Cloud CLI**
To begin, I install the Yandex Cloud CLI by running: 
```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```


## **2. Log in to Yandex Cloud**
I authenticate my Yandex Cloud account using: 
```bash
yc init
```

## **3. Create a Service Account**
I create a service account to manage Terraform resources: 
```bash
yc iam service-account create --name terraform-sa
```

---

## **4. Assign Required Roles**
I assign the necessary roles to my service account: 
```bash
yc resource-manager folder add-access-binding <my-folder-id> \
  --role <role> --subject serviceAccount:<my-service-account-id>
```
## **5. Generate a Service Account Key**
I generate a service account key and save it to a file: 
```bash
yc iam key create --service-account-id <my-service-account-id> --output sa-key.json
```

## **6. Create a Terraform Project**
I create a new Terraform project and define the infrastructure inside `main.tf`.  
```bash
mkdir yacloud && cd yacloud
touch main.tf
```

## **7. Initialize Terraform**
Before applying my configuration, I initialize and validate Terraform: 
```bash
terraform init
terraform validate
```

## **8. Apply the Terraform Configuration**
Finally, I apply my Terraform configuration to create resources: 
```bash
terraform apply -auto-approve
```

## Challenges Encountered & Solutions**

### **Determining Which Roles to Assign**
- Initially, I was unsure which roles were required for Terraform to work correctly with Yandex Cloud.
- **Solution:** I researched Yandex Cloud IAM roles and assigned the following:
  - `editor` for general management
  - `vpc.privateAdmin` for network operations
  - `compute.admin` for managing VM instances

### **Incorrect Image ID for VM**
- **Problem:** My VM creation failed because the image ID was incorrect.
- **Solution:** I ran the following command to get the correct **image ID** for Ubuntu:
  ```bash
  yc compute image list --folder-id standard-images
  ```

### **Finding the Correct Subnet ID**
- **Problem:** The Terraform configuration required a subnet ID, which I didn’t have.
- **Solution:** I listed available subnets using:
  ```bash
  yc vpc subnet list
  ```
  
  
# Best Practices for Terraform in GitHub Infrastructure

## Use Environment Variables for Secrets
- Store sensitive tokens like `GITHUB_TOKEN` as environment variables, **not** in `.tf` files.
- Example: `export GITHUB_TOKEN="your_token_here"`

## Use the `terraform import` Command for Existing Repositories
- Avoid creating a duplicate repository if one already exists.
- Use `terraform import github_repository.<resource_name> <repo_name>`.

## Keep Terraform Code in a Separate Repository or Directory
- Use a dedicated **Terraform repository** or a `github-terraform/` directory to **separate code infrastructure from project code**.

## Use `.gitignore` to Exclude Sensitive Files
- Add `.terraform/` and `.terraform.tfstate` to `.gitignore` to avoid committing Terraform state files.

## **Always Run `terraform plan` Before `apply`**  
- Helps preview infrastructure changes before execution. 
- Example: 
  ```bash
  terraform plan
  terraform apply -auto-approve
  ```

