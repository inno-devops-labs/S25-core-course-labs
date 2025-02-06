# TF

## Best Practices Implemented

1. **Configuration Management**
   - Using variables for configurable values
   - Consistent resource naming patterns
   - Proper resource attribute organization

2. **Output Management**
   - Defining useful outputs for resource properties
   - Structured output format for better readability

3. **Security Best Practices**
   - Using environment variables for sensitive information (TF_VAR_github_token)
   - Not committing sensitive tokens directly in code

## Docker Task

- `terraform show`

```bash
# docker_container.app_container:

resource "docker_container" "app_container" {
attach = false
bridge = [90mnull[0m[0m
command = [
"redis-server",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_set = [90mnull[0m[0m
cpu_shares = 0
domainname = [90mnull[0m[0m
entrypoint = [
"docker-entrypoint.sh",
]
env = []
hostname = "a8348491799f"
id = "a8348491799fadce35441b972870398cb42da6ca52ac168aa07f5942642624cb"
image = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = [90mnull[0m[0m
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = [90mnull[0m[0m
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "bridge"
pid_mode = [90mnull[0m[0m
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_signal = [90mnull[0m[0m
stop_timeout = 0
tty = false
user = [90mnull[0m[0m
userns_mode = [90mnull[0m[0m
wait = false
wait_timeout = 60
working_dir = "/data"

    ports {
        external = 4000
        internal = 4000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}

# docker_image.app_image:

resource "docker_image" "app_image" {
id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79aredis:latest"
image_id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
name = "redis:latest"
repo_digest = "redis@sha256:eadf354977d428e347d93046bb1a5569d701e8deb68f090215534a99dbcb23b9"
}
```

- `terraform state list`

```bash
docker_container.app_container
docker_image.app_image
```

- `terraform state show docker_container.app_container`

```bash
# docker_container.app_container:

resource "docker_container" "app_container" {
attach = false
bridge = null
command = [
"redis-server",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_set = null
cpu_shares = 0
domainname = null
entrypoint = [
"docker-entrypoint.sh",
]
env = []
hostname = "a8348491799f"
id = "a8348491799fadce35441b972870398cb42da6ca52ac168aa07f5942642624cb"
image = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = null
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = null
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "bridge"
pid_mode = null
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_signal = null
stop_timeout = 0
tty = false
user = null
userns_mode = null
wait = false
wait_timeout = 60
working_dir = "/data"

    ports {
        external = 4000
        internal = 4000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}
```

- `terraform state show docker_image.app_image`

```bash
resource "docker_image" "app_image" {
   id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79aredis:latest"
   image_id = "sha256:9fba7e5fadd5fc42b7aaf71b85f2b1de951fc870f97d0d64e5eb06243be7c79a"
   name = "redis:latest"
   repo_digest = "redis@sha256:eadf354977d428e347d93046bb1a5569d701e8deb68f090215534a99dbcb23b9"
}
```

### Change container name

```bash
terraform apply
```

```bash
latest" # forces replacement
~ init = false -> (known after apply)
~ ipc_mode = "private" -> (known after apply)
~ log_driver = "json-file" -> (known after apply) - log_opts = {} -> null - max_retry_count = 0 -> null - memory = 0 -> null - memory_swap = 0 -> null
~ name = "app_python" -> "app_python_changed" # forces replacement
~ network_data = [
- {
- gateway = "172.17.0.1"
- global_ipv6_prefix_length = 0
- ip_address = "172.17.0.2"
- ip_prefix_length = 16
- mac_address = "02:42:ac:11:00:02"
- network_name = "bridge"
# (2 unchanged attributes hidden)
},
] -> (known after apply)

```

### terraform output

```bash
container_image = "redis:latest"
container_name = "app_python_changed"
container_port = tolist([
{
"external" = 4000
"internal" = 4000
"ip" = "0.0.0.0"
"protocol" = "tcp"
},
])

```

## AWS Task

**Set up steps:**

