# Terraform Infrastructure Documentation

This document describes the Terraform configuration for deploying a Python application using Docker on Yandex Cloud and managing a GitHub repository.

## Project Structure

```
terraform/
├── docker/              # Local Docker deployment
│   ├── main.tf         # Docker provider configuration
│   ├── variables.tf    # Input variables
│   └── outputs.tf      # Output definitions
├── yandex/             # Yandex Cloud deployment
│   ├── main.tf         # Main infrastructure configuration
│   ├── variables.tf    # Input variables
│   ├── versions.tf     # Provider version constraints
│   └── outputs.tf      # Output definitions
└── github/             # GitHub repository management
    ├── main.tf         # Repository and branch configuration
    ├── variables.tf    # Input variables
    ├── versions.tf     # Provider version constraints
    └── outputs.tf      # Output definitions
```

## 1. Yandex Cloud Configuration

### Prerequisites

1. Yandex Cloud account with billing enabled
2. Service account with roles:
   - `editor`
   - `compute.admin`
   - `vpc.user`
3. Service account key file (`key.json`)

### Infrastructure Components

1. **Compute Instance**
   - Ubuntu-based VM
   - Docker installation via user-data script
   - Python application deployment using Docker

2. **Network Resources**
   - Uses default VPC network
   - Uses default subnet in ru-central1-a
   - NAT enabled for public access

### Variables

| Name | Description | Type | Default |
|------|-------------|------|---------|
| folder_id | Yandex Cloud Folder ID | string | - |
| cloud_id | Yandex Cloud ID | string | - |
| zone | Yandex Cloud Zone | string | "ru-central1-a" |
| image_id | Ubuntu image ID | string | "fd8308aanqma9v5n76aj" |
| vm_resources | VM resources configuration | object | {cores = 2, memory = 2, core_fraction = 100} |
| app_port | Application port to expose | number | 5000 |

### Outputs

| Name | Description |
|------|-------------|
| external_ip_address | Public IP address of the instance |
| internal_ip_address | Private IP address of the instance |
| instance_fqdn | Fully Qualified Domain Name of the instance |
| app_url | URL to access the application |
| instance_status | Current status of the instance |

## 2. GitHub Configuration

### Prerequisites

1. GitHub account
2. Personal Access Token with permissions:
   - `repo` (Full control of private repositories)
   - `admin:org` (Full control of orgs and teams)
   - `delete_repo` (Delete repositories)

### Infrastructure Components

1. **Repository Configuration**
   - Repository name and description
   - Public visibility
   - Issues, wiki, and projects enabled
   - Branch protection rules

2. **Branch Management**
   - Default branch set to "master"
   - Branch protection rules
   - Auto-deletion of merged branches

### Variables

| Name | Description | Type | Default |
|------|-------------|------|---------|
| github_token | GitHub Personal Access Token | string | - |
| repository_name | Name of the GitHub repository | string | "S25-core-course-labs" |
| repository_description | Description of the repository | string | "Core course labs for S25" |
| repository_visibility | Repository visibility | string | "public" |
| default_branch | Default branch name | string | "master" |

### Outputs

| Name | Description |
|------|-------------|
| repository_url | URL of the created repository |
| repository_git_clone_url | Git clone URL of the repository |
| repository_default_branch | Default branch of the repository |

## Best Practices Implemented

1. **Variable Management**
   - All configurable values defined as variables
   - Meaningful variable descriptions
   - Type constraints for all variables
   - Sensible default values where appropriate

2. **Resource Organization**
   - Logical grouping of resources by provider
   - Clear resource naming
   - Use of data sources for existing resources

3. **Security**
   - SSH key-based authentication for VMs
   - Branch protection rules for repository
   - Required pull request reviews
   - Minimal required permissions

4. **Infrastructure as Code**
   - Clear code structure
   - Consistent formatting
   - Comprehensive documentation
   - Version-controlled configuration

## Usage

### Yandex Cloud Deployment

1. Initialize Terraform:
```bash
cd terraform/yandex
terraform init
```

2. Apply the configuration:
```bash
terraform apply
```

### GitHub Repository Management

1. Set GitHub token:
```bash
export GITHUB_TOKEN=your_token_here
```

2. Initialize Terraform:
```bash
cd terraform/github
terraform init
```

3. Import existing repository:
```bash
terraform import github_repository.core-course-labs S25-core-course-labs
```

4. Apply configuration:
```bash
terraform apply
```

## State Commands Output

### Terraform State List
```
$ terraform state list
github_branch_default.master
github_branch_protection.master
github_repository.core-course-labs
```

### Terraform Output
```
$ terraform output
repository_default_branch = "master"
repository_git_clone_url = "git://github.com/AlexStrNik/S25-core-course-labs.git"
repository_url = "https://github.com/AlexStrNik/S25-core-course-labs"
```

## Task 1: Introduction to Terraform

### Docker Infrastructure

1. Terraform State List Output:
```
docker_container.nginx
docker_image.nginx
```

2. Terraform Apply Output:
```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
container_id = "bced15514414daf75e4dfb6fefd1ee8030499c143ca1b65125894022845ce4d1"
image_id = "sha256:0dff3f9967e3cb3482965cc57c30e171f1def88e574757def5474cd791f50a16nginx:latest"
```

