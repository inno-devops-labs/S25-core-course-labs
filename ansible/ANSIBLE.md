# Ansible

## Exisiting Ansible role

- Installing the existing Ansible docker role:

```bash
ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- changing role geerlingguy.docker from 7.4.5 to unspecified
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /home/mikha/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

## Custom Ansible role

- Allowing Ansible to locate the config file

```bash
export ANSIBLE_CONFIG=/mnt/c/devops/kubespray/ansible.cfg
```

- Running the playbook

```bash
ansible-playbook playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] ***********************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] **************************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ***************************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **************************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ********************************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ********************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] *******************************************************************************
ok: [master_vm]

PLAY RECAP *************************************************************************************************************
master_vm                  : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

- Listing the inventory

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "master_vm": {
                "ansible_host": "51.250.83.111",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ubuntu"
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
            "master_vm"
        ]
    }
}
```

- Validating the inventory

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--master_vm
```

## Lab 7: Application deployment

```bash
ansible-playbook playbooks/dev/main.yaml 

PLAY [Install and Configure Docker] ************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] ***********************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] **************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ***************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **************************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ********************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] *******************************************************************************************************************************************
ok: [master_vm]

TASK [web_app : Create application directory] **************************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Deploy Docker Compose template] ************************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Ensure Docker image is pulled] *************************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Run Python application container] **********************************************************************************************************************************
changed: [master_vm]

PLAY RECAP *************************************************************************************************************************************************************************
master_vm                  : ok=12   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```
