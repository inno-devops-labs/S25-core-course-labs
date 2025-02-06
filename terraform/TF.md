# Terraform

## Docker Infrastructure

### `terraform state list`

```powershell
> terraform state list

docker_container.nginx
docker_image.nginx
```

### `terraform state show`

- `docker_container.nginx`

```powershell
> terraform state show docker_container.nginx

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
    hostname                                    = "a74bd3073bcc"
    id                                          = "a74bd3073bcce2e75eac709500f6dbfa43c61109174967796ccb97504e2df874"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "nginx_container"
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

- `docker_image.nginx`

```powershell
> terraform state show docker_image.nginx

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```

### `terraform apply`

A part of the log with applied changes is documented here:

```powershell
> terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
      + name                                        = "nginx_container"
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

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 10s [id=sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=a74bd3073bcce2e75eac709500f6dbfa43c61109174967796ccb97504e2df874]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "a74bd3073bcce2e75eac709500f6dbfa43c61109174967796ccb97504e2df874"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```

### `terraform output`

```powershell
> terraform output

container_id = "a74bd3073bcce2e75eac709500f6dbfa43c61109174967796ccb97504e2df874"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```

## Yandex Cloud Infrastructure

1. I have created an account on [Yandex Cloud](https://cloud.yandex.com/)
2. There is one available free-tier option: a grant for 1000₽ that may be spent for virtual machines, which are suitable for this lab.
   > During the whole process of building a Yandex Cloud Infrastructure, I have followed the official [Yandex Quickstart Guide](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1).
3. To begin the setup, we need to create a [service account](https://yandex.cloud/en/docs/iam/concepts/users/service-accounts) via Identity and Access Management.

- I have chosen the folder where I wanted to create a service account. In my particular case, it was a `default` folder.
- Then I clicked the **Identity and Access Management** service in the service list
- Then I clicked the **Create service account** button.
- In the modal I specified the desired name, description, and have chosen the `editor` role and created the account.
  > **CAVEAT:** do not forget to set roles for a service account! Service account requires at least an `editor` role to have possibility to create a resources inside our folder.

4. Then we need to create [an authorized key](https://yandex.cloud/en/docs/iam/concepts/authorization/key) for the brand new service account.

The command I entered is:

```powershell
yc iam key create \
  --service-account-id aje***************** \
  --folder-name default \
  --output key.json
```

where:

- `service-account-id` is an identifier of service account
- `folder-name` is the name of folder where the service account is created. In my case it is `default`
- `output` is the name of output file, which will contain this authorized key.

The output:

```powershell
id: aje*****************
service_account_id: aje*****************
created_at: "2025-06-02T10:57:43.479156798Z"
key_algorithm: RSA_2048
```

5. Then I have created the CLI profile to perform operations as a service account.

```powershell
yc config profile create terraform_cli
```

The output:

```powershell
Profile 'terraform_cli' created and activated
```

6. Also we need to set the profile configuration.

To do so, I used the following commands:

```powershell
yc config set service-account-key key.json
yc config set cloud-id b1g*****************
yc config set folder-id b1g*****************
```

where:

- `service-account-key` is a file with authorized key of service account
- `cloud-id` is the identifier of a cloud
- `folder-id` is the identifier of a folder (in my case `default`)

7. Then I have added the authentication data from the previous step to the environment variables.
   Since I am using Windows as my primary OS, I did it in Powershell:

```powershell
$Env:YC_TOKEN=$(yc iam create-token)
$Env:YC_CLOUD_ID=$(yc config get cloud-id)
$Env:YC_FOLDER_ID=$(yc config get folder-id)
```

where:

- `YC_TOKEN` is IAM-token.
- `YC_CLOUD_ID` is the identifier of a cloud
- `YC_FOLDER_ID` is the identifier of a folder

8. Then we need to configure the Terraform provider.
   If you have previous provider (I did not have one), then you need to save its preferences.

```powershell
mv $env:APPDATA/terraform.rc $env:APPDATA/terraform.rc.old
```

I created the file `terraform.rc` and added the following block (which specifying the official Terraform mirror).

```powershell
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

9. Then I generated the SSH key for the user:

```powershell
ssh-keygen -t ed25519 -C "yc"
```

10. Now we can setup the Terraform configuration file.
    I have used the template specified in the guide, but it may be changed according to our needs.

- the provider is Yandex Cloud
- the availability zone of the provider is `ru-central1-a`

The image list is provided by Yandex Cloud Marketplace, which is available by this command:

```powershell
yc compute image list --folder-id standard-images
```

I have decided to use common LTS image - `ubuntu-2204-lts`, which has this ID: `fd85u0rct32prepgjlv0`.

