# Terraform Infrastructure Summary

## Best Practices Utilized

- **Provider Version Pinning**
- **Sensitive Variables Handling**
- **Network Segmentation**
- **SSH Key-Based Authentication**

## Docker Infrastructure

### State List

```bash
docker_container.moscow-time-app
docker_image.moscow-time-app
```

### Resource Details

#### `docker_container.moscow-time-app`

```terraform
resource "docker_container" "moscow-time-app" {
    attach                                      = false
    bridge                                      = null
    command                                     = ["sh", "./run.sh"]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "4763f67ea127"
    id                                          = "4763f67ea12746e2ca2470ab192bb6572bc23d24e3bce1179b4a4c5d8bec5652"
    image                                       = "sha256:ab2ab10dc5c1be95654dffd1458537762d5ab81c5a455580fffd880623eaffbf"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    working_dir                                 = "/usr/src/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### `docker_image.moscow-time-app`

```terraform
resource "docker_image" "moscow-time-app" {
    id           = "sha256:ab2ab10dc5c1be95654dffd1458537762d5ab81c5a455580fffd880623eaffbfjustcgh/moscow-time-app:latest"
    image_id     = "sha256:ab2ab10dc5c1be95654dffd1458537762d5ab81c5a455580fffd880623eaffbf"
    keep_locally = false
    name         = "justcgh/moscow-time-app:latest"
    repo_digest  = "justcgh/moscow-time-app@sha256:a494f726a00d1802b883e0ff0f2e29e8ca03fa5c3dc2cd2b322bf82b91659c74"
}
```

### Outputs

```terraform
container_image_python = "sha256:ab2ab10dc5c1be95654dffd1458537762d5ab81c5a455580fffd880623eaffbf"
container_name_python = "app_python"
container_port_python = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

---

## Cloud Infrastructure (Yandex)

### Steps and Challenges

- install yandex cloud cli
- create service account
- get all the necessary tokens and ids
- develop an infrastructure
- record the outputs

### State List

```bash
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Resource Details

#### `yandex_compute_instance.vm-1`

```terraform
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-05T15:22:40Z"
    description               = null
    folder_id                 = "b1g21aoblblp94jt4m9a"
    fqdn                      = "epd5agecqoulbddt5f7e.auto.internal"
    gpu_cluster_id            = null
    hostname                  = null
    id                        = "epd5agecqoulbddt5f7e"
    maintenance_grace_period  = null
    metadata                  = {"ssh-keys" = (sensitive value)}
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"
}
```

#### `yandex_vpc_network.network-1`

```terraform
resource "yandex_vpc_network" "network-1" {
    created_at = "2025-02-05T15:22:00Z"
    id         = "enpab1lfb08bthi5122r"
    name       = "Network1"
}
```

#### `yandex_vpc_subnet.subnet-1`

```terraform
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-05T15:22:39Z"
    id             = "e2ldjf3sk19lv1o5qj7i"
    name           = "Subnet1"
    network_id     = "enpab1lfb08bthi5122r"
    zone           = "ru-central1-b"
}
```

---

## GitHub Infrastructure

### State List

```bash
github_branch_default.master
github_branch_protection.default
github_repository.devops
```

### Resource Details

#### `github_branch_default.master`

```terraform
resource "github_branch_default" "master" {
    branch     = "master"
    id         = "S25-core-course-labs"
    repository = "S25-core-course-labs"
}
```

#### `github_branch_protection.default`

```terraform
resource "github_branch_protection" "default" {
    enforce_admins = true
    id             = "BPR_kwDONwHR2c4DiejZ"
    pattern        = "master"
}
```

#### `github_repository.devops`

```terraform
resource "github_repository" "devops" {
    name        = "S25-core-course-labs"
    visibility  = "public"
    repo_id     = 922866137
}
```

## GitHub Teams Infrastructure (Bonus Repo)

I also implemented the bonus task. Here is the [organisation](https://github.com/justcgh9-org), [repo](https://github.com/justcgh9-org/bonus-repo), and [teams](https://github.com/orgs/justcgh9-org/teams)

### State List

```bash
github_branch_default.repo_main
github_branch_protection.repo_protection
github_repository.repo
github_team.justcgh9
github_team.others
github_team_repository.justcgh9_repo
github_team_repository.others_repo
```

### Resource Details

#### `github_branch_default.repo_main`

```terraform
resource "github_branch_default" "repo_main" {
    branch     = "main"
    id         = "bonus-repo"
    repository = "bonus-repo"
}
```

#### `github_branch_protection.repo_protection`

```terraform
resource "github_branch_protection" "repo_protection" {
    enforce_admins = true
    pattern        = "main"
    repository_id  = "bonus-repo"

    required_pull_request_reviews {
        required_approving_review_count = 1
    }
}
```

#### `github_repository.repo`

```terraform
resource "github_repository" "repo" {
    name       = "bonus-repo"
    visibility = "public"
    repo_id    = 927930971
}
```

#### `github_team.justcgh9`

```terraform
resource "github_team" "justcgh9" {
    name        = "OP team"
    description = "the best team there is"
    privacy     = "closed"
    id          = "12122774"
}
```

#### `github_team.others`

```terraform
resource "github_team" "others" {
    name        = "just guys"
    description = "average team"
    privacy     = "closed"
    id          = "12122776"
}
```

#### `github_team_repository.justcgh9_repo`

```terraform
resource "github_team_repository" "justcgh9_repo" {
    team_id    = "12122774"
    repository = "bonus-repo"
    permission = "push"
}
```

#### `github_team_repository.others_repo`

```terraform
resource "github_team_repository" "others_repo" {
    team_id    = "12122776"
    repository = "bonus-repo"
    permission = "maintain"
}
```
