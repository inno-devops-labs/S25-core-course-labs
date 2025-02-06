# TF

## Best Practices Implemented

1. **Configuration Management**
   - Using variables for configurable values
   - Consistent resource naming patterns
   - Proper resource attribute organization

2. **Output Management**
   - Defining useful outputs for resource properties
   - Structured output format for better readability

3. 1. **Security Best Practices**
   - Using environment variables for sensitive information (TF_VAR_github_token)
   - Not committing sensitive tokens directly in code

## Docker Task

### terraform show

```bash
# docker_container.app_container:

resource "docker_container" "app_container" {
attach = false
bridge = [90mnull[0m[0m
command = [
"redis-server",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_set = [90mnull[0m[0m
cpu_shares = 0
domainname = [90mnull[0m[0m
entrypoint = [
"docker-entrypoint.sh",
]
env = []
hostname = "a8348491799f"
id = "a8348491799fadce35441b972870398cb42da6ca52ac168aa07f5942642624cb"
image = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = [90mnull[0m[0m
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = [90mnull[0m[0m
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "bridge"
pid_mode = [90mnull[0m[0m
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_signal = [90mnull[0m[0m
stop_timeout = 0
tty = false
user = [90mnull[0m[0m
userns_mode = [90mnull[0m[0m
wait = false
wait_timeout = 60
working_dir = "/data"

    ports {
        external = 4000
        internal = 4000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}

# docker_image.app_image:

resource "docker_image" "app_image" {
id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79aredis:latest"
image_id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
name = "redis:latest"
repo_digest = "redis@sha256:eadf354977d428e347d93046bb1a5569d701e8deb68f090215534a99dbcb23b9"
}
```

### terraform state list

```bash
docker_container.app_container
docker_image.app_image
```

### terraform state show docker_container.app_container

```bash
# docker_container.app_container:

resource "docker_container" "app_container" {
attach = false
bridge = null
command = [
"redis-server",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_set = null
cpu_shares = 0
domainname = null
entrypoint = [
"docker-entrypoint.sh",
]
env = []
hostname = "a8348491799f"
id = "a8348491799fadce35441b972870398cb42da6ca52ac168aa07f5942642624cb"
image = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = null
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = null
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "bridge"
pid_mode = null
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_signal = null
stop_timeout = 0
tty = false
user = null
userns_mode = null
wait = false
wait_timeout = 60
working_dir = "/data"

    ports {
        external = 4000
        internal = 4000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}
```

### terraform state show docker_image.app_image

```bash
resource "docker_image" "app_image" {
   id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79aredis:latest"
   image_id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
   name = "redis:latest"
   repo_digest = "redis@sha256:eadf354977d428e347d93046bb1a5569d701e8deb68f090215534a99dbcb23b9"
}
```

### Change container name

```bash
terraform apply
```

```bash
latest" # forces replacement
~ init = false -> (known after apply)
~ ipc_mode = "private" -> (known after apply)
~ log_driver = "json-file" -> (known after apply) - log_opts = {} -> null - max_retry_count = 0 -> null - memory = 0 -> null - memory_swap = 0 -> null
~ name = "app_python" -> "app_python_changed" # forces replacement
~ network_data = [
- {
- gateway = "172.17.0.1"
- global_ipv6_prefix_length = 0
- ip_address = "172.17.0.2"
- ip_prefix_length = 16
- mac_address = "02:42:ac:11:00:02"
- network_name = "bridge"
# (2 unchanged attributes hidden)
},
] -> (known after apply)

```

### terraform output

```bash
container_image = "redis:latest"
container_name = "app_python_changed"
container_port = tolist([
{
"external" = 4000
"internal" = 4000
"ip" = "0.0.0.0"
"protocol" = "tcp"
},
])

```

## Yandex Task

**Set up steps:**

1. Install cloud cli
2. Create service account
3. Generate tokens and ids
4. Set up the provider and resources
5. Run `terraform apply`

**Outputs**:

- `terraform state list`:

