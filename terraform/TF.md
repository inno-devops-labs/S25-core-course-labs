# Terraform Lab Documentation

## Task 1: Introduction to Terraform

### Docker Infrastructure

#### Installation and Setup
1. Terraform has been successfully installed and configured
2. Docker provider initialized successfully
3. Infrastructure has been created and is running

#### Terraform Commands Output
##### State Show
```
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
    hostname                                    = "21720ab1ad24"
    id                                          = "21720ab1ad2498a335810c2e963850a8028848ccaa1c0d81da212807eb74ec42"
    image                                       = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {
        "max-file" = "5"
        "max-size" = "20m"
    }
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_mode                                = "bridge"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 6004
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
    id           = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx:latest"
    image_id     = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```

##### State List
```
docker_container.nginx
docker_image.nginx
```

##### Applied Changes Log
```
Successfully created and configured:
- NGINX Docker image pulled from Docker Hub
- Container running on port 8000 (mapped to internal port 80)
- Container name set to "tutorial"
```

##### Terraform Output
```
container_id = "21720ab1ad2498a335810c2e963850a8028848ccaa1c0d81da212807eb74ec42"
image_id = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx:latest"
```

## Task 2: GitHub Infrastructure with Terraform

### Repository Configuration
The GitHub infrastructure is configured with:
- Repository name: S25-core-course-labs
- Public visibility
- Branch protection rules for main branch
- Required status checks and pull request reviews
- Admin enforcement enabled
- Enhanced security features:
  - Advanced security enabled
  - Secret scanning enabled
  - Secret scanning push protection enabled
- Repository features:
  - Issues enabled
  - Projects enabled
  - Wiki enabled
  - Vulnerability alerts enabled

### Import Process
1. Created GitHub Personal Access Token with required permissions
2. Set up environment variable:
   ```bash
   export GITHUB_TOKEN=<token>
   ```
3. Initialized Terraform in the github directory:
   ```bash
   cd terraform/github
   terraform init
   ```
4. Imported existing repository:
   ```bash
   terraform import "github_repository.core-course-labs" "SergePolin/S25-core-course-labs"
   ```
5. Applied Terraform configuration:
   ```bash
   terraform plan
   terraform apply
   ```

### Best Practices Applied
1. Using environment variables for sensitive data (GITHUB_TOKEN)
2. Implementing branch protection rules for better security
3. Version constraints specified for providers
4. Resource naming follows Terraform conventions
5. Modular configuration structure (separate directories for Docker and GitHub)
6. Variables separated into dedicated variables.tf file
7. Enhanced security features enabled for the repository
8. Comprehensive documentation of all steps and configurations

### Azure Cloud Infrastructure
1. Azure CLI Authentication:
   ```bash
   az login
   ```
   - Successfully authenticated with Azure CLI
   - Selected subscription: "Main" (0ff37950-3e06-4453-aab7-a3633926c961)

2. Azure Provider Configuration:
   ```hcl
   terraform {
     required_providers {
       azurerm = {
         source  = "hashicorp/azurerm"
         version = "~> 3.0"
       }
     }
   }

   provider "azurerm" {
     features {}
     subscription_id = "0ff37950-3e06-4453-aab7-a3633926c961"
   }
   ```

3. Resource Group:
   - Created resource group "Devops_iu" in "eastus" region
   - Used as the base for all other resources

4. Network Infrastructure:
   - Virtual Network:
     - Name: "vnet-devops"
     - Address space: 10.0.0.0/16
     - Location: eastus
   - Subnet:
     - Name: "subnet-devops"
     - Address prefix: 10.0.1.0/24
   - Public IP:
     - Name: "vps-public-ip"
     - Allocation: Dynamic
     - SKU: Basic
   - Network Interface:
     - Name: "vps-nic"
     - Connected to subnet and public IP

5. Virtual Machine:
   - Name: "devops-vps"
   - Size: Standard_B1s
   - Image: Ubuntu Server 18.04-LTS
   - Authentication: SSH Key
   - Admin Username: adminuser
   - OS Disk: Standard LRS

6. Deployment Process:
   ```bash
   # Initialize Terraform
   terraform init
   
   # Plan the infrastructure
   terraform plan
   
   # Apply the configuration
   terraform apply
   ```

7. Resources Created:
   - 1 Resource Group
   - 1 Virtual Network
   - 1 Subnet
   - 1 Public IP
   - 1 Network Interface
   - 1 Linux Virtual Machine

8. Deployment Results:
   - All resources successfully created
   - Deployment completed in approximately 55 seconds
   - Network and VM configurations applied successfully

9. Challenges and Solutions:
   - Initial resource group already existed: Resolved by creating new resources within the existing group
   - SSH key configuration: Successfully configured using inline public key
   - Network dependencies: Handled automatically by Terraform's dependency management

10. Best Practices Applied:
    - Resource naming follows Azure conventions
    - Network segmentation with dedicated subnet
    - Secure VM access with SSH key authentication
    - Dynamic IP allocation for cost optimization
    - Basic SKU selection for development environment