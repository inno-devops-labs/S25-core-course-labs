# Terraform  

## Part 1: Basics  

### init
- Installed Terraform from yandex mirror + tenv
- Created folder `terraform`   
- Made separate directories for different providers to keep things organized  

### Docker Part  

* init

```  
cd terraform/docker  
terraform init  
```  

* check state
```  
$ terraform state list  
docker_container.devopslabs  
docker_image.devopslabs  
```  


* apply
  
When I changed something, output after `terraform apply` was:  
```  
docker_container.devopslabs: Destroying... [id=81fd03...]  
...  
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.  
```  

* use variables 
I learned to pass variables like container name:  
```  
terraform apply -var="container_name=custom_name"  
```  
Checked result with `docker ps` and saw new name:  
```  
NAMES        -> custom_name  
```  

### Yandex Cloud Part  

#### setup
* account
- Created Yandex.Cloud account (used personal email, I work at yandex and have benefits by this)  
- Installed YC CLI using command from documentation 
```  
curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash  
yc init  
```  

* config 
Got cloud ID and folder ID via CLI:  
```  
yc config get cloud-id  
yc config get folder-id  
```  
Set environment variables for Terraform:  
```  
export TF_VAR_token="yc-token"  # Not hardcoding!  
export TF_VAR_cloud_id="cloud-id"  
...  
```  

* run terraform 
Initialized and applied:  
```bash  
cd terraform/yandex  
terraform init && terraform apply  
```  

* outputs 
VM details from `terraform state show`:  
- 2 CPU cores, 2GB RAM  
- Ubuntu 20.04 image  
- Public IP for connection via ssh


### Repository Configuration  

* setup provider 
Used GitHub token:  
```  
export TF_VAR_github_token=""  
```  

* import repo
Imported my course labs repo:  
```  
terraform import github_repository.S25-core-course-labs S25-core-course-labs  
```  

## Best Practicies 

### Security  
- **No Secrets in Code**: Used `TF_VAR` 
- **SSH Keys**: For Yandex VM access  

### Code Organization  
- Separate folders for each provider (Docker/Yandex/GitHub)
- Clear names like
- ignoring cache files in repository


## Commands

| Action | Command |  
|--------|---------|  
| Initialize | `terraform init` |  
| Plan Changes | `terraform plan -out=tfplan` |  
| Apply | `terraform apply tfplan` |  
| Destroy | `terraform destroy` (be careful!) |  

## Improvements 

* Automatic backups
* Security montoring (XDR)
* Resource monitoring
* Alerts

