# Ansible

## Overview
Ansible playbooks and roles for deploying Docker and applications to Yandex Cloud :?

## Structure
```
ansible/
├── inventory/
│ └── default_aws_ec2.yml # Inventory file for cloud instance
├── playbooks/
│ └── dev/
│ └── main.yaml # Main playbook for Docker deployment
├── roles/
│ ├── docker/ # Custom Docker role
│ └── web_app/ # Role for web application deployment
└── ansible.cfg # Ansible configuration
```

## Roles

### Docker Role
The Docker role installs and configures Docker and Docker Compose on target machines. For detailed information about the Docker role, see [ansible/roles/docker/README.md](roles/docker/README.md).

## Inventory Information

### Current Inventory Structure
```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
"_meta": {
"hostvars": {
"yandex_vm": {
"ansible_host": "51.250.89.227",
"ansible_ssh_private_key_file": "~/.ssh/id_rsa",
"ansible_user": "yc-user"
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
"yandex_vm"
 ]
 }
}
```

### Inventory Graph
```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
 |--@ungrouped:
 | |--yandex_vm
```

## Deployment Output
Last deployment output (last 50 lines):
```
PLAY [all] ********************************************************************
TASK [Gathering Facts] ********************************************************
ok: [yandex_vm]
TASK [docker : Install required system packages] ******************************
ok: [yandex_vm]
TASK [docker : Install Docker with official script] ***************************
ok: [yandex_vm]
TASK [docker : Configure Docker to start on boot] *****************************
ok: [yandex_vm]
TASK [docker : Create docker group] ******************************************
changed: [yandex_vm]
TASK [docker : Add user to docker group] ************************************
changed: [yandex_vm]
TASK [docker : Install Docker Compose] **************************************
changed: [yandex_vm]
PLAY RECAP ******************************************************************
yandex_vm : ok=9 changed=3 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

### Web App Deployment Output
Latest web app deployment output:
```
PLAY [all] ***************************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************
ok: [yandex_vm]
TASK [web_app : Template Docker Compose file] ****************************************************************************************
changed: [yandex_vm]
TASK [web_app : Start application with Docker Compose] *******************************************************************************
changed: [yandex_vm]
PLAY RECAP ***************************************************************************************************************************
yandex_vm                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### The web application is now successfully deployed and accessible at http://51.250.89.227:8000