3. Container Configuration:
- Using nginx:latest image
- Port mapping: internal port 80 to external port 8000
- Container name: "tutorial" (configurable via variable)

### Yandex Cloud Infrastructure Setup

1. First, install Yandex Cloud CLI:
```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```

2. Initialize Yandex Cloud CLI:
```bash
yc init
```

3. Create a service account:
```bash
yc iam service-account create --name terraform
```

4. Get your folder ID:
```bash
yc config get folder-id
```

5. Create an authorized key:
```bash
yc iam key create --service-account-name terraform --output key.json
```

6. Get an OAuth token from Yandex Cloud:
   - Visit https://oauth.yandex.com/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb

7. Set up environment variables:
```bash
export YC_TOKEN="<your_oauth_token>"
export YC_CLOUD_ID="<your_cloud_id>"
export YC_FOLDER_ID="<your_folder_id>"
```

8. Generate SSH key if you don't have one:
```bash
ssh-keygen -t rsa -b 2048
```

9. Get the image ID for your VM:
```bash
yc compute image list --folder-id standard-images
```

10. Initialize and apply Terraform:
```bash
cd terraform/yandex
terraform init
terraform plan
terraform apply
```

### Infrastructure Details

The Terraform configuration creates:
- A Virtual Private Cloud (VPC) network
- A subnet in the ru-central1-a zone
- A compute instance with:
  - 2 CPU cores
  - 2 GB RAM
  - Public IP address
  - Ubuntu image
  - SSH key access

### Best Practices

1. **Security**:
   - Never commit sensitive credentials to version control
   - Use environment variables for sensitive data
   - Rotate access tokens regularly

2. **State Management**:
   - Keep terraform state files secure
   - Consider using remote state storage
   - Use state locking when working in a team

3. **Code Organization**:
   - Separate configurations into different directories
   - Use variables for reusable values
   - Document your configurations

4. **Resource Naming**:
   - Use consistent naming conventions
   - Add proper tags and labels
   - Include purpose in resource names

## Task 2: GitHub Infrastructure

In this task, we set up and manage GitHub repository infrastructure using Terraform. The implementation follows Infrastructure as Code (IaC) principles to maintain consistent and version-controlled repository configuration.

### Implementation Details

1. **Provider Configuration (`versions.tf`)**
   ```hcl
   terraform {
     required_providers {
       github = {
         source  = "hashicorp/github"
         version = "~> 5.0"
       }
     }
     required_version = ">= 1.0.0"
   }
   ```

2. **Variables (`variables.tf`)**
   - Defined essential variables for repository configuration
   - Used variable types and descriptions for better documentation
   - Implemented sensitive handling for GitHub token
   ```hcl
   variable "github_token" {
     description = "GitHub Personal Access Token"
     type        = string
     sensitive   = true
   }
   ```

3. **Main Configuration (`main.tf`)**
   - Repository settings:
     - Name and description
     - Visibility (public)
     - Features (issues, wiki, projects)
   - Branch protection rules:
     - Protected master branch
     - Required pull request reviews
     - Status checks requirement
   ```hcl
   resource "github_repository" "core-course-labs" {
     name        = var.repository_name
     description = var.repository_description
     visibility  = var.repository_visibility
     has_issues  = true
     # ...
   }
   ```

4. **Outputs (`outputs.tf`)**
   - Repository URL
   - Git clone URL
   - Default branch name
   ```hcl
   output "repository_url" {
     description = "URL of the created repository"
     value       = github_repository.core-course-labs.html_url
   }
   ```

### Security Measures

1. **Authentication**
   - Used Personal Access Token with minimal required permissions
   - Token stored as sensitive variable
   - Token passed via environment variable

2. **Branch Protection**
   - Protected master branch from direct pushes
   - Required pull request reviews
   - Required status checks
   - Enforced code owner reviews

3. **Repository Settings**
   - Configured secure defaults
   - Enabled branch deletion on merge
   - Required linear history

### Workflow

1. **Initial Setup**
   ```bash
   # Set GitHub token
   export GITHUB_TOKEN=<your_token>

   # Initialize Terraform
   cd terraform/github
   terraform init
   ```

2. **Repository Import**
   ```bash
   # Import existing repository
   terraform import github_repository.core-course-labs S25-core-course-labs
   ```

3. **Apply Configuration**
   ```bash
   # Apply changes
   terraform apply
   ```

### Results

The implementation successfully:
1. Configured repository settings through code
2. Implemented branch protection rules
3. Set up required review processes
4. Enabled repository features (issues, wiki, projects)
5. Documented configuration in version control

### Best Practices Applied

1. **Code Organization**
   - Separated configuration into logical files
   - Used clear resource naming
   - Implemented consistent formatting

2. **Security**
   - Protected sensitive values
   - Implemented least privilege principle
   - Set up comprehensive branch protection

3. **Documentation**
   - Added inline comments
   - Created comprehensive README
   - Documented variables and outputs

4. **Version Control**
   - Committed Terraform files
   - Included lock files
   - Added documentation

### Verification

You can verify the configuration by:
1. Checking repository settings on GitHub
2. Attempting to push directly to master (should be blocked)
3. Creating a pull request (should require review)
4. Viewing the repository features (issues, wiki, etc.)

The infrastructure is now managed through code, ensuring consistent configuration and enabling version control of infrastructure changes.
