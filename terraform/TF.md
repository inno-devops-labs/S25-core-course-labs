# 🚀 Terraform Lab Documentation

## 🛠️ Docker Infrastructure Using Terraform

### 1. `terraform state show` Output:
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

### 2. `terraform state list` Output:
docker_container.moscow_time

### 3. Applied Changes Log:
Changes to Outputs:
  ~ container_id   = "73e855edbe540f795f7ea54dc93a592ca153862326b0d82325062960f04086ab" -> (known after apply)
  ~ container_name = "moscow-time" -> "my-new-container-name"

### 4. Terraform Output:
container_id = "748c713b5e151bc89c429304020e6c17a43212d76363a377562b9113580547f6"
container_name = "moscow-time"

Steps:
Using info from tutorial:
1. Sign up for an account on Yandex Cloud.
2. Retrieve authentication credentials:
Retrieve authentication credentials:
Generate a service account.

3. Set up the CLI profile for operations using the service account:
    yc iam key create \
    --service-account-id <service_account_id> \
    --folder-name <repository_name_of_service_acount> \
    --output key.json 
   Locate service_account_id and repository_name_of_service_account within your account.
- If you encounter issues with yc, execute the following and retry the previous command:
    curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
4. Establish a CLI profile for executing operations under the service account. Define the profile name:
   yc config profile create <profile_name>
5. Configure the profile settings:
   yc config set service-account-key key.json
   yc config set cloud-id <cloud_id>
   yc config set folder-id <repository_id>
   Retrieve 'cloud_id' and repository_id from your account.
6. Store authentication credentials in environment variables:
   export YC_TOKEN=$(yc iam create-token)
   export YC_CLOUD_ID=$(yc config get cloud-id)
   export YC_FOLDER_ID=$(yc config get folder-id)
7. Create a directory yc_conf and a file main.tf within it.
8. My `main.tf` you can check in repository.
   The chosen region is ru-central1-d.
   To identify the boot disk image ID from Yandex Cloud Marketplace, execute:
   ```yc compute image list --folder-id standard-images```.
   Create `meta.txt` and generate an SSH key by running: To do it run this command 
  `ssh-keygen -t rsa -b 4096 -C "your_email"`.
9. Run the project and check results:
   terraform init
   terraform apply
   terraform validate
   terraform fmt

# Terraform for GitHub
This project leverages Terraform to automate GitHub repository infrastructure management, including configuration and branch protection enforcement.

1. **GitHub Provider Configuration:**
   Utilizing provider integrations/github version ~> 5.0.
   Implemented environment variables for secure storage of the GitHub token (TF_VAR_github_token).

2. **Repository Setup:**
   Defined github_repository.core-course-labs to manage an existing repository.
   Configured visibility (public), description, permissions, wiki, and project settings.

3. **Default Branch Configuration:**
   Designated the master branch as default using github_branch_default.
   
4. **Branch Protection Rules:**
   Established protection rules for the master branch.
   Configured settings:
    Preventing branch deletion (allows_deletions = false).
    Pull request requirements (minimum approval count, outdated review rejection).
    Enforcing policies for administrators (enforce_admins = true).

5. **Import existing resources:**
  Executed terraform import to integrate an existing repository and branch protection rules.

6. **Applying the changes:**
  Applied the following commands to implement the settings:
  terraform init
  terraform plan
  terraform apply