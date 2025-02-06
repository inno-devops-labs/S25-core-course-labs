## Terraform Output

- **Container ID**: c2795b5772d3d5b47bde8bda83b016c81bc174281c9ec4da4aa1dedea0e6b779
- **Container Name**: docker_container.nginx


- **Container ID**: sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx:latest
- **Container Name**: docker_image.nginx


## Terraform state list
- docker_container.nginx
- docker_image.nginx

## Terraform state show 
- **docker_container.nginx**

Output:
```hcl
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach            = false
    bridge            = null
    command           = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    cpu_set           = null
    cpu_shares        = 0
    domainname        = null
    entrypoint        = [
        "/docker-entrypoint.sh",
    ]
    env               = []
    gateway           = "172.17.0.1"
    hostname          = "c2795b5772d3"
    id                = "c2795b5772d3d5b47bde8bda83b016c81bc174281c9ec4da4aa1dedea0e6b779"
    image             = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    init              = false
    ip_address        = "172.17.0.2"
    ip_prefix_length  = 16
    ipc_mode          = "private"
    log_driver        = "json-file"
    logs              = false
    max_retry_count   = 0
    memory            = 0
    memory_swap       = 0
    must_run          = true
    name              = "example-nginx"
    network_data      = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            network_name              = "bridge"
        },
    ]
    network_mode      = "default"
    pid_mode          = null
    privileged        = false
    publish_all_ports = false
    read_only         = false
    remove_volumes    = true
    restart           = "no"
    rm                = false
    runtime           = "runc"
    security_opts     = []
    shm_size          = 64
    start             = true
    stdin_open        = false
    stop_signal       = "SIGQUIT"
    stop_timeout      = 0
    tty               = false
    user              = null
    userns_mode       = null
    working_dir       = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

- **docker_image.nginx**

Output:
```hcl
# docker_image.nginx:
resource "docker_image" "nginx" {
    id          = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442dfnginx:latest"
    image_id    = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    latest      = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    name        = "nginx:latest"
    repo_digest = "nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
}
```

After updating name of Docker container and perform new apply command
```bash
terraform apply -var="container_name=Lab4"
```

Outputs are:
- **Container ID** = "ca0c2b0cde785e7a8a451920d00a25e1c99516614abcaed40d3c526c33101deb"

- **Container Name**: "Lab4"


## Terraform for GitHub

Inside folder github-infrastracture all needs files for interact with github repository.
Also I load environment variable with token to GitHub

Run commands:
```bash 
terraform init 
```

```bash
terraform import "github_repository.S25-core-course-labs" "S25-core-course-labs"  # for make state
```

```bash
terraform apply -var="github_token=$env:GITHUB_TOKEN"
```

After last command output is:

```

github_repository.S25-core-course-labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_repository.S25-core-course-labs will be updated in-place
  ~ resource "github_repository" "S25-core-course-labs" {
      ~ description                 = "Repository with terraform" -> "Repository description with Terraform"
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (35 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.S25-core-course-labs: Modifying... [id=S25-core-course-labs]
github_repository.S25-core-course-labs: Modifications complete after 2s [id=S25-core-course-labs]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

repository_url = "https://github.com/DeHopen/S25-core-course-labs"
```



