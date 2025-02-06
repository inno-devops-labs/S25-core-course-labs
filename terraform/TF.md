# TF Documentation

## Best Practices Implemented

## Terraform Output

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
