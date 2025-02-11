# Terraform practice report

## Initial setup

main.tf

```tf
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

```txt
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

```txt
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
4. Issue 1: the guide to define VM resource from Yandex is not very clear: it does mention that you should create a network and set up a network interface in a VM (among boot drive and other things), but it does not provide examples on the same page. Borrowed a full example from the provider docs.
5. I've defined the network, subnet and VM resources based on the docs and the IDE hints (Terraform linter in VSCode)
6. I've determined the image id for the latest Ubuntu release using the `yc` CLI tool and used it in the resource creation
7. Ran `terraform fmt && terraform validate` to check the config
8. Ran `terraform plan && terraform apply` to apply the changes using credentials from my environment set up in step 2
9. **Output:**

```txt
❯ terraform show
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-06T21:07:48Z"
    folder_id                 = "<<redacted>>"
    fqdn                      = "<<redacted>>.auto.internal"
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    id                        = "<<redacted>>"
    metadata                  = {
        "ssh-keys" = <<-EOT
            <<redacted>>
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm5p62alunk94vcr0no"
        disk_id     = "fhm5p62alunk94vcr0no"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd82odtq5h79jo7ffss3"
            size       = 10
            type       = "network-hdd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "10.0.100.33"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:62:28:84:48"
        nat                = true
        nat_ip_address     = "<<redacted>>"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "<<redacted>>"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}

# yandex_vpc_network.network-tfproject:
resource "yandex_vpc_network" "network-tfproject" {
    created_at                = "2025-02-06T21:07:44Z"
    default_security_group_id = "<<redacted>>"
    folder_id                 = "<<redacted>>"
    id                        = "<<redacted>>"
    labels                    = {}
    name                      = "network-1"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-tfproject:
resource "yandex_vpc_subnet" "subnet-tfproject" {
    created_at     = "2025-02-06T21:07:47Z"
    folder_id      = "<<redacted>>"
    id             = "<<redacted>>"
    labels         = {}
    name           = "subnet-1"
    network_id     = "<<redacted>>"
    v4_cidr_blocks = [
        "10.0.100.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

> Note: run `terraform destroy` in the end to not burn through the free trial 🙂

## GitHub

- Issue 2: default branch setting is deprecated
- Issue 3: branch protection with status checks does not play well with path-filter conditions on workflows
- Issue 4: Difference between rulesets and branch protections was unclear. The wording for option on requiring PRs to push to protected branch in Terraform was unclear as well.

1. `export GITHUB_TOKEN=$(gh auth token)` to authenticate terraform
2. `terraform init` to initialize after copying the initial provider template from the provided docs
3. `terraform import github_repository.lab-repo S25-core-course-labs` to import the repository (had to check the docs to understand the second argument)
4. `terraform plan && terraform apply` to apply the changes (some issues with the default branch and weird settings naming)
5. **Output:**

```txt
❯ terraform apply
github_repository.lab_repo: Refreshing state... [id=S25-core-course-labs]
github_branch_default.default: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.push-protection: Refreshing state... [id=BPR_kwDONxz2aM4DipGL]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_protection.push-protection will be updated in-place
  ~ resource "github_branch_protection" "push-protection" {
        id                              = "BPR_kwDONxz2aM4DipGL"
        # (10 unchanged attributes hidden)

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 0
        }

        # (1 unchanged block hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_protection.push-protection: Modifying... [id=BPR_kwDONxz2aM4DipGL]
github_branch_protection.push-protection: Modifications complete after 5s [id=BPR_kwDONxz2aM4DipGL]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

## Best Practices

A good read [here](https://www.terraform-best-practices.com/code-structure)

- No secrets hardcoded or stored in the repo
- Clean .gitignore (with lock files commited as suggested by Terraform docs)
- Meaningful names for files, resources and variables, since like any code tf files should remain readable
- Variables are used where applicable but are not forced into situations where they make no sense (e.g. variable for amount of cores or a name of the network that is not reused elsewhere, since this is supposed to be a static information)
- Use of modules to make the changes in different infrastructure providers coherent by calling a single main.tf
  - Also helps with provider caches and state

## GitHub Teams

- for f**ks sake, Microsoft has ruined it for me once again
  - Issue 5: `this resource can only be used in the context of an organization, "FallenChromium" is a user` actually meant that this token didn't have enough permissions
  - Issue 6: TF state was confused by me using a PAT with a non-organization scope, so I had to wipe .tfstate files before it started working again
  - Issue 7: The worst for the last. The linter and the docs said I should use "owner" rather than "organization" setting in the provider, but doing so raised `this resource can only be used in the context of an organization, "inno-devops-fallenchromium" is a user` (even though IT IS an organization and not a user) and 401s on wiping the tfstate again. Bloody cursed.
  - **Output:**

```txt
❯ terraform apply

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_repository.example_repo will be created
  + resource "github_repository" "example_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "An example repository managed by Terraform"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "test-repo"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false
    }

  # github_team.admins will be created
  + resource "github_team" "admins" {
      + create_default_maintainer = false
      + description               = "Team with full access"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Admins"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.developers will be created
  + resource "github_team" "developers" {
      + create_default_maintainer = false
      + description               = "Team of developers"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Developers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.qa will be created
  + resource "github_team" "qa" {
      + create_default_maintainer = false
      + description               = "Quality Assurance team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "QA"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.admins_access will be created
  + resource "github_team_repository" "admins_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "test-repo"
      + team_id    = (known after apply)
    }

  # github_team_repository.developers_access will be created
  + resource "github_team_repository" "developers_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "test-repo"
      + team_id    = (known after apply)
    }

  # github_team_repository.qa_access will be created
  + resource "github_team_repository" "qa_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "test-repo"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.
╷
│ Warning: Argument is deprecated
│ 
│   with provider["registry.terraform.io/hashicorp/github"],
│   on main.tf line 2, in provider "github":
│    2:   organization = "inno-devops-fallenchromium"
│ 
│ Use owner (or GITHUB_OWNER) instead of organization (or GITHUB_ORGANIZATION)
│ 
│ (and one more similar warning elsewhere)
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.developers: Creating...
github_team.qa: Creating...
github_team.admins: Creating...
github_repository.example_repo: Creating...
github_team.admins: Still creating... [10s elapsed]
github_team.developers: Still creating... [10s elapsed]
github_team.qa: Still creating... [10s elapsed]
github_repository.example_repo: Still creating... [10s elapsed]
github_team.developers: Creation complete after 18s [id=12133679]
github_team.qa: Creation complete after 18s [id=12133680]
github_team.admins: Creation complete after 19s [id=12133681]
github_repository.example_repo: Creation complete after 19s [id=test-repo]
github_team_repository.admins_access: Creating...
github_team_repository.qa_access: Creating...
github_team_repository.developers_access: Creating...
github_team_repository.admins_access: Creation complete after 5s [id=12133681:test-repo]
github_team_repository.developers_access: Creation complete after 5s [id=12133679:test-repo]
github_team_repository.qa_access: Creation complete after 6s [id=12133680:test-repo]
╷
│ Warning: Argument is deprecated
│ 
│   with provider["registry.terraform.io/hashicorp/github"],
│   on main.tf line 2, in provider "github":
│    2:   organization = "inno-devops-fallenchromium"
│ 
│ Use owner (or GITHUB_OWNER) instead of organization (or GITHUB_ORGANIZATION)
╵

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```
