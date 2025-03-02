# Ansible Infrastructure Documentation

## Overview
This Ansible configuration manages the deployment of a Python web application using Docker on Ubuntu servers.

## Directory Structure
```
ansible/
├── ansible.cfg
├── inventory/
│   └── default.yml
├── playbooks/
│   └── dev/
│       └── main.yaml
└── roles/
    ├── docker/
    │   ├── defaults/
    │   ├── handlers/
    │   └── tasks/
    └── web_app/
        ├── defaults/
        ├── handlers/
        ├── meta/
        └── tasks/
```

## Inventory Information

### Inventory List Output
```bash
$ ansible-inventory -i inventory/default.yml --list
{
    "all": {
        "hosts": {
            "vm": {
                "ansible_host": "YOUR_IP",
                "ansible_user": "ubuntu",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa"
            }
        }
    }
}
```

### Inventory Graph
```bash
$ ansible-inventory -i inventory/default.yml --graph
@all:
  |--@ungrouped:
  |  |--vm
```

## Roles

### Docker Role
Installs and configures Docker and Docker Compose:
- Installs required packages
- Configures Docker repository
- Sets up Docker service
- Adds users to Docker group
- Installs Docker Compose

### Web App Role
Deploys the Python web application:
- Pulls application Docker image
- Creates and starts container
- Configures port mapping
- Sets timezone
- Implements restart policy

## Deployment Output
```bash
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [all] ********************************************************************

TASK [Gathering Facts] ********************************************************
ok: [vm]

TASK [docker : Install required system packages] *******************************
ok: [vm]

TASK [docker : Add Docker GPG key] *******************************************
ok: [vm]

TASK [docker : Add Docker repository] ****************************************
ok: [vm]

TASK [docker : Install Docker packages] **************************************
ok: [vm]

TASK [docker : Ensure Docker service is started and enabled] *****************
ok: [vm]

TASK [docker : Add users to Docker group] ***********************************
ok: [vm]

TASK [web_app : Pull Docker image] ******************************************
ok: [vm]

TASK [web_app : Create and start container] *********************************
changed: [vm]

PLAY RECAP ******************************************************************
vm : ok=9 changed=1 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

## Usage

### Deploy Infrastructure
```bash
ansible-playbook playbooks/dev/main.yaml --diff
```

### Verify Deployment
```bash
ansible vm -m shell -a "docker ps"
```

### Check Application
Access the application at: http://YOUR_VM_IP:5000

## Best Practices Implemented

1. **Role-based Organization**
   - Separate roles for Docker and application
   - Clear dependency management
   - Modular and reusable code

2. **Security**
   - No hardcoded credentials
   - Proper user management
   - Secure Docker configuration

3. **Configuration Management**
   - Variables in defaults
   - Environment-specific playbooks
   - Handlers for service management

4. **Documentation**
   - Clear role documentation
   - Deployment instructions
   - Inventory information 