1. Install cloud cli
2. Create service account
3. Generate tokens and ids
4. Run `terraform apply`

**Outputs**:

- `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:

- create

Terraform will perform the following actions:

# aws_instance.app_server will be created

- resource "aws_instance" "app_server" {

  - ami = "ami-830c94e3"
  - arn = (known after apply)
  - associate_public_ip_address = (known after apply)
  - availability_zone = (known after apply)
  - cpu_core_count = (known after apply)
  - cpu_threads_per_core = (known after apply)
  - disable_api_stop = (known after apply)
  - disable_api_termination = (known after apply)
  - ebs_optimized = (known after apply)
  - get_password_data = false
  - host_id = (known after apply)
  - host_resource_group_arn = (known after apply)
  - iam_instance_profile = (known after apply)
  - id = (known after apply)
  - instance_initiated_shutdown_behavior = (known after apply)
  - instance_state = (known after apply)
  - instance_type = "t2.micro"
  - ipv6_address_count = (known after apply)
  - ipv6_addresses = (known after apply)
  - key_name = (known after apply)
  - monitoring = (known after apply)
  - outpost_arn = (known after apply)
  - password_data = (known after apply)
  - placement_group = (known after apply)
  - placement_partition_number = (known after apply)
  - primary_network_interface_id = (known after apply)
  - private_dns = (known after apply)
  - private_ip = (known after apply)
  - public_dns = (known after apply)
  - public_ip = (known after apply)
  - secondary_private_ips = (known after apply)
  - security_groups = (known after apply)
  - source_dest_check = true
  - subnet_id = (known after apply)
  - tags = {
    - "Name" = "ExampleAppServerInstance"
      }
  - tags_all = {
    - "Name" = "ExampleAppServerInstance"
      }
  - tenancy = (known after apply)
  - user_data = (known after apply)
  - user_data_base64 = (known after apply)
  - user_data_replace_on_change = false
  - vpc_security_group_ids = (known after apply)

  - capacity_reservation_specification (known after apply)

  - cpu_options (known after apply)

  - ebs_block_device (known after apply)

  - enclave_options (known after apply)

  - ephemeral_block_device (known after apply)

  - maintenance_options (known after apply)

  - metadata_options (known after apply)

  - network_interface (known after apply)

  - private_dns_name_options (known after apply)

  - root_block_device (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value: yes

aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Still creating... [20s elapsed]
aws_instance.app_server: Creation complete after 26s [id=i-0ae3c813911b89ca3]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

```

- `terraform state list`:

```bash
aws_instance.app_server
```

- `terraform show`:

```bash
# aws_instance.app_server:

resource "aws_instance" "app_server" {
ami = "ami-830c94e3"
arn = "arn:aws:ec2:us-west-2:820242942180:instance/i-0ae3c813911b89ca3"
associate_public_ip_address = true
availability_zone = "us-west-2b"
cpu_core_count = 1
cpu_threads_per_core = 1
disable_api_stop = false
disable_api_termination = false
ebs_optimized = false
get_password_data = false
hibernation = false
host_id = null
iam_instance_profile = null
id = "i-0ae3c813911b89ca3"
instance_initiated_shutdown_behavior = "stop"
instance_state = "running"
instance_type = "t2.micro"
ipv6_address_count = 0
ipv6_addresses = []
key_name = null
monitoring = false
outpost_arn = null
password_data = null
placement_group = null
placement_partition_number = 0
primary_network_interface_id = "eni-038bc5ea37a91ac16"
private_dns = "ip-172-31-22-32.us-west-2.compute.internal"
private_ip = "172.31.22.32"
public_dns = "ec2-34-223-218-149.us-west-2.compute.amazonaws.com"
public_ip = "34.223.218.149"
secondary_private_ips = []
security_groups = [
"default",
]
source_dest_check = true
subnet_id = "subnet-05f802481936ed38e"
tags = {
"Name" = "ExampleAppServerInstance"
}
tags_all = {
"Name" = "ExampleAppServerInstance"
}
tenancy = "default"
user_data_replace_on_change = false
vpc_security_group_ids = [
"sg-0ef1dfb2245c67718",
]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    cpu_options {
        amd_sev_snp      = null
        core_count       = 1
        threads_per_core = 1
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        kms_key_id            = null
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-02c72cbe195cc4f0a"
        volume_size           = 8
        volume_type           = "standard"
    }

}
```

