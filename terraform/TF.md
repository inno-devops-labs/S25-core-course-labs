# Terraform

## Docker

Results of running `terraform state list`:

```bash
docker_container.moscow_time_app
docker_image.moscow_time_app
```

Results of running `terraform state show docker_container.moscow_time_app`:

```c
# docker_container.moscow_time_app:
resource "docker_container" "moscow_time_app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "sh",
        "-c",
        "gunicorn --bind 0.0.0.0:${PORT} --access-logfile - --error-logfile - app:app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "beda9f85563a"
    id                                          = "beda9f85563a6e3a5bd5df114c28812336bbe11b8bd4c3acbb52785e0015dc0b"
    image                                       = "sha256:fef50fb04885e8c3fef31b88eadedc00eba923f84995574ad27b21d6a6d5d49f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_time_app"
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
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

Results of running terraform output:

```c
container_id = "2e88fe0986165ddd45ad1ac775df43360a6dfe5252cfc3cd479ceee05b28a70a"
image_id = "sha256:fef50fb04885e8c3fef31b88eadedc00eba923f84995574ad27b21d6a6d5d49fpr0ventu5/moscow-time-app"
```

## Yandex

First, we need to setup our account. I have linked Yandex.Cloud account to my Yandex.Profile. After this, you need to enter your payment details. I will not provide my payment details here for personal reasons.

To use terraform securely, I have created a service account and used the official instruction to setup the environment variables. To be short, the commands I've done:

```bash

```

Now, I checked the available images and taken the "ubuntu-22" as an example (id - "").

```bash
➜  S25-core-course-labs git:(lab4) ✗ yc compute image list --folder-id standard-images | grep ubuntu-22
| fd80bm0rh4rkepi5ksdi | ubuntu-22-04-lts-v20230925                                 | ubuntu-2204-lts                                 | f2e3vsap4cmi4pqk05lg           | READY  |
| fd80e2irqkjdtbu6rrqk | nat-instance-ubuntu-22-04-lts-v20240729                    | nat-instance-ubuntu-2204                        | f2evo40rkkgol2045o9d,          | READY  |
| fd80i32k3d1h5dna4mjt | nat-instance-ubuntu-22-04-lts-v20240610                    | nat-instance-ubuntu-2204                        | f2e9pqf3v76132fem6p7,          | READY  |
| fd80ok8sil1fn2gqbm6h | ubuntu-22-04-lts-v20241014                                 | ubuntu-2204-lts                                 | f2essuur1lbjq176dukv           | READY  |
| fd80tpcdvop5e9qcosnq | ubuntu-2204-lts-oslogin-v20240101                          | ubuntu-2204-lts-oslogin                         | f2emscmodd2r1suum3f1           | READY  |
| fd813diu6vpu4q9buvjr | nat-instance-ubuntu-22-04-lts-v20240115                    | nat-instance-ubuntu-2204                        | f2e8nga0u93m5in9mtu1,          | READY  |
| fd813vofdafcjauqlsqv | ubuntu-2204-lts-oslogin-v20240108                          | ubuntu-2204-lts-oslogin                         | f2e8adopubpplrmcjkp6           | READY  |
```

As the standart-v1 plan is not available in ru-central1-d, I've used ru-central1-b.

For the VM, I have used the following resources:

- 2 cores
- 2GB of RAM
- 20GB of HDD

As this is standart-v1, the CPU is Intel® Xeon® Processor E5-2660 v4.

And now we can apply the configuration:

```bash
  Enter a value: yes

yandex_vpc_subnet.subnet-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2luq4uiu8algja3isqh]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=epd7ng9kbdek20dpq87n]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 38s [id=epd7974uqtc4icin26ej]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "<REDACTED>"
internal_ip_address_vm_1 = "192.168.10.24"
```

## GitHub

I have created a fine-granted token for S25-core-course-labs repository and used it as a sensetive variable in .tf file.

To apply and plan the terraform configuration, we need to import our current repository. For this, I used the following command:

```bash
terraform import github_repository.repo S25-core-course-labs
```

After this, I could successfuly run the terraform apply and create a branch protection rule.