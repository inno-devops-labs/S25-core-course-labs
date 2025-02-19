# Ansible Documentation

## Overview

This repository now includes Ansible playbooks and roles for a complete Continuous Deployment (CD) process for our applications. In addition to the Docker installation and configuration provided in Lab 5, this lab (Lab 6) introduces a new **web_app** role that deploys our application's Docker image using Docker Compose. The enhancements include:

- **Application Deployment:**  
  - A custom **web_app** role that deploys the application's Docker image.
  - A Docker Compose template to define the container configuration.
  - A wipe logic to remove existing containers/configuration (controlled via a variable).

- **Best Practices:**  
  - Grouping tasks with blocks for better organization.
  - Applying role dependencies (the **web_app** role depends on the **docker** role).
  - Using tags for selective execution (e.g., `docker`, `deploy`, `wipe`).
  
- **Bonus CD Improvement:**  
  - An extra playbook for deploying a NodeJS application (located in `app_nodejs`), reusing the **web_app** role with overridden variables.

## Role and Playbook Structure

- **Playbooks:**  
  - **Main Playbook:** `ansible/playbooks/dev/main.yaml`  
    (Deploys both the Docker and the web_app roles.)
  - **Bonus NodeJS Playbook:** `ansible/playbooks/dev/app_nodejs/main.yaml`  
    (Overrides the image and port for the NodeJS application.)

- **Roles:**  
  - **Docker Role:** Located in `ansible/roles/docker/`  
    - Default variables: `ansible/roles/docker/defaults/main.yml`
    - Handlers: `ansible/roles/docker/handlers/main.yml`
    - Tasks:
      - `install_docker.yml`
      - `install_compose.yml`
      - `add_user_to_docker_group.yml`
      - Main task file: `ansible/roles/docker/tasks/main.yml`
  - **Web App Role:** Located in `ansible/roles/web_app/`  
    - Defaults: `ansible/roles/web_app/defaults/main.yml` (defines `docker_image`, `app_port`, and `web_app_full_wipe`)
    - Metadata: `ansible/roles/web_app/meta/main.yml` (declares dependency on the **docker** role)
    - Tasks:  
      - Wipe logic: `ansible/roles/web_app/tasks/0-wipe.yml`
      - Main deployment tasks: `ansible/roles/web_app/tasks/main.yml`  
        *This file uses blocks to group tasks (e.g., create directory, deploy docker-compose, pull image, and start the container) and applies appropriate tags.*
    - Templates:  
      - Docker Compose file template: `ansible/roles/web_app/templates/docker-compose.yml.j2`
    - Documentation: `ansible/roles/web_app/README.md`

## Testing the Playbooks

1. **Prerequisites:**  
   - Configure your VM (AWS EC2 or other) with proper credentials (Access Key ID, Secret, region, etc.).
   - Ensure the `ANSIBLE_CONFIG` environment variable is set if needed:
     ```bash
     export ANSIBLE_CONFIG=/full/path/to/your/ansible.cfg
     ```

2. **Dry Run (Check Mode):**  
   A dry run using the `--check` and `--diff` flags can be executed to preview changes:
   ```bash
   ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --check --diff
   ```

3. **Deployment Execution:**
    To deploy the complete environment (Docker and web_app), run:
    ```bash
    ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
    ```

3. **Selective Execution Using Tags:**
    To run only Docker-related tasks:
    ```bash
    ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --tags docker
    ```
    To run only the wipe tasks:
    ```bash
    ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --tags wipe
    ```


    ## Deployement Output: 
    Below are the last 50 lines from our deployment command (using a live run or --check --diff):

    ```
    TASK [docker : Ensure Docker service is running and enabled on boot] ********************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [docker : Download Docker Compose binary] *******************************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [docker : Create symbolic link for docker-compose] ************************************************
    ok: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [docker : Ensure the docker group exists] *********************************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [docker : Add current user to the docker group] ***************************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [docker : restart docker] *************************************************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [web_app : Create directory for the web application] **********************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [web_app : Deploy docker-compose file for the web application] **************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [web_app : Pull the Docker image for the application] ***********************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    TASK [web_app : Start the application container using Docker Compose] ************************************
    changed: [ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com]
    ```

