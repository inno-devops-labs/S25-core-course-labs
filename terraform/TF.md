# Terraform State Report

## Terraform State List
```
docker_container.nginx
docker_image.nginx
```

## Terraform State Show: docker_container.nginx
```
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
    hostname                                    = "a9bc4f5d5a54"
    id                                          = "a9bc4f5d5a543d5c904d31a8108d870d4482a7520f62d2cf0ee88260fd9896a2"
    image                                       = "sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
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

## Terraform State Show: docker_image.nginx
```
resource "docker_image" "nginx" {
    id           = "sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcefnginx:latest"
    image_id     = "sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
```

## Log of Applied Changes
```
-/+ resource "docker_container" "nginx" {
    + bridge              = (known after apply)
    ~ command             = ["nginx", "-g", "daemon off;"] -> (known after apply)
    ~ hostname            = "03d2ba8451ef" -> (known after apply)
    ~ id                  = "03d2ba8451effe7407a5f326a02a07d16aaa77dffd41d648d2c217c228b63b12" -> (known after apply)
    ~ name                = "YetAnotherName" -> "NewName"
    ~ network_mode        = "bridge" -> null
    ~ stop_signal         = "SIGQUIT" -> (known after apply)
  }
```

### **Terraform Output**
```
container_id   = "685fcaa8932509fed153fe1f7a6e3b93e6e3bf683f0947137e5e2a49a56c6021"
container_name = "NewName"
```

# Yandex Cloud Infrastructure Using Terraform

## **1. Create an Account on Yandex Cloud**
- Signed up on [Yandex Cloud](https://cloud.yandex.com/).
- Created a billing account and ensured it has `TRIAL_ACTIVE` status.
- Created a **Cloud** and a **Folder** for managing infrastructure.

## **2. Install Yandex Cloud CLI**
```sh
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
yc init
```

## **3. Configure Authentication**
- Created a **Service Account**:
  ```sh
  yc iam service-account create --name terraform-sa
  ```
- Assigned necessary roles:
  ```sh
  yc resource-manager folder add-access-binding test \
    --role admin \
    --subject serviceAccount:$(yc iam service-account get terraform-sa --format json | jq -r .id)
  ```
- Generated an authorized key:
  ```sh
  yc iam key create --service-account-id ajeg7sjap0uiikr85uj6 --output key.json
  ```
- Configured CLI to use the service account:
  ```sh
  yc config profile create terraform-profile
  yc config set service-account-key key.json
  yc config set cloud-id b1g3kfmlknmgul9ah0pi
  yc config set folder-id b1g69akcgnfq2bu85ltf
  ```

## **4. Create Terraform Configuration**
- Created `main.tf`:
  ```hcl
  terraform {
    required_providers {
      yandex = {
        source  = "yandex-cloud/yandex"
        version = "~> 0.87"
      }
    }
  }

  provider "yandex" {
    zone      = "ru-central1-a"
  }

  resource "yandex_compute_instance" "vm" {
    name = "my-yandex-vm"

    resources {
      cores  = 2
      memory = 2
    }

    boot_disk {
      initialize_params {
        image_id = "fd8qavqba6h1atobdrd8"
      }
    }

    network_interface {
      subnet_id = "e9bla69ijcg5looi3lal"
      nat       = true
    }

    metadata = {
      ssh-keys = ...
    }
  }
  
  output "vm_public_ip" {
    value = yandex_compute_instance.vm.network_interface.0.nat_ip_address
  }
  ```

## **5. Initialize Terraform and Apply Configuration**
```sh
terraform init
terraform apply -auto-approve
```

- Retrieved the VM public IP using:
```sh
terraform output
```

## **6. Destroy Resources (Cleanup)**
```sh
terraform destroy -auto-approve
```

# Terraform Best Practices for GitHub Repository Management

## 1. Specified Required Terraform and Provider Versions
- Ensures compatibility with Terraform versions `>= 1.2.0`.
- Locks the provider version to `~> 4.0`, preventing breaking changes while allowing minor updates.

## 2. Secured Provider Authentication
- Uses a variable (`var.token`) instead of hardcoding sensitive authentication tokens.
- Token value is stored in `config.auto.tfvars`, ensuring it is not exposed in source code.

## 3. Defined Variables for Configuration Flexibility
- Marks the `token` variable as sensitive, preventing it from being displayed in logs.
- Keeps repository details configurable, allowing reusability by modifying `terraform.tfvars` instead of `main.tf`.
- Prevents accidental exposure in version control by ensuring `.gitignore` excludes `config.auto.tfvars`.

## 4. Automated Repository Initialization
- Ensures the repository has issues and a wiki enabled.
- Automatically initializes the repository with a `README.md`.
- Includes a `VisualStudio`-based `.gitignore` and an `MIT` license.

## 5. Set and Protected the Default Branch
- Ensures a predefined default branch (`main`).
- Enforces branch protection:
  - Requires conversation resolution before merging.
  - Requires at least one approving review for pull requests.

## 6. Applied Infrastructure as Code (IaC) Best Practices
- Use `terraform plan` before `apply` to preview changes.

# Bonus Task: GitHub Teams Using Terraform
- Created GitHub Organization: [DevOps-test-iu](https://github.com/DevOps-test-iu)
- Extended configuration for managing teams in `github_terraform/main.tf`
- Applied changes successfully (see image below):
  ![GitHub Teams Applied](image.png)
