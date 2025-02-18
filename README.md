# Docker Installation with Ansible

This repository contains an Ansible playbook for installing Docker on a remote machine.

## Prerequisites
- Ansible 2.x or higher
- A remote server or localhost with SSH access

### Install Docker
Run the following command to install Docker on the remote machine:

``` bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --ask-become-pass
```

### Verify Installation
After the playbook runs, verify Docker is installed by running:

``` bash
docker --version
```

## Directory Structure
The repository follows the structure:

ansible/: Contains Ansible configuration, inventory, roles, and playbooks.

app_python/: Contains Python application code (if any).

terraform/: Contains Terraform configuration (if any).
