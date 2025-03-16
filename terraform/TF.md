 
# terraform state show:
-state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.

# terraform state list:

docker_container.python_app
docker_image.python_app

# logs

```bash
docker_image.python_app: Refreshing state... [id=sha256:e3cd76718b978fb83fe841eba1012790b8f7b6baa99f41e2e85727f43f39a5a8ksenon9/lab2:latest]
docker_image.nginx: Refreshing state... [id=sha256:e3cd76718b978fb83fe841eba1012790b8f7b6baa99f41e2e85727f43f39a5a8ksenon9/lab2:latest]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy

Terraform will perform the following actions:

  # docker_container.python_app will be created
  + resource "docker_container" "python_app" {
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
      + image                                       = "sha256:e3cd76718b978fb83fe841eba1012790b8f7b6baa99f41e2e85727f43f39a5a8"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "lab4"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be destroyed
  # (because docker_image.nginx is not in configuration)
  - resource "docker_image" "nginx" {
      - id           = "sha256:e3cd76718b978fb83fe841eba1012790b8f7b6baa99f41e2e85727f43f39a5a8ksenon9/lab2:latest" -> null
      - image_id     = "sha256:e3cd76718b978fb83fe841eba1012790b8f7b6baa99f41e2e85727f43f39a5a8" -> null
      - keep_locally = false -> null
      - name         = "ksenon9/lab2:latest" -> null
      - repo_digest  = "ksenon9/lab2@sha256:845d78eb187727f00d78b9a23463f8b82b70fe66d7ea1edabd51f09668f151d7" -> null
    }

Plan: 1 to add, 0 to change, 1 to destroy.


# Output 
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

container_name = "lab4"
```

# Yandex-cloud

## Steps

- I created account
- installed yc (yandex cloud): 
```bash 
iex (New-Object System.Net.WebClient).DownloadString('https://storage.yandexcloud.net/yandexcloud-yc/install.ps1'
```
- and logged in 
```bash 
yc init
```

- Then I chose folder and zone
- created main.tf file with using folder and zone ids from previous step
- created token  
```bash 
yc iam create-token
```

- I put the above data into variables
- then execute:

```bash 
terraform init
terraform plan
terraform apply
```


# logs 

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.terraform1 will be created
  + resource "yandex_compute_instance" "terraform1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd869umlvb3mfbj2lrks"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
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
          + memory        = 4
        }

      + scheduling_policy (known after apply)
    }

  # yandex_compute_instance.terraform2 will be created
  + resource "yandex_compute_instance" "terraform2" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + name                      = "terraform2"
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd869umlvb3mfbj2lrks"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
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
          + cores         = 4
          + memory        = 8
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network_1 will be created
  + resource "yandex_vpc_network" "network_1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet_1 will be created
  + resource "yandex_vpc_subnet" "subnet_1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + terraform1_public_ip = (known after apply)
  + terraform2_public_ip = (known after apply)
```


# GitHub Infrastructure

## Best Practices Applied
- **Environment Variables for Sensitive Data:** I use the environment variable GITHUB_TOKEN for authentication instead of hardcoding it in the configuration.
- **Modular Structure:** Terraform configuration is organized into separate files 

# logs:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.default will be created
  + resource "github_branch_default" "default" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "lab4_terraform"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

PS C:\Users\Admin\PycharmProjects\devOps\S25-core-course-labs\terraform\gitHub> terraform apply                                          
                                          
  Enter a value:                          

github_repository.repo: Refreshing state... [id=lab4_terraform]
github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create                                   
                                             
Terraform will perform the following actions:

  # github_branch_default.default will be created
  + resource "github_branch_default" "default" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "lab4_terraform"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "lab4_terraform"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```