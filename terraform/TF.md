# Terraform practice report

## Initial setup:

main.tf
```terraform
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"

  ports {
    internal = 80
    external = 8000
  }
}
```

**Commands executed:**

```bash
terraform init
terraform apply
terraform state
```

**Output:**

```
❯ terraform state show
Exactly one argument expected.
Usage: terraform [global options] state show [options] ADDRESS

  Shows the attributes of a resource in the Terraform state.

  This command shows the attributes of a single resource in the Terraform
  state. The address argument must be used to specify a single resource.
  You can view the list of available resources with "terraform state list".

Options:

  -state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.

❯ terraform show
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "cff5d058f391"
    id                                          = "cff5d058f391fd00b8468c7d78fdd610eed67cc245a63d96a88700afa5f4ae46"
    image                                       = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
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
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
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
resource "docker_image" "nginx" {
    id           = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx"
    image_id     = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```

## Changing the config

main.tf
```diff
-   external = 8000
+   external = 8080
```

**Commands executed:**

```bash
terraform apply
```

**Output:**

```
docker_image.nginx: Refreshing state... [id=sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx]
docker_container.nginx: Refreshing state... [id=cff5d058f391fd00b8468c7d78fdd610eed67cc245a63d96a88700afa5f4ae46]

Terraform used the selected providers to generate the
following execution plan. Resource actions are indicated
with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "cff5d058f391" -> (known after apply)
      ~ id                                          = "cff5d058f391fd00b8468c7d78fdd610eed67cc245a63d96a88700afa5f4ae46" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=cff5d058f391fd00b8468c7d78fdd610eed67cc245a63d96a88700afa5f4ae46]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=5d1a57608ae76807242ea45602124c11eb168c6b442a19b8deb64c602293e678]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Adding a variable and using an output

vars.tf

```tf
variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}
```

main.tf

```diff
-   name = "tutorial"
+   name = var.container_name
```

output.tf

```tf
output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.id
}
```

**Output:**

```bash
❯ terraform output
container_id = "489ecf23eebd82c655e36d2d4dde8c258b6ef358dce16b84ccfdbc1335874a20"
image_id = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx"
```

## Yandex cloud

1. I've configured a new service account, assigned an editor role and created an authorized key for it in the Cloud Console
2. I've used the `yc` CLI to set up the cloud id, folder id and an api token in the environment variables
3. I've initialized a new terraform workspace with yandex provider (and made changes to ~/.terraformrc according to the yandex cloud docs beforehand)
4. Issue 1: the guide to define VM resource from Yandex is outdated: it does not mention that you should create a network and set up a network interface in a VM.
