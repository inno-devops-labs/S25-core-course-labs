# Terraform starting

I installed and built terraform things. I faced some problems with my aws, i used vpn but still there were some problems
with it

## Results of terraform show

Result can be founded in the output_tf_show.txt:
With the command
`
    terraform show
`

I got

```shell
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "c81778adc197"
    id                                          = "c81778adc197c2f81e6c09df14ec56064fae79999a27e2adc80d1434bdd3558d"
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
            gateway                   = "172.30.12.1"
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.30.12.24"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:1e:0c:18"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = [90mnull[0m[0m
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
    user                                        = [90mnull[0m[0m
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = [90mnull[0m[0m

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx"
    image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}

```

## Results of terraform state show

The `terraform state show` command provides detailed information about the state of resources stored in Terraform's
state
file. It helps track resource attributes and aids in debugging or further configuration. The output can be found in the
`output_tf_state.txt` file.

With the command

```bash
    terraform state show
```

I got

```bash
Usage: terraform [global options] state show [options] ADDRESS

  Shows the attributes of a resource in the Terraform state.

  This command shows the attributes of a single resource in the Terraform
  state. The address argument must be used to specify a single resource.
  You can view the list of available resources with "terraform state list".

Options:

  -state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.
```

## Results of terraform state list

The `terraform state list` command lists all resources that are currently managed in the Terraform state file.

The output from running:

```bash
    terraform state list
```

I got

```bash
    docker_container.nginx
    docker_image.nginx
```

After running the commands above and making the necessary changes to my configuration files, I added the `outputs.tf`
file
to display the results from Terraform outputs. The output from the command `terraform output` can be found in
`output_tf_outputs.txt`.

The log from running the `terraform output` command is as follows:

```bash
    container_id: "2a6d3c89f4e94f62bced7ab3774b9050f1f5a9c43c83e3d1b7bfa3b6c5f8a1e1"
    image_id: "sha256:d53a7a6e2ff8b5a4236f2938bcf2e7164582be0d9cf734c64e7a2e1b73e5da98nginx:latest"
```

Once more, you can find the logs in text files, which offer a complete overview of what happened during the Terraform
operations. After making sure everything was set up correctly, I destroyed the Terraform resources without any issues.

## Task 2

### GitHub Infrastructure Details

Terraform configuration includes:

- Repository name: s25-core-course-labs
- Repository description: Repository for terraform lab
- Visibility: public
- Default branch: main
- Branch protection rules applied to main

Import Existing Repository

```bash
    terraform import "github_repository.core-course-labs" "s25-core-course-labs"
```

## Bonus task

`terraform state show`

```bash
terraform state show github_team.admin_team
terraform state show github_team.developer_team
```

For the 
`terraform state list`

```bash
github_team.admin_team
github_team.developer_team
github_team_repository.admin_repo
github_team_repository.developer_repo
```

#### Best Practices Implemented

- Resource tracking: Leveraged Terraform's state management to monitor resources effectively.
- Environment variables: Stored the GitHub token in the `GITHUB_TOKEN` environment variable rather than embedding it
  directly in the code.
- Modular configuration: Organized the setup by splitting the configuration into separate .tf files for improved clarity
  and maintainability.
- Provider Version Control: Specified provider versions to maintain consistent behavior and prevent breaking changes.
- Security: Enforced repository policies by implementing branch protection rules.
