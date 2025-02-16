# Ansible Deployment Documentation

## Overview
This document details the Ansible setup for deploying Docker on a cloud VM. We use a custom Docker role to install Docker, Docker Compose, enable Docker to start on boot, and add the user to the docker group.

## Playbook Execution
The playbook used is located at `ansible/playbooks/dev/main.yaml`. A dry-run was performed using:
```sh
ansible-playbook ansible/playbooks/dev/main.yaml --inventory ansible/inventory/default_aws_ec2.yml --diff --check
PLAY [Deploy Docker on VM] *********************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
[WARNING]: Platform linux on host local_vm is using the discovered Python interpreter at /usr/bin/python3.12, but
future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [local_vm]

TASK [docker : Include task to install Docker] *************************************************************************
included: /mnt/c/Users/aymou/Documents/iu-study/S25/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for local_vm

TASK [docker : Install Docker prerequisites] ***************************************************************************
changed: [local_vm] => (item=apt-transport-https)
ok: [local_vm] => (item=ca-certificates)
ok: [local_vm] => (item=curl)
ok: [local_vm] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] *************************************************************************************
changed: [local_vm]

TASK [docker : Add Docker repository] **********************************************************************************
changed: [local_vm]

TASK [docker : Install Docker] *****************************************************************************************
changed: [local_vm]

TASK [docker : Enable Docker service] **********************************************************************************
ok: [local_vm]

TASK [docker : Include task to install Docker Compose] *****************************************************************
included: /mnt/c/Users/aymou/Documents/iu-study/S25/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for local_vm

TASK [docker : Download Docker Compose] ********************************************************************************
changed: [local_vm]

TASK [docker : Verify Docker Compose installation] *********************************************************************
changed: [local_vm]

TASK [docker : Add current user to the docker group] *******************************************************************
changed: [local_vm]

TASK [docker : Ensure Docker starts on boot] ***************************************************************************
changed: [local_vm]

RUNNING HANDLER [docker : restart docker] ******************************************************************************
changed: [local_vm]

PLAY RECAP *************************************************************************************************************
local_vm                   : ok=13   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Information
Inventory list:
```sh
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "local_vm": {
                "ansible_connection": "local",
                "ansible_host": "127.0.0.1",
                "ansible_user": "sedoxxx"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "local_vm"
        ]
    }
}
```
Inventory graph:
```sh
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--local_vm
```
## Roles

### Docker Role Overview

1. **`default/main.yml`** - Contains configurations for installing and managing Docker and Docker Compose.
2. **`handlers/main.yml`** - Includes a handler for the service module to restart the Docker service when triggered.
3. **`tasks/install_compose.yml`** - Handles the installation of Docker Compose using the pip module.
4. **`tasks/install_docker.yml`** - Manages the installation of Docker on Debian-based systems using the `apt` module.
5. **`tasks/main.yml`** - Defines tasks to update the apt cache, install `Python 3` and `pip3`, and imports and executes tasks for installing Docker and Docker Compose.

For more details, refer to the [Docker Role README](roles/docker/README.md).

## Usage

### Prerequisites
1. Ansible 2.9+ installed
2. For local development:
   - Homebrew/WSL installed
   - ANSIBLE_SUDO_PASS environment variable set:
     ```bash
     export ANSIBLE_SUDO_PASS='your_sudo_password'
     ```
3. For Ubuntu deployment:
   - SSH key configured
   - Target host accessible


## Best Practices
- Organized repository structure with separate roles, playbooks, and inventory.
- Use of Ansible roles for modularity.
- Dry-run (`--check` and `--diff`) to verify changes before applying.
- Role defaults for Docker versions and configuration.
- Handlers to restart services when configuration changes.

## Secure Docker Configuration (BONUS TASK)

To enhance the security of our Docker deployment, we applied several measures through our custom Docker role:

- **Disabling Root Privileges:**  
  The configuration sets `"no-new-privileges": true` to prevent processes from gaining additional privileges. This helps in reducing the risk of privilege escalation from within containers.

- **User Namespace Remapping:**  
  We enable user namespace remapping by setting `"userns-remap": "default"` in the Docker daemon configuration. This isolates container user IDs from those on the host, reducing the impact if a container is compromised.

- **Configuration Deployment:**  
  The secure settings are defined in a `daemon.json` file, which is copied to `/etc/docker/daemon.json` using Ansible's `copy` module. Once applied, the Docker service is restarted to enforce the new configuration.