- `terraform state show aws_instance.app_server`:

```bash
# aws_instance.app_server:

resource "aws_instance" "app_server" {
ami = "ami-830c94e3"
arn = "arn:aws:ec2:us-west-2:820242942180:instance/i-0ae3c813911b89ca3"
associate_public_ip_address = true
availability_zone = "us-west-2b"
cpu_core_count = 1
cpu_threads_per_core = 1
disable_api_stop = false
disable_api_termination = false
ebs_optimized = false
get_password_data = false
hibernation = false
host_id = null
iam_instance_profile = null
id = "i-0ae3c813911b89ca3"
instance_initiated_shutdown_behavior = "stop"
instance_state = "running"
instance_type = "t2.micro"
ipv6_address_count = 0
ipv6_addresses = []
key_name = null
monitoring = false
outpost_arn = null
password_data = null
placement_group = null
placement_partition_number = 0
primary_network_interface_id = "eni-038bc5ea37a91ac16"
private_dns = "ip-172-31-22-32.us-west-2.compute.internal"
private_ip = "172.31.22.32"
public_dns = "ec2-34-223-218-149.us-west-2.compute.amazonaws.com"
public_ip = "34.223.218.149"
secondary_private_ips = []
security_groups = [
"default",
]
source_dest_check = true
subnet_id = "subnet-05f802481936ed38e"
tags = {
"Name" = "ExampleAppServerInstance"
}
tags_all = {
"Name" = "ExampleAppServerInstance"
}
tenancy = "default"
user_data_replace_on_change = false
vpc_security_group_ids = [
"sg-0ef1dfb2245c67718",
]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    cpu_options {
        amd_sev_snp      = null
        core_count       = 1
        threads_per_core = 1
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        kms_key_id            = null
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-02c72cbe195cc4f0a"
        volume_size           = 8
        volume_type           = "standard"
    }

}

```

## Github Task

### Export Variables

```bash
export TF_VAR_github_token="your-token-here"
```

### Import Configuration

```bash
terraform import "github_repository.core-course-labs" "S25-core-course-labs"
```

### Output

- `terraform state list`:

```bash
github_repository.core-course-labs:
  Import ID: github_repository.core-course-labs
```

- `terraform state show github_branch_protection.main`:

```bash
# github_branch_protection.main:

resource "github_branch_protection" "main" {
allows_deletions = false
allows_force_pushes = false
enforce_admins = false
id = "BPR_kwDONx0tmc4DikOO"
lock_branch = false
pattern = "main"
repository_id = "R_kgDONx0tmQ"
require_conversation_resolution = false
require_signed_commits = false
required_linear_history = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = true
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }

    required_status_checks {
        strict = true
    }

}
```

- `terraform state show github_repository.core-course-labs`:

