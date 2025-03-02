# Terraform setup report

## Setting up terraform locally

<details>
<summary>terraform show output</summary>
<br>
S25-core-course-labs\terraform> terraform show
```batch
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
    hostname                                    = "d3383c3fc25e"
    id                                          = "d3383c3fc25e764cf6e3aa12945b646ce64cf5c2e12a386103ea37aade5d9b7f"
    image                                       = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
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
    id           = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
    image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```
</details>

<details>
<summary>terraform state list output</summary>
<br>
```batch
S25-core-course-labs\terraform>terraform state list
docker_container.nginx
docker_image.nginx
```
</details>

<details>
<summary>Applied changes</summary>
<br>
```batch
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
      + name                                        = "tutorial"
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
```
</details>

<details>
<summary>terraform output output</summary>
<br>
```batch
S25-core-course-labs\terraform>terraform output
container_id = "57c257e09966b50144c5e5f257f2489599d78345e08df024698996b20140b888"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
```
</details>

## Setting up terraform on Yandex Cloud

First, I logged into Yandex Cloud using my Yandex ID and added a service accout with an admin role.
This step did not give me much trouble, but I was incredibly reluctant to do this since
I generally dislike entering my personal information online, especially for a university assignment,
which I believe should not involve my debit card.

Second, I followed the tutorial closely to create a CLI profile and added the environment variables
YC_TOKEN, YC_CLOUD_ID and YC_FOLDER_ID. The only problem here was that I did not see where to get the
cloud and folder id's for some short amount of time.

Third, I configured terraforma to use yandex cloud and made the main.tf file. This was also mostly copied
from the tutorial, apart for some things. After I ran terraform validate, it seemed like it ws ok, but
this was the hardest part to do. The thing is, the default platform for compute instances is standard-1,
but it does not exist in ru-central1-d zone, which I was using. It took some more figuring out to
learn that and correctly emplace anothe platform into the config. Moreover, I had to look for image id's,
and the command "yc compute image list --folder-id standard-images" did not yield a working image from
what i've tried. I had to look up an ubuntu vm id on the website, which worked.

Lastly, I validated and formatted the configuration and applied it, after which everything worked and I could see
my instances on the dashboard.

## Terraforma best practices

I have implemented the following best practices:
- Import existing infrastructure
  The github structure was imported into terraform because it already existed
- Avoid variables hard-coding
  I have used environmental variables to store the github token and not write it
  anywhere, even in the variables file.
- Always format and validate
  As described above, I have always formatted and validated the configuration before
  using it.
- Implement a Secrets Management Strategy
  No secret is currently inside the configuration files, except for ssh public key,
  but it is called public for a reason. I have used TF_VAR_token to store my github
  PAT.
