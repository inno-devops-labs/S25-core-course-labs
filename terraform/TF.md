## Outputs of the commands

There is no `terraform state show` command, but I believe this was required

```bash
terraform show
```

~~~
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
    hostname                                    = "52d442d1d5ea"
    id                                          = "52d442d1d5eac00552f86e4fb64416e2b23142709d24bfa2b03ede3d8c7289bd"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
~~~

```bash
terraform state list
```

~~~
docker_container.nginx
docker_image.nginx
~~~

## Utilize input variables to rename your Docker container

I chose to keep the variables in [variables.tf](./variables.tf), you can see it there.

## Document a part of the log of the applied changes

I genuinly do not understand what specific changes I need to document, but here is a log of the changes I had during
the tutorial:

~~~
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
      ~ hostname                                    = "2e5d4192e2ba" -> (known after apply)
      ~ id                                          = "2e5d4192e2babe4ef2f32e3d7955c84d11c65805e28d26baa4d6ddf62844438b" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "MagelonExampleContainer"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
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
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.
~~~

```bash
terraform output
```

~~~
container_id = "71e9d89a79bb33f8b26bdf9626ed776ab8da9be79897329031e4d1bda0079844"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
~~~

# Yandex cloud

I will try to remember all the steps that I had to take during Yandex cloud, but the first challange was creating an
account, as Yandex died and did not want to have an SSL connection with me and that made me retry the whole creation several times.

Another issue with the provided document is that it does not provide instructions on how to download `Yandex CLI`
So, I found [the documentation](https://yandex.cloud/en-ru/docs/cli/quickstart), although not from my first attempt.

Rest assured, my next issue was inside of `CMD`, as Windows is silly and PowerShell did not want to cooperate. Also,
at the next steps I changed back to just `CMD`, yet I did not know that the **ENV** are somehow different there.
Thankfully it was only an issue of the last couple of steps.

I have gotten to the *Management Console* inside of `Yandex.Cloud`, created the service account, gave it admin role and
then in `CLI` I set the profile to run all the operations on behalf of the service account, which meant creating an
autorized key, creating a profile, naming it and configuring all the `ENV` and other variables.

Then I searched for ```$env:APPDATA/terraform.rc```, but I did not expect it to be a file, instead of a folder along
with everything that is usually in `APPDATA`. There I set up the mirrors as
[in the tutorial](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#configure-provider).

Then I prepared an infrastructure plan, but the images that the command in the tutorial gave did not work, so I
just Googled some other Ubuntu images and inserted them in the [main.tf](./YandexCloud/main.tf) file.

Then I forgot that I was making a user for `Linux` (well, I am working from `Windows`), so I needed to create Users,
just as described [in here](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#users)
in the `Linux` section.

Then I needed to validate the configuration:

```bash
terraform validate
```

Then I needed to format the files:

```bash
terraform fmt
```

Then I needed to prepare (plan) the configuration:

```bash
terraform plan
```

Then (after fixing errors) I needed to create the resources:

```bash
terraform apply
```

That concluded my testings of the Yandex Cloud.

And then, crucially, I needed to stop spending money that I did not have, so I deleted the resources:

```bash
terraform destroy
```

# Best practices for terraform

- Implement a Secrets Management Strategy
  - The secrets are secret
- Use existing shared and community modules
  - Docker module
- Avoid variables hard-coding
  - No variables (Except for Yandex)
- Always format and validate
  - I did it all the time
- Use a consistent naming convention and descriptions
  - There is a description everywhere
- Test your Terraform code
  - Used `terraform plan` a lot
- Take advantage of the IDE extensions
  - I was never so happy to see `PyCharm` highlighting and warnings

Also acknowledged (primarily from [here](https://spacelift.io/blog/terraform-best-practices),
but also read [this](https://www.terraform-best-practices.com/) and
[that](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices)):

- Use remote state
- Import existing infrastructure
- Tag your Resources
- Introduce Policy as Code
- Enable debug/troubleshooting
- Build modules wherever possible
- Use loops and conditionals
- Use functions
- Take advantage of Dynamic Blocks
- Use Terraform Workspaces
- Use the Lifecycle Block
- Use variables validations
- Leverage Helper tools to make your life easier