```bash
# github_repository.core-course-labs:

resource "github_repository" "core-course-labs" {
allow_auto_merge = false
allow_merge_commit = true
allow_rebase_merge = true
allow_squash_merge = true
allow_update_branch = false
archived = false
auto_init = false
default_branch = "master"
delete_branch_on_merge = false
description = "DevOps Engineering Course Labs"
etag = "W/\"5e5d83275ec8daef2caf5078a7c5bede076eebe218d2e96cfcbae381b05c808d\""
full_name = "HaidarJbeily7/S25-core-course-labs"
git_clone_url = "git://github.com/HaidarJbeily7/S25-core-course-labs.git"
has_discussions = false
has_downloads = false
has_issues = true
has_projects = false
has_wiki = true
homepage_url = null
html_url = "https://github.com/HaidarJbeily7/S25-core-course-labs"
http_clone_url = "https://github.com/HaidarJbeily7/S25-core-course-labs.git"
id = "S25-core-course-labs"
is_template = false
merge_commit_message = "PR_TITLE"
merge_commit_title = "MERGE_MESSAGE"
name = "S25-core-course-labs"
node_id = "R_kgDONx0tmQ"
primary_language = null
private = false
repo_id = 924659097
squash_merge_commit_message = "COMMIT_MESSAGES"
squash_merge_commit_title = "COMMIT_OR_PR_TITLE"
ssh_clone_url = "git@github.com:HaidarJbeily7/S25-core-course-labs.git"
svn_url = "https://github.com/HaidarJbeily7/S25-core-course-labs"
topics = []
visibility = "public"
vulnerability_alerts = false
web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "enabled"
        }
        secret_scanning_push_protection {
            status = "enabled"
        }
    }

}

```

## Bonus Task

- `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:

- create

Terraform will perform the following actions:

# github_team.admins will be created

- resource "github_team" "admins" {
  - create_default_maintainer = false
  - description = "Team with admin access"
  - etag = (known after apply)
  - id = (known after apply)
  - members_count = (known after apply)
  - name = "administrators-exploring-cc"
  - node_id = (known after apply)
  - parent_team_read_id = (known after apply)
  - parent_team_read_slug = (known after apply)
  - privacy = "closed"
  - slug = (known after apply)
    }

# github_team.developers will be created

- resource "github_team" "developers" {
  - create_default_maintainer = false
  - description = "Team with write access"
  - etag = (known after apply)
  - id = (known after apply)
  - members_count = (known after apply)
  - name = "developers-exploring-cc"
  - node_id = (known after apply)
  - parent_team_read_id = (known after apply)
  - parent_team_read_slug = (known after apply)
  - privacy = "closed"
  - slug = (known after apply)
    }

# github_team.viewers will be created

- resource "github_team" "viewers" {
  - create_default_maintainer = false
  - description = "Team with read access"
  - etag = (known after apply)
  - id = (known after apply)
  - members_count = (known after apply)
  - name = "viewers-exploring-cc"
  - node_id = (known after apply)
  - parent_team_read_id = (known after apply)
  - parent_team_read_slug = (known after apply)
  - privacy = "closed"
  - slug = (known after apply)
    }

# github_team_repository.admin_repo will be created

- resource "github_team_repository" "admin_repo" {
  - etag = (known after apply)
  - id = (known after apply)
  - permission = "admin"
  - repository = "cc-tool"
  - team_id = (known after apply)
    }

# github_team_repository.dev_repo will be created

- resource "github_team_repository" "dev_repo" {
  - etag = (known after apply)
  - id = (known after apply)
  - permission = "push"
  - repository = "cc-tool"
  - team_id = (known after apply)
    }

# github_team_repository.viewer_repo will be created

- resource "github_team_repository" "viewer_repo" {
  - etag = (known after apply)
  - id = (known after apply)
  - permission = "pull"
  - repository = "cc-tool"
  - team_id = (known after apply)
    }

Plan: 6 to add, 0 to change, 0 to destroy.

Changes to Outputs:

- admin_team_id = (known after apply)
  ~ admin_team_name = "administrators" -> "administrators-exploring-cc"
- developers_team_id = (known after apply)
  ~ developers_team_name = "developers" -> "developers-exploring-cc"
- viewers_team_id = (known after apply)
  ~ viewers_team_name = "viewers" -> "viewers-exploring-cc"

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value: yes

github_team.admins: Creating...
github_team.developers: Creating...
github_team.viewers: Creating...
github_team.viewers: Still creating... [10s elapsed]
github_team.admins: Still creating... [10s elapsed]
github_team.developers: Still creating... [10s elapsed]
github_team.viewers: Creation complete after 15s [id=12132225]
github_team_repository.viewer_repo: Creating...
github_team.admins: Creation complete after 15s [id=12132226]
github_team_repository.admin_repo: Creating...
github_team.developers: Creation complete after 15s [id=12132227]
github_team_repository.dev_repo: Creating...
github_team_repository.viewer_repo: Creation complete after 5s [id=12132225:cc-tool]
github_team_repository.admin_repo: Creation complete after 5s [id=12132226:cc-tool]
github_team_repository.dev_repo: Creation complete after 6s [id=12132227:cc-tool]

Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

```

