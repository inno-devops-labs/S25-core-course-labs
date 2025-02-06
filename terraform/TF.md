# Terraform overview

## Introduction to Terraform

Terraform is an infrastructure-as-code tool that allows users to define and provision cloud resources declaratively. By following best practices, we ensure code quality, security, and maintainability.

### Best Practices Applied

#### 1. Code Quality & Validation

To ensure consistent and error-free configurations:

```bash
# Enforce formatting across all configuration files
terraform fmt -recursive

# Validate syntax and logical correctness
terraform validate
```

## Sensitive data handling

Sensitive data such as API tokens and private keys are stored securely and excluded from version control:

```text
# .gitignore entry to exclude sensitive files
*.auto.tfvars
*.tfvars
```

## Version Control Safety

Files ignored by Git:

.terraform/ – Terraform working directory
*.tfstate – State files
*.tfstate.backup – Backup state files
*.auto.tfvars – Auto-applied variable files

Committed files:

main.tf – Core configuration
variables.tf – Variable declarations
TF.md – Documentation

## Provider Management

Provider versions are strictly constrained to ensure stability:

```hcl
provider "yandex" {
  version = "~> 0.76"
}
```

### Yandex Cloud Infrastructure

Setup was done using official tutorial:
[link](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1)

## Github Terraform

### Best practices

1. Version pinning
   Ensures consistency by pinning the GitHub provider to 6.0.
2. Environment variables
   Protects sensitive data by using the GITHUB_TOKEN environment variable for the API token.
3. Descriptive resource names
   Uses clear names like github_repository.devops_labs and github_branch_default.default_branch for better readability.
4. Use of outputs for key values
   Exposes important details like the repository URL and default branch via outputs.
5. Branch protection
   Enforces rules on the default branch: requires conversation resolution, restricts admins, and mandates one approving review.
6. No hardcoding secrets
   Declares the token variable as sensitive to prevent exposing credentials.

### Outputs

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\terraform\github_tf> terraform apply
var.token
GitHub personal access token

Enter a value:

github_repository.devops_labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
+ create
  ~ update in-place

Terraform will perform the following actions:

# github_branch_default.default_branch will be created
+ resource "github_branch_default" "default_branch" {
   + branch     = "master"
   + id         = (known after apply)
   + repository = "S25-core-course-labs"
     }

# github_branch_protection.branch_protection will be created
+ resource "github_branch_protection" "branch_protection" {
   + allows_deletions                = false
   + allows_force_pushes             = false
   + blocks_creations                = false
   + enforce_admins                  = true
   + id                              = (known after apply)
   + pattern                         = "master"
   + repository_id                   = "S25-core-course-labs"
   + require_conversation_resolution = true
   + require_signed_commits          = false
   + required_linear_history         = false

   + required_pull_request_reviews {
      + required_approving_review_count = 1
        }
        }

# github_repository.devops_labs will be updated in-place
~ resource "github_repository" "devops_labs" {
~ description                 = "Repository for DevOps labs at Innopolis University" -> "DevOps Labs Repository"
+ gitignore_template          = "VisualStudio"
- has_downloads               = true -> null
~ has_issues                  = false -> true
~ has_wiki                    = false -> true
id                          = "S25-core-course-labs"
+ license_template            = "mit"
name                        = "S25-core-course-labs"
# (29 unchanged attributes hidden)
}

Plan: 2 to add, 1 to change, 0 to destroy.

Changes to Outputs:
+ default_branch = "master"

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.
Enter a value:
github_repository.devops_labs: Modifying... [id=S25-core-course-labs]
github_repository.devops_labs: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.default_branch: Creating...
github_branch_default.default_branch: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.branch_protection: Creating...
github_branch_protection.branch_protection: Creation complete after 5s [id=BPR_kwDONvaLAc4DifkR]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

default_branch = "master"
repository_url = "https://github.com/RwKaLs/S25-core-course-labs"
```

## Docker task

Task was done fully using the following tutorial:
[link](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)

### Required outputs for the task

```text
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\terraform\docker_tf> terraform state show docker_container.nginx
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
hostname                                    = "a89dce7f2f3e"
id                                          = "a89dce7f2f3ea436ed6beb09909820f8b80d55a5f5bfee3e72c1cc59c014b023"
image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
init                                        = false
ipc_mode                                    = "private"
log_driver                                  = "json-file"
logs                                        = false
max_retry_count                             = 0
memory                                      = 0
memory_swap                                 = 0
must_run                                    = true
name                                        = "custom_container"
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

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_image.nginx:
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\terraform\docker_tf> terraform state list docker_container.nginx
docker_container.nginx
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\terraform\docker_tf> terraform state list docker_image.nginx
docker_image.nginx
PS C:\Users\egora\PycharmProjects\S25-core-course-labs\terraform\docker_tf> terraform output
custom_container_id = "a89dce7f2f3ea436ed6beb09909820f8b80d55a5f5bfee3e72c1cc59c014b023"
custom_container_image = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
custom_container_name = "custom_container"
```