```bash
data.yandex_compute_image.ubuntu
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

- `terraform show`:

```bash
# data.yandex_compute_image.ubuntu:
data "yandex_compute_image" "ubuntu" {
    created_at          = "2025-02-03T11:06:30Z"
    description         = "ubuntu 22.04 lts"
    family              = "ubuntu-2204-lts"
    folder_id           = "standard-images"
    hardware_generation = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    id                  = "fd8j3fo8lqh4730j2ftd"
    image_id            = "fd8j3fo8lqh4730j2ftd"
    labels              = {}
    min_disk_size       = 8
    name                = "ubuntu-22-04-lts-v20250203"
    os_type             = "linux"
    pooled              = true
    product_ids         = [
        "f2ebj2oj0d2aeadn1j0m",
    ]
    size                = 7
    status              = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-05T20:37:58Z"
    description               = null
    folder_id                 = "b1gumar694vnatu3hepu"
    fqdn                      = "fb1gumar694vnatu3hepu.auto.internal"
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
    id                        = "fhmj7plmp00npe9hgmm3"
    labels                    = {}
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmspt4b17etjqsovdp2"
        disk_id     = "fhmspt4b17etjqsovdp2"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd8j3fo8lqh4730j2ftd"
            kms_key_id  = null
            name        = null
            size        = 8
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
        ip_address         = "192.168.20.31"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:13:3e:6b:6c"
        nat                = true
        nat_ip_address     = "89.169.131.82"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b503fimd5moima07hb"
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

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-05T20:35:15Z"
    default_security_group_id = "enpiv2r1fafj7fmp3249"
    description               = null
    folder_id                 = "b1gfbs7j036gik9qg28a"
    id                        = "enpgg0ui8ednp4ulk3od"
    labels                    = {}
    name                      = "Network-1"
    subnet_ids                = [
        "e9b503fimd5moima07hb",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-05T20:37:57Z"
    description    = null
    folder_id      = "b1gumar694vnatu3hepu"
    id             = "e9b503fimd5moima07hb"
    labels         = {}
    name           = "Subnet-1"
    network_id     = "enpgg0ui8ednp4ulk3od"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Github Task

### Export Variables

```bash
export TF_VAR_github_token="your-token-here"
```

### Import Configuration

```bash
terraform import "github_repository.core-course-labs" "S25-core-course-labs"
```

### Output

- `terraform state list`:

```bash
github_repository.core-course-labs:
  Import ID: github_repository.core-course-labs
```

- `terraform state show github_branch_protection.main`:

```bash
# github_branch_protection.main:

resource "github_branch_protection" "main" {
allows_deletions = false
allows_force_pushes = false
enforce_admins = false
id = "BPR_kwDONx0tmc4DikOO"
lock_branch = false
pattern = "main"
repository_id = "R_kgDONx0tmQ"
require_conversation_resolution = false
require_signed_commits = false
required_linear_history = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = true
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }

    required_status_checks {
        strict = true
    }

}
```

- `terraform state show github_repository.core-course-labs`:

```bash
# github_repository.core-course-labs:

resource "github_repository" "core-course-labs" {
allow_auto_merge = false
allow_merge_commit = true
allow_rebase_merge = true
allow_squash_merge = true
allow_update_branch = false
archived = false
auto_init = false
default_branch = "master"
delete_branch_on_merge = false
description = "DevOps Engineering Course Labs"
etag = "W/\"5e5d83275ec8daef2caf5078a7c5bede076eebe218d2e96cfcbae381b05c808d\""
full_name = "HaidarJbeily7/S25-core-course-labs"
git_clone_url = "git://github.com/HaidarJbeily7/S25-core-course-labs.git"
has_discussions = false
has_downloads = false
has_issues = true
has_projects = false
has_wiki = true
homepage_url = null
html_url = "https://github.com/HaidarJbeily7/S25-core-course-labs"
http_clone_url = "https://github.com/HaidarJbeily7/S25-core-course-labs.git"
id = "S25-core-course-labs"
is_template = false
merge_commit_message = "PR_TITLE"
merge_commit_title = "MERGE_MESSAGE"
name = "S25-core-course-labs"
node_id = "R_kgDONx0tmQ"
primary_language = null
private = false
repo_id = 924659097
squash_merge_commit_message = "COMMIT_MESSAGES"
squash_merge_commit_title = "COMMIT_OR_PR_TITLE"
ssh_clone_url = "git@github.com:HaidarJbeily7/S25-core-course-labs.git"
svn_url = "https://github.com/HaidarJbeily7/S25-core-course-labs"
topics = []
visibility = "public"
vulnerability_alerts = false
web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "enabled"
        }
        secret_scanning_push_protection {
            status = "enabled"
        }
    }

}

```
