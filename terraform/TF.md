# Terraform Lab Report

After installing and updating `docker` and `terraform` to continue working on the task, I obtained `terraform` project data. However, some data could not be received due to an Error: "configuring Terraform AWS Provider: no valid credential sources for Terraform AWS Provider found." I used different proxies and VPNs, used different operating systems, and rewrote the code to fix this error, but I still couldn't continue working. After some stage described in the attached guide, the terraform apply command stopped working. Therefore, I have attached all the files that I could make in this lab in the terraform folder.

## Installation and setup

1. **Install `terraform`**:
   - Download `terraform` from the official website.
   - Add `terraform` to system PATH.
   - Verify installation using:
     ```
     terraform --version
     ```

2. **Install `docker`**:
   - Download `pip` from the official website.
   - Adde `pip` to system PATH.
   - Download `docker` using:
     ```
     pip install docker
     ```

3. **Initialize `terraform` project**:
   - Created a `terraform` directory.
   - Run command to initialize the project and install required providers:
     ```
     terraform init
     terraform apply
     ```

## Terraform outputs

### `terraform show`
```
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
            gateway                   = "172.17.0.1"
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:11:00:02"
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

### `terraform state show`
```
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

### `terraform state list`
```
docker_container.nginx
docker_image.nginx
```

# Terraform for GitHub

### GitHub Infrastructure Details

Terraform configuration includes:
- Repository name: `core-course-labs`
- Repository description: `Repository for terraform lab`
- Visibility: `public`
- Default branch: `main`
- Branch protection rules applied to `main`

### Import Existing Repository
```
terraform import "github_repository.core-course-labs" "core-course-labs"
```

# Best Practices Implemented

- **State Management**: Used Terraform state to track resources.
- **Environment Variables**: GitHub token stored in `GITHUB_TOKEN` env variable instead of hardcoding.
- **Modularization**: Used separate `.tf` files for better organization.
- **Version Locking**: Defined provider versions to ensure stability.
- **Security**: Applied branch protection rules to enforce repository policies.

