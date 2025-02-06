## Terraform Apply Output

```
docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 3m34s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 6s [id=d08435af6207530e17af0bcef301a50658910d4369b6626dbd6d09a3d5914637]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

## Using Input Variables

To make our configuration more flexible, we'll use input variables for the container name. This allows us to reuse our configuration with different container names without modifying the main configuration file.

The container name is now defined in `variables.tf`:
```hcl
variable "container_name" {
  description = "The name of the container"
  type        = string
  default     = "tutorial"
}
```

## Terraform Outputs

After applying the configuration with variables and outputs, here are the results:

```
Outputs:

container_id = "506c8a65a5173d238a1732abb81040f4471a396d60a08d230b25236373d76ebe"
container_ip = "172.17.0.2"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
```

These outputs provide easy access to important information about our deployed resources:
- The container ID for reference and management
- The container's IP address for connectivity
- The image ID used by the container

## Terraform Best Practices for GitHub Repository Management

1. **Variable Management**
   - Use `variables.tf` to declare all input variables
   - Never hardcode sensitive values like tokens in configuration files
   - Mark sensitive variables with `sensitive = true`
   - Use `terraform.tfvars` for local development, but add it to `.gitignore`

2. **Repository Configuration**
   - Enable security features like secret scanning and push protection
   - Configure branch protection rules for main branches
   - Set appropriate merge strategies (squash, rebase, merge)
   - Enable vulnerability alerts and other security features

3. **State Management**
   - Keep `.terraform` and `terraform.tfstate*` in `.gitignore`
   - Consider using remote state storage for team collaboration
   - Regularly back up your state files

4. **Provider Configuration**
   - Pin provider versions to ensure consistency
   - Use environment variables for sensitive provider credentials
   - Keep provider configuration separate from resource definitions

5. **Resource Organization**
   - Use descriptive resource names that reflect their purpose
   - Group related resources together in the configuration
   - Use modules for reusable components

6. **Security Best Practices**
   - Use least privilege principle for GitHub tokens
   - Regularly rotate credentials and tokens
   - Enable two-factor authentication for GitHub accounts
   - Use secret scanning to prevent accidental credential exposure

7. **Documentation**
   - Maintain clear documentation of your Terraform configuration
   - Use comments in `.tf` files to explain complex configurations
   - Document variable descriptions and default values

8. **Version Control**
   - Use version control for all Terraform configurations
   - Implement CI/CD pipelines for Terraform deployments
   - Use pull requests for code reviews before applying changes

9. **Error Handling**
   - Use `terraform plan` to preview changes before applying
   - Implement proper error handling for API calls
   - Use `terraform import` for existing resources

10. **Maintenance**
    - Regularly update providers and modules
    - Clean up unused resources
    - Monitor and review Terraform configurations periodically

    ## Azure Cloud Infrastructure

1. **Azure CLI Authentication**
   ```bash
   az login
   ```
   - Successfully authenticated with Azure CLI
   - Selected subscription: "Main" (0ff37950-3e06-4453-aab7-a3633926c961)

2. **Azure Provider Configuration**
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

3. **Resource Group**
   - Created resource group "Devops_lab" in "eastus" region
   - Used as the base for all other resources

4. **Network Infrastructure**
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

5. **Virtual Machine**
   - Name: "devops-vps"
   - Size: Standard_B1s
   - Image: Ubuntu Server 18.04-LTS
   - Authentication: SSH Key
   - Admin Username: adminuser
   - OS Disk: Standard LRS

6. **Deployment Process**
   ```bash
   # Initialize Terraform
   terraform init
   
   # Plan the infrastructure
   terraform plan
   
   # Apply the configuration
   terraform apply
   ```

7. **Resources Created**
   - 1 Resource Group
   - 1 Virtual Network
   - 1 Subnet
   - 1 Public IP
   - 1 Network Interface
   - 1 Linux Virtual Machine

8. **Deployment Results**
   - All resources successfully created
   - Deployment completed in approximately 55 seconds
   - Network and VM configurations applied successfully

9. **Challenges and Solutions**
   - Initial resource group already existed: Resolved by creating new resources within the existing group
   - SSH key configuration: Successfully configured using inline public key
   - Network dependencies: Handled automatically by Terraform's dependency management

10. **Best Practices Applied**
    - Resource naming follows Azure conventions
    - Network segmentation with dedicated subnet
    - Secure VM access with SSH key authentication
    - Dynamic IP allocation for cost optimization
    - Basic SKU selection for development environment
