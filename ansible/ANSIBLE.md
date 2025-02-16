# Ansible-related work
- organized repository for ansible
- used an existing Ansible role for Docker, created a playbook and tested:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```
- developed a custom Ansible role for Docker:
    - install Docker and Docker Compose: install_docker.yml and install_compose.yml
    - updated ansible/playbooks/dev/main.yaml
    - added task to configure Docker to start on boot
    - included task o add the current user to the docker group to avoid using sudo for Docker commands

## Output of
```bash 
ANSIBLE_ROLES_PATH=ansible/roles ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --check --diff | tail -n 50 > ansible/ANSIBLE.md
```

PLAY [Deploy Docker with Custom Role] ******************************************

TASK [Gathering Facts] *********************************************************
ok: [cloud_vm]

TASK [docker : Install Docker] *************************************************
included: /home/sg/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for cloud_vm

TASK [docker : Install Docker dependencies] ************************************
ok: [cloud_vm]

TASK [docker : Add Docker GPG key] *********************************************
ok: [cloud_vm]

TASK [docker : Add Docker repository] ******************************************
ok: [cloud_vm]

TASK [docker : Install Docker] *************************************************
ok: [cloud_vm]

TASK [docker : Install Docker Compose] *****************************************
included: /home/sg/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for cloud_vm

TASK [docker : Download Docker Compose] ****************************************
ok: [cloud_vm]

TASK [docker : Enable and Start Docker Service] ********************************
ok: [cloud_vm]

TASK [docker : Add user to Docker group] ***************************************
ok: [cloud_vm]

TASK [docker : Configure Docker daemon (User Namespace Remap)] *****************
ok: [cloud_vm]

TASK [docker : Restart Docker] *************************************************
changed: [cloud_vm]

PLAY RECAP *********************************************************************
cloud_vm                   : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

## Output of
```bash
ANSIBLE_ROLES_PATH=ansible/roles ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```
{
    "_meta": {
        "hostvars": {
            "cloud_vm": {
                "ansible_host": "158.160.152.199",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/home/sg/.ssh/id_ed25519",
                "ansible_user": "vm-user"
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
            "cloud_vm"
        ]
    }
}

## Output of
```bash
ANSIBLE_ROLES_PATH=ansible/roles ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
```
@all:
  |--@ungrouped:
  |  |--cloud_vm