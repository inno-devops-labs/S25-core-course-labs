# Terraform
## 1. Docker Infrastructure Using Terraform
### Proces of my work
Following the instructions provided in tutorial:
1. Install **Terraform**.
2. Create a file `main.tf`. 
3. Run with commands:
    ```bash
    terraform init
    terraform apply
    ```
4. Check the result:
    ```bash
    terraform show
    ```
   **Output**:
    ```bash
    docker_container.nginx:
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
        hostname                                    = "93a940f5449f"
        id                                          = "93a940f5449f99e8648e030e669a799251e744a455b65f7e7d9eaaa89093cbd1"
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
                ip_address                = "172.17.0.3"
                ip_prefix_length          = 16
                ipv6_gateway              = null
                mac_address               = "02:42:ac:11:00:03"
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
        id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
        image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
        keep_locally = false
        name         = "nginx:latest"
        repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
    }
    ```
    ```bash
    terraform state list
    ```
   **Output**:
   ```bash 
    docker_container.nginx
    docker_image.nginx
    ```
   
   ```bash
    terraform output
    ```
   **Output**:
   ```bash 
    container_id = "3ba84abedd1669701f7fc203d5bf2362b0fbf21eed2dcc95e234617384be00f6"
    container_name = "my-nginx-container"
    container_port = 8000
    ```

## 2. Yandex Cloud Infrastructure Using Terraform
### Proces of my work
Following the instructions provided in tutorial:

1. Create an account on Yandex Cloud.
2. Get the authentication data:
   - Create service account.
   - Choose **Identity and Access Management** service.
3. Configure the CLI profile to perform operations on behalf of the service account:
   ```bash
    yc iam key create \
    --service-account-id <service_account_id> \
    --folder-name <repository_name_of_service_acount> \
    --output key.json 
     ```
   You can find `service_account_id` and `repository_name_of_service_acount` in your account.
- If you have problem with `yc`, try this and repeat previous command:
   ```bash
    curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
   ```
4. Create a CLI profile to perform operations on behalf of the service account. Specify the profile name:
   ```bash
   yc config profile create <profile_name>
   ```
5. Set the profile configuration:
   ```bash
   yc config set service-account-key key.json
   yc config set cloud-id <cloud_id>
   yc config set folder-id <repository_id>
   ```
   You can find `cloud_id` and `repository_id` in your account.
6. Add authentication data to the environment variables:
   ```bash
   export YC_TOKEN=$(yc iam create-token)
   export YC_CLOUD_ID=$(yc config get cloud-id)
   export YC_FOLDER_ID=$(yc config get folder-id)
   ```
7. Create new directory `yc_conf` and file `main.tf` in it.
8. My `main.tf` you can check in repository.
- I use `ru-central1-d`
- To get the ID of the boot disk image from the Yandex Cloud Marketplace run ```yc compute image list --folder-id standard-images```. I chose first one.
- Create `meta.txt` and generate SSH-key. To do it run this command `ssh-keygen -t rsa -b 4096 -C "your_email"`.
9. Run the project and check results:
   ```bash
   terraform init
   terraform apply
   terraform validate
   terraform fmt
   ```   

# Terraform for GitHub
## Overview

This project uses Terraform to manage the infrastructure of the GitHub repository. We have created a configuration that allows you to automate the configuration of the repository, including branch protection and their rules.

## Work done

1. **Setting up the GitHub provider:**
- The provider `integrations/github` version `~> 5.0` is used.
- Added environment variables for secure storage of the GitHub token ('TF_VAR_github_token').

2. **Creating a repository:**
- The `github_repository.core-course-labs` resource has been defined to manage the existing repository.
- Visibility settings (`public`), description, permission issues, wiki and projects are configured.

3. **Setting up the main branch:**
- The `github_branch_default` resource was used to install the `master` branch as the main one.

4. **Protection of branches:**
- Protection rules have been created for `master` branch.
- The following parameters are configured: Prohibiting the deletion of branches (`allows_deletions = false`).
- Pull request requirements (minimum number of approvals, possibility to reject outdated reviews).
- Application of rules even for administrators (`enforce_admins = true`).

5. **Import existing resources:**
- The terraform import command was used to import an existing repository and branch protection rules.

6. **Applying the changes:**
- The commands `terraform init`, `terraform plan` and `terraform apply` have been executed to apply the configuration.