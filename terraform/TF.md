# Terraform  

## Part 1: Basics  

### init
- Installed Terraform from yandex mirror + tenv
- Created folder `terraform`   
- Made separate directories for different providers to keep things organized  

### Docker Part  

1. **Initialization**  
First, I start Terraform in docker folder:  
```bash  
cd terraform/docker  
terraform init  
```  

2. **Checking State**  
After apply, I check what resources exist:  
```bash  
$ terraform state list  
docker_container.python_app  
docker_image.python_app  
```  

When I run `terraform state show` for container, it display all settings. For example:  
- Command to run app: `["python", "app.py"]`  
- Environment variable `TZ=Europe/Moscow` (because I live in Russia)  
- Ports mapping: 5000 inside container to 5001 on host  

For image resource, output shows:  
- Image name: `mazzz3r/app_python:latest`  
- Keep_locally set to `false` (to save disk space)  

3. **Applying Changes**  
When I changed something, output after `terraform apply` was:  
```  
docker_container.python_app: Destroying... [id=81fd03...]  
...  
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.  
```  

4. **Using Variables**  
I learned to pass variables like container name:  
```bash  
terraform apply -var="container_name=custom_name"  
```  
Checked result with `docker ps` and saw new name:  
```  
NAMES        -> custom_name  
```  

### Yandex Cloud Part  

#### Setup Steps  
1. **Account and CLI**  
- Created Yandex.Cloud account (used university email)  
- Installed YC CLI using command:  
```bash  
curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash  
yc init  
```  

2. **Configuration**  
Got cloud ID and folder ID via CLI:  
```bash  
yc config get cloud-id  
yc config get folder-id  
```  
Set environment variables for Terraform:  
```bash  
export TF_VAR_token="yc-token"  # Not hardcoding!  
export TF_VAR_cloud_id="cloud-id"  
...  
```  

3. **Terraform Commands**  
Initialized and applied:  
```bash  
cd terraform/yandex  
terraform init && terraform apply  
```  

4. **State Output**  
VM details from `terraform state show`:  
- 2 CPU cores, 2GB RAM  
- Ubuntu 20.04 image  
- Public IP `89.169.132.86` (could access via SSH)  

#### Problems I Solved  
- **Authentication Issue**: At first, I put token directly in `.tf` file. My teacher said it’s unsafe. Fixed by using `TF_VAR` environment variables.  

## Part 2: Managing GitHub with Terraform  

### Repository Configuration  
1. **Setting Provider**  
Used personal GitHub token:  
```bash  
export TF_VAR_github_token="<my-secret-token>"  
```  

2. **Import Existing Repo**  
Imported my course labs repo:  
```bash  
terraform import github_repository.S25-core-course-labs S25-core-course-labs  
```  
Output said import successful.  

3. **Branch Protection**  
Added rules for `main` branch:  
- Require 1 approval before merge  
- Check status check "build"  
- No force pushes allowed  

State output shows:  
```  
required_pull_request_reviews {  
  required_approving_review_count = 1  
}  
```  

## How I Followed Best Practices  

### Security  
- **No Secrets in Code**: Used `TF_VAR` for tokens (teacher approved!)  
- **SSH Keys**: For Yandex VM access  
- **Branch Protection**: So nobody breaks main branch  

### Code Organization  
- Separate folders for each provider (Docker/Yandex/GitHub)  
- Clear names like `docker-container.tf`  
- Comments in English (but my English not perfect)  

### State Management  
- Backup `terraform.tfstate` manually (will learn remote state later)  
- Use `terraform state` commands to check resources  

## Common Commands I Used  

| Action | Command |  
|--------|---------|  
| Initialize | `terraform init` |  
| Plan Changes | `terraform plan -out=tfplan` |  
| Apply | `terraform apply tfplan` |  
| Destroy | `terraform destroy` (be careful!) |  

## What I Want to Improve Next  

1. **Remote State Storage**: Now using local files—not good for team projects.  
2. **Automate Backups**: Maybe use Yandex.Storage for state files.  
3. **Add Monitoring**: Like alerts if VM goes down.  
4. **Learn Modules**: To reuse code between projects.  

---

**Note from Student**:  
I’m still learning English and Terraform. Sometimes I make grammar mistakes or not understand advanced features, but I try my best. Big thanks to my professor for help!
