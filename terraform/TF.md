# Terraform Tutorial Progress

## Overview
I followed a tutorial to deploy an Nginx container using Terraform and Docker. Below is a summary of the steps I completed and the outputs I received.

## Steps Completed

### 1. Checking Terraform State for the Nginx Container
After running the command:
```sh
terraform state show docker_container.nginx
```
I received the following output:
```plaintext
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
    hostname                                    = "324765fba5a2"
    id                                          = "324765fba5a22cc40a558c7be22519b2bc188beda40730e45ca8cf9ab52054b6"
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

### 2. Listing Terraform State Resources
I executed the command:
```sh
terraform state list
```
Output:
```plaintext
docker_container.nginx
docker_image.nginx
```

### 3. Checking Terraform Output
I ran the command:
```sh
terraform output
```
And received:
```plaintext
container_id = "037302449ffa9ca95bc60af75c571e68e44406c22dd96a9741a2e22476db0dcb"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
```

# Terraform Configuration for Yandex Cloud

Folder ```cloud-terraform```

## Setup Process

### Initialize Terraform
```powershell
cd cloud-terraform
PS D:\DE\Solutions\S25-core-course-labs\cloud-terraform> mv $env:APPDATA/terraform.rc $env:APPDATA/terraform.rc.old
```
Output:
```
mv : Не удается найти путь "C:\Users\Кристина\AppData\Roaming\terraform.rc", так как он не существует.
```

Continue initialization:
```powershell
terraform init
```
Output:
```
Terraform has been successfully initialized!
```

Lock providers and validate:
```powershell
terraform providers lock
terraform validate
```
Output:
```
Success! The configuration is valid.
```

Format Terraform files:
```powershell
terraform fmt
```
Formatted files:
- main.tf
- variables.tf

---

## Terraform Configuration Files

### `main.tf`
```hcl
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
}

resource "yandex_vpc_network" "default" {
  name = var.network
}

resource "yandex_vpc_subnet" "default" {
  network_id     = yandex_vpc_network.default.id
  name           = var.subnet
  v4_cidr_blocks = var.subnet_v4_cidr_blocks
  zone           = var.zone
}

data "yandex_compute_image" "default" {
  family = var.image_family
}

data "template_file" "default" {
  template = file("${path.module}/init.ps1")
  vars = {
    user_name  = var.user_name
    user_pass  = var.user_pass
    admin_pass = var.admin_pass
  }
}

resource "yandex_compute_instance" "default" {
  name     = var.name
  hostname = var.name
  zone     = var.zone

  resources {
    cores  = var.cores
    memory = var.memory
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.default.id
      size     = var.disk_size
      type     = var.disk_type
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = var.nat
  }

  metadata = {
    user-data = data.template_file.default.rendered
  }

  timeouts {
    create = var.timeout_create
    delete = var.timeout_delete
  }
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}
```

### `terraform.tfvars`
```hcl
name       = "<my_server_name>"
user_name  = "<my_user>"
user_pass  = "<my_password>"
admin_pass = "<my_password>"
```

### `init.ps1`
```powershell
#ps1
Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
"Bootstrap script started" | Write-Host

$MyUserName = "${ user_name }"
$MyPlainTextPassword = "${ user_pass }"
if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
    "Create user" | Write-Host
    $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
    $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
    $MyUser | Add-LocalGroupMember -Group 'Administrators'
    $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
}

$MyAdministratorPlainTextPassword = "${ admin_pass }"
if (-not [string]::IsNullOrEmpty($MyAdministratorPlainTextPassword)) {
    "Set local administrator password" | Write-Host
    $MyAdministratorPassword = $MyAdministratorPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
    $MyAdministrator = Get-LocalUser | Where-Object -Property "SID" -like "S-1-5-21-*-500"
    $MyAdministrator | Set-LocalUser -Password $MyAdministratorPassword
}

"Bootstrap script ended" | Write-Host
```

### `variables.tf`
```hcl
variable "zone" {
  type    = string
  default = "ru-central1-d"
}

variable "network" {
  type    = string
  default = "ya-network"
}

variable "subnet" {
  type    = string
  default = "ya-network"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.10.0/16"]
}

variable "nat" {
  type    = bool
  default = true
}

variable "image_family" {
  type    = string
  default = "windows-2019-dc-gvlk"
}

variable "name" {
  type = string
}

variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 4
}

variable "disk_size" {
  type    = number
  default = 50
}

variable "disk_type" {
  type    = string
  default = "network-nvme"
}

variable "user_name" {
  default = ""
  type    = string
}

variable "user_pass" {
  default = ""
  type    = string
}

variable "admin_pass" {
  default = ""
  type    = string
}

variable "timeout_create" {
  default = "300s"
}

variable "timeout_delete" {
  default = "300s"
}
```



## Conclusion
I followed the tutorial step by step and successfully deployed an Nginx container using Terraform and Docker. The outputs confirm that the container is running as expected. Also followed Yandex Quickstart Guide.

