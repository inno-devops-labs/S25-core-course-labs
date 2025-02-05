# Terraform Best Practices

## 1. Secure Storage of Secrets
- Use environment variables to store sensitive data (e.g., GitHub token).
- Avoid hardcoding secrets directly into the configuration files.

## 2. Importing Existing Resources
- If a resource already exists in your infrastructure, use the `terraform import` command to include it in your Terraform configuration.

## 3. Modular Structure
- Organize your Terraform code into reusable modules to improve maintainability and scalability.
- Break down complex configurations into smaller, manageable components.

## 4. Branch Protection
- Configure branch protection rules for critical branches (e.g., `main`) to enforce code reviews, status checks, and other safeguards.
- Ensure that pull request reviews and required approvals are enforced before merging changes.


#### Terraform state list output:
docker_container.nginx
docker_image.nginx
#### Terrafor show putput:
/# docker_container.nginx:
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
    hostname                                    = "1407231ed187"
    id                                          = "1407231ed18783105a3cbcfabca831007d4b9acafba665a49705712d1dc11826"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
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

/# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}

#### Terraform output output:
$ terraform output
container_id = "8b745d5acb9b3f2007388a517a8399e8dee6007be8f35ea1d947079eec9e0c68"
container_name = "Lab4_container"
container_port = 8000

#### Log of applied changes
docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Still creating... [30s elapsed]
docker_image.nginx: Still creating... [40s elapsed]
docker_image.nginx: Still creating... [50s elapsed]
docker_image.nginx: Still creating... [1m0s elapsed]
docker_image.nginx: Creation complete after 1m10s [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=1407231ed18783105a3cbcfabca831007d4b9acafba665a49705712d1dc11826]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

# Yandex Cloud integration
## Proccess
#### 1. Create a service account on Yandex Cloud
#### 2. Set up CLI
#### 3. Write .terraformrc at the root
#### 4. Generate service account key
#### 5. Set up configs (folder id, cloud id, etc)
#### 6. Configure a provider in .tf file
#### 7. Choose a VM and set up network and subnetwork
#### 8. Add ssh access
#### 9. Add users
#### And finally, fall asleep
## Difficulties
#### Some platforms (standart-v1) not available in current zone