- `terraform output`:

```bash
admin_team_id = "12132226"
admin_team_name = "administrators-exploring-cc"
developers_team_id = "12132227"
developers_team_name = "developers-exploring-cc"
viewers_team_id = "12132225"
viewers_team_name = "viewers-exploring-cc"
```

- `terraform show`:

```bash
# github_team.admins:

resource "github_team" "admins" {
create_default_maintainer = false
description = "Team with admin access"
etag = "W/\"a594d267ef91f5245c6ae2c1e396442683420208f8227ad311b4f6bbb39192ab\""
id = "12132226"
ldap_dn = null
members_count = 0
name = "administrators-exploring-cc"
node_id = "T_kwDOC88mj84AuR-C"
parent_team_id = null
parent_team_read_id = null
parent_team_read_slug = null
privacy = "closed"
slug = "administrators-exploring-cc"
}

# github_team.developers:

resource "github_team" "developers" {
create_default_maintainer = false
description = "Team with write access"
etag = "W/\"05c718c772daea583ba14532feb33cee9a4d4f1bbbc1ab210a280c7273bf6b3d\""
id = "12132227"
ldap_dn = null
members_count = 0
name = "developers-exploring-cc"
node_id = "T_kwDOC88mj84AuR-D"
parent_team_id = null
parent_team_read_id = null
parent_team_read_slug = null
privacy = "closed"
slug = "developers-exploring-cc"
}

# github_team.viewers:

resource "github_team" "viewers" {
create_default_maintainer = false
description = "Team with read access"
etag = "W/\"de09a9aa901f35d365c91f0cc5b1490d1446b81b79ff1ce05971ff9174309e46\""
id = "12132225"
ldap_dn = null
members_count = 0
name = "viewers-exploring-cc"
node_id = "T_kwDOC88mj84AuR-B"
parent_team_id = null
parent_team_read_id = null
parent_team_read_slug = null
privacy = "closed"
slug = "viewers-exploring-cc"
}

# github_team_repository.admin_repo:

resource "github_team_repository" "admin_repo" {
etag = "W/\"22cf7e7da5083ebf35ce9a76799baf33c316fcee727327278d1a5fed75efe930\""
id = "12132226:cc-tool"
permission = "admin"
repository = "cc-tool"
team_id = "12132226"
}

# github_team_repository.dev_repo:

resource "github_team_repository" "dev_repo" {
etag = "W/\"db65ba937dcef8156c20534968381523e6b3f3d4c59911541fd515a1e2c0932d\""
id = "12132227:cc-tool"
permission = "push"
repository = "cc-tool"
team_id = "12132227"
}

# github_team_repository.viewer_repo:

resource "github_team_repository" "viewer_repo" {
etag = "W/\"1360db2f859ef651e0455b5c2727c42e1ae68db9171046dcac3785330dd8bf8b\""
id = "12132225:cc-tool"
permission = "pull"
repository = "cc-tool"
team_id = "12132225"
}

Outputs:

admin_team_id = "12132226"
admin_team_name = "administrators-exploring-cc"
developers_team_id = "12132227"
developers_team_name = "developers-exploring-cc"
viewers_team_id = "12132225"
viewers_team_name = "viewers-exploring-cc"

```

- `terraform state list`:

```bash
github_team.admins
github_team.developers
github_team.viewers
github_team_repository.admin_repo
github_team_repository.dev_repo
github_team_repository.viewer_repo
```
