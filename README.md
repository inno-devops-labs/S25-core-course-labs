# Docker Installation with Ansible

This repository contains an Ansible playbook for installing Docker on a remote machine and deploying a web application in a Docker container.


## Prerequisites
- Ansible 2.x or higher
- A remote server or localhost with SSH access
- Docker must not be already installed on the target machine for this playbook to work
- The `community.docker` Ansible collection is required for Docker management

### Install Ansible Collection
To ensure the proper functionality of the playbook, you need to install the `community.docker` collection:

```bash
ansible-galaxy collection install community.docker
```

### Install Docker
Run the following command to install Docker on the remote machine:

``` bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --ask-become-pass
```

This playbook will:

Install Docker on the remote machine

Pull the Docker image for the web application

Run the Docker container for the web app

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

## Role Documentation
For more details about the Docker role used in this repository, refer to `ansible/roles/docker/README.md` .