### Resources created

The YC Disk is connected to YC Instance.
The YC Instance is connected to YVPC Subnet.
The YVPC Subnet is connected to YVPC Network.

The created VM has two IP addresses: internal and external.

- Yandex Compute Disk (HDD, 20GB, `ru-central1-a`, `ubuntu-2204-lts` image)
- Yandex Compute Instance (CPUx2, 2GB RAM)
- Yandex VPC Network
- Yandex VPC Subnet (`ru-central1-a`)

> Additionally, for the VM it is necessary to setup the **user metadata** (in the resource config I specified the metadata field and provided path to the `user_metadata.txt` file). It contains the public SSH key generated earlier and username for the user on this VM.

10. Then I initiated the provider using `terraform init`.

11. Format and validate the Terraform configuration: `terraform fmt` and `terraform validate`.

12. Then let's perform the check: `terraform plan`.

Output:

```powershell
> terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd85u0rct32prepgjlv0"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: yc_user
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICR8jQL9Pv6VF+HBwcSo79zvIB+24iRTNjTmGbGz1TOI
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params (known after apply)
        }

      + metadata_options (known after apply)

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
```

13. The configuration is ok, then I write `terraform apply` and confirm my choice.

Output:

```powershell
> terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd85u0rct32prepgjlv0"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: yc_user
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICR8jQL9Pv6VF+HBwcSo79zvIB+24iRTNjTmGbGz1TOI
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params (known after apply)
        }

      + metadata_options (known after apply)

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enpnm2vjefqcj2e9ljkm]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9b9lsrbvt7oeckhrtvr]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhmn9ik3sph8nuoq4tis]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [50s elapsed]
yandex_compute_instance.vm-1: Creation complete after 58s [id=fhmlokreq2o8a6bl6jvr]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.250.8.70"
internal_ip_address_vm_1 = "192.168.10.21"
```

14. Let's check the state list and separate states:

```powershell
> terraform state list

yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

- `yandex_compute_disk.boot-disk-1`

```powershell
> terraform state show yandex_compute_disk.boot-disk-1

# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2025-02-06T08:49:03Z"
    description = null
    folder_id   = "b1g*****************"
    id          = "fhmn9ik3sph8nuoq4tis"
    image_id    = "fd85u0rct32prepgjlv0"
    name        = "boot-disk-1"
    product_ids = [
        "f2ef01lju2nsansfdahf",
    ]
    size        = 20
    snapshot_id = null
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {
        disk_placement_group_id = null
    }

    hardware_generation {
        legacy_features {
            pci_topology = "PCI_TOPOLOGY_V1"
        }
    }
}
```

- `yandex_compute_instance.vm-1`

```powershell
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-06T08:49:14Z"
    description               = null
    folder_id                 = "b1g*****************"
    fqdn                      = "fhmlokreq2o8a6bl6jvr.auto.internal"
    gpu_cluster_id            = null
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    hostname                  = null
    id                        = "fhmlokreq2o8a6bl6jvr"
    maintenance_grace_period  = null
    metadata                  = {
        "user-data" = <<-EOT
            #cloud-config
            users:
              - name: yc_user
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh_authorized_keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICR8jQL9Pv6VF+HBwcSo79zvIB+24iRTNjTmGbGz1TOI
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmn9ik3sph8nuoq4tis"
        disk_id     = "fhmn9ik3sph8nuoq4tis"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd85u0rct32prepgjlv0"
            kms_key_id  = null
            name        = "boot-disk-1"
            size        = 20
            snapshot_id = null
            type        = "network-hdd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "192.168.10.21"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:15:c5:36:ed"
        nat                = true
        nat_ip_address     = "51.250.8.70"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b9lsrbvt7oeckhrtvr"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}
```

- `yandex_vpc_network.network-1`

```powershell
> terraform state show yandex_vpc_network.network-1

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-06T08:49:03Z"
    default_security_group_id = "enpm336la6u0c186ikf7"
    description               = null
    folder_id                 = "b1g*****************"
    id                        = "enpnm2vjefqcj2e9ljkm"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
```

- `yandex_vpc_subnet.subnet-1`

```powershell
> terraform state show yandex_vpc_subnet.subnet-1

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-06T08:49:05Z"
    description    = null
    folder_id      = "b1g*****************"
    id             = "e9b9lsrbvt7oeckhrtvr"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpnm2vjefqcj2e9ljkm"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

15. Finally, let's check the `terraform output`:

```powershell
> terraform output

external_ip_address_vm_1 = "51.250.8.70"
internal_ip_address_vm_1 = "192.168.10.21"
```

There were not any significant challenges, except for my forgetfullness to give the `editor` role to service account.