## Inventory Details

Inventory output list:
```
{
    "Devops_Devops_Labs": {
        "hosts": [
            "ubuntu@ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com"
        ]
    },
    "_meta": {
        "hostvars": {
            "ubuntu@ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2025-02-18T14:16:29+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0e4142cf2330e9af6"
                        }
                    }
                ],
                "boot_mode": "uefi-preferred",
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "373ea385-d97b-4c53-9c41-91bb931cd168",
                "cpu_options": {
                    "core_count": 1,
                    "threads_per_core": 1
                },
                "current_instance_boot_mode": "legacy-bios",
                "ebs_optimized": false,
                "ena_support": true,
                "enclave_options": {
                    "enabled": false
                },
                "hibernation_options": {
                    "configured": false
                },
                "hypervisor": "xen",
                "image_id": "ami-01e2093820bf84df1",
                "instance_id": "i-0a7a85b8dbdee46cd",
                "instance_type": "t2.micro",
                "key_name": "Devops_Labs_1",
                "launch_time": "2025-02-18T14:16:28+00:00",
                "maintenance_options": {
                    "auto_recovery": "default"
                },
                "metadata_options": {
                    "http_endpoint": "enabled",
                    "http_protocol_ipv6": "disabled",
                    "http_put_response_hop_limit": 2,
                    "http_tokens": "required",
                    "instance_metadata_tags": "disabled",
                    "state": "applied"
                },
                "monitoring": {
                    "state": "disabled"
                },
                "network_interfaces": [
                    {
                        "association": {
                            "ip_owner_id": "amazon",
                            "public_dns_name": "ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com",
                            "public_ip": "3.107.79.201"
                        },
                        "attachment": {
                            "attach_time": "2025-02-18T14:16:28+00:00",
                            "attachment_id": "eni-attach-0879f23bfa08a9fe5",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-06b28a1abfd174e36",
                                "group_name": "launch-wizard-1"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:34:33:c1:4c:59",
                        "network_interface_id": "eni-0a32b9edf192abb1a",
                        "operator": {
                            "managed": false
                        },
                        "owner_id": "149536497278",
                        "private_dns_name": "ip-172-31-9-197.ap-southeast-2.compute.internal",
                        "private_ip_address": "172.31.9.197",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com",
                                    "public_ip": "3.107.79.201"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-9-197.ap-southeast-2.compute.internal",
                                "private_ip_address": "172.31.9.197"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0a0f7654a567cc7ed",
                        "vpc_id": "vpc-0890f62000b5787cd"
                    }
                ],
                "network_performance_options": {
                    "bandwidth_weighting": "default"
                },
                "operator": {
                    "managed": false
                },
                "owner_id": "149536497278",
                "placement": {
                    "availability_zone": "ap-southeast-2b",
                    "group_name": "",
                    "region": "ap-southeast-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-9-197.ap-southeast-2.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": true,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.9.197",
                "product_codes": [],
                "public_dns_name": "ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com",
                "public_ip_address": "3.107.79.201",
                "requester_id": "",
                "reservation_id": "r-007b8338c0f91fbf4",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-06b28a1abfd174e36",
                        "group_name": "launch-wizard-1"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0a0f7654a567cc7ed",
                "tags": {
                    "Name": "Devops_Labs",
                    "Role": "webapp"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2025-02-18T14:16:28+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0890f62000b5787cd"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2",
            "Devops_Devops_Labs"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ubuntu@ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com"
        ]
    }
}
```

Inventory output graph:
```
@all:
  |--@ungrouped:
  |--@aws_ec2:
  |  |--ubuntu@ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com
  |--@Devops_Devops_Labs:
  |  |--ubuntu@ec2-3-107-79-201.ap-southeast-2.compute.amazonaws.com
```
