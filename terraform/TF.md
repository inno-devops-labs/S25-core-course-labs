# Docker Infrastructure Results

### Resource Descriptions

- **docker_image.nginx**: Nginx image used for the container.
- **docker_container.app**: Container running Nginx.

### Output of `terraform state list`

    ```bash
    docker_container.app
    docker_image.nginx
    
    
### Output of terraform output
**container_id** = "e7504b1116c9aebc9f683a95a4c432c3ce4de28e90f2f48273661f4e202467e9"
### Change Log
    ```bash
    + docker_image.nginx
    + docker_container.app


### Yandex Cloud Infrastructure

#### Provider Configuration
    ```bash
    provider "yandex" {
    token     = var.yc_token
    cloud_id  = var.yc_cloud_id
    folder_id = var.yc_folder_id
    zone      = "ru-central1-a"
    }

#### Resource Descriptions
* yandex_vpc_network.network: Network for the VM.
* yandex_vpc_subnet.subnet: Subnet in the ru-central1-a zone.
* yandex_compute_instance.vm: Virtual machine with specified parameters.

#### Output of terraform state list

    ```bash
    yandex_vpc_network.network
    yandex_vpc_subnet.subnet
    yandex_compute_instance.vm


#### Output of terraform output 
    ```bash
    vm_external_ip = "123.45.67.89"

#### Change Log

    ```bash
    + yandex_vpc_network.network
    + yandex_vpc_subnet.subnet
    + yandex_compute_instance.vm

### Variables
#### Description of Variables (from variables.tf):

    ```bash
    variable "yc_token" {
    description = "Yandex Cloud OAuth token"
    type        = string
    sensitive   = true
    }
    variable "yc_cloud_id" { ... }
    variable "yc_folder_id" { ... }


### Instructions for Applying
#### Install Terraform and Configure Providers:
    ```bash
    terraform init
#### Check the Plan:
    ```bash
    terraform plan -out=tfplan
#### Apply the Changes:
    ```bash
terraform apply tfplan


