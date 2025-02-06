# Terraform

## Table of Contents

- [VK Cloud](#VK)
- [Docker](#Docker)
- [Github](#Github)
- [Best practises](#Best)

# VK

We need password to connect to VK cloud, so it automatically asking for password from console.
After `terraform apply`:

```
D:\git\core-course-labs\terraform\vk_cloud>terraform state list
data.vkcs_compute_flavor.compute
data.vkcs_images_image.compute
data.vkcs_networking_network.extnet
vkcs_compute_floatingip_associate.fip
vkcs_compute_instance.compute
vkcs_networking_floatingip.fip
vkcs_networking_network.network
vkcs_networking_port.port
vkcs_networking_port_secgroup_associate.port
vkcs_networking_router.router
vkcs_networking_router_interface.db
vkcs_networking_secgroup.secgroup
vkcs_networking_secgroup_rule.secgroup_rule
vkcs_networking_subnet.subnetwork

D:\git\core-course-labs\terraform\vk_cloud>terraform state show vkcs_compute_instance.compute
# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.0.4"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "dd20f13e-6e62-475a-ae83-c7048e5ae967"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "ssh",
    ]
    stop_before_destroy = false

    block_device {
        boot_index            = 0
        delete_on_termination = true
        destination_type      = "volume"
        source_type           = "image"
        uuid                  = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "192.168.0.4"
        mac            = "fa:16:3e:37:6a:a4"
        name           = "net"
        uuid           = "b3791ec3-fe9b-45a5-8216-995243399f3e"
    }
}

D:\git\core-course-labs\terraform\vk_cloud>terraform output
instance_fip = "212.233.95.21"
```

# Docker

We don't need any external info, just make sure Docker Daemon is running.
After `terraform apply`:

```
PS D:\git\core-course-labs\terraform\docker> terraform state list
docker_container.app_kotlin
docker_image.app_kotlin
PS D:\git\core-course-labs\terraform\docker> terraform state show docker_container.app_kotlin
# docker_container.app_kotlin:
resource "docker_container" "app_kotlin" {
    attach                                      = false
    command                                     = [
        "java",
        "-jar",
        "com.example.app-sample-all.jar",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "9a1a39523df3"
    id                                          = "9a1a39523df365b98de68a28594d7145b26907da3262a65dd961774109f3631b"
    image                                       = "sha256:000a6c2b89d5cde8df1c1687a38f17dbf7daadc2237b4d3c2cd8e72daebcab27"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_kotlin"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
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
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "nobody"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
PS D:\git\core-course-labs\terraform\docker> terraform output
container_id = "9a1a39523df365b98de68a28594d7145b26907da3262a65dd961774109f3631b"
image_id = "sha256:000a6c2b89d5cde8df1c1687a38f17dbf7daadc2237b4d3c2cd8e72daebcab27dyllasdek/app_kotlin:latest"
```

# Github

If you using Windows, you should add to environment variables `GITHUB_OWNER=<name_of_organisation>`

# Best practises

- I've seperated tf config files corresponding to its need, `variables.tf` stores variables and etc.

- Each project has its own folder to avoid intersection with condigurations

- Validating and formating terraform config files
