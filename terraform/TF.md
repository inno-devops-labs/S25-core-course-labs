# Terraform overview

### Best Practices 

#### 1. Linting and formatting

```bash
terraform fmt -recursive
```

```bash
terraform validate
```

## Secure storage of sensitive data

Sensitive data are stored securely and excluded from git:

```
*.auto.tfvars
*.tfvars
```

## Clean git index

.terraform/ – Terraform working directory
*.tfstate – State files
*.tfstate.backup – Backup state files
*.auto.tfvars – Auto-applied variable files

## Fixed versions

```hcl
provider "yandex" {
  version = "~> 0.76"
}
```

## Yandex Cloud Infrastructure
[tutorial](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1)

Everything was done by standards

## Docker task

[tutorial](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)

### Outputs

```text
xrvst@dev-tachka:~/study/devops/S25-core-course-labs/terraform/docker$ terraform state show docker_container.nginx
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
hostname                                    = "as1d0e7f2w1e"
id                                          = "a89dce7f2f3ea436ed6beb09909820f8b86425a5f5bfee3e72c1cc59c014b023"
image                                       = "sha256:kq21925241f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f438243139cs92a"
init                                        = false
ipc_mode                                    = "private"
log_driver                                  = "json-file"
logs                                        = false
max_retry_count                             = 0
memory                                      = 0
memory_swap                                 = 0
must_run                                    = true
name                                        = "my_container"
network_data                                = [
{
gateway                   = "172.17.0.1"
global_ipv6_address       = null
global_ipv6_prefix_length = 0
ip_address                = "172.17.0.2"
ip_prefix_length          = 16
ipv6_gateway              = null
mac_address               = "12:42:bc:21:01:02"
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
    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_image.nginx:
    id           = "sha256:kq21925241f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f438243139cs92anginx:latest"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
xrvst@dev-tachka:~/study/devops/S25-core-course-labs/terraform/docker$ terraform state list docker_container.nginx
docker_container.nginx
xrvst@dev-tachka:~/study/devops/S25-core-course-labs/terraform/docker$ terraform state list docker_image.nginx
docker_image.nginx
xrvst@dev-tachka:~/study/devops/S25-core-course-labs/terraform/docker$ terraform output
my_container_id = "a89dce7f2f3ea436ed6beb09909820f8b86425a5f5bfee3e72c1cc59c014b023"
my_container_image = "sha256:kq21925241f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f438243139cs92a"
my_container_name = "my_container"
```