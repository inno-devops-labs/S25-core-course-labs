# Ansible Documentation

## Deployment Output

Last 50 lines of ansible-playbook execution:
```bash
PLAY [Deploy Docker on Cloud VM] ***************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [master_vm]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/d/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for master_vm

TASK [docker : Update apt package index] *******************************************************************************
changed: [master_vm]

TASK [docker : Install prerequisites for Docker] ***********************************************************************
changed: [master_vm]

TASK [docker : Add Docker’s official GPG key] **************************************************************************
changed: [master_vm]

TASK [docker : Add Docker repository] **********************************************************************************
changed: [master_vm]

TASK [docker : Install Docker CE] **************************************************************************************
changed: [master_vm]

TASK [docker : Ensure Docker service is started and enabled] ***********************************************************
ok: [master_vm]

TASK [docker : Add current user to docker group] ***********************************************************************
changed: [master_vm]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/d/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for master_vm

TASK [docker : Download Docker Compose] ********************************************************************************
changed: [master_vm]

TASK [docker : Verify Docker Compose installation] *********************************************************************
ok: [master_vm]

PLAY RECAP *************************************************************************************************************
master_vm                  : ok=12   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Dry Run Output

Command used to perform a dry run:

```bash
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --check --diff
PLAY [Deploy Docker on Cloud VM] ***************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [master_vm]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/d/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for master_vm

TASK [docker : Update apt package index] *******************************************************************************
changed: [master_vm]

TASK [docker : Install prerequisites for Docker] ***********************************************************************
ok: [master_vm]

TASK [docker : Add Docker’s official GPG key] **************************************************************************
ok: [master_vm]

TASK [docker : Add Docker repository] **********************************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **************************************************************************************
ok: [master_vm]

TASK [docker : Ensure Docker service is started and enabled] ***********************************************************
ok: [master_vm]

TASK [docker : Add current user to docker group] ***********************************************************************
ok: [master_vm]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/d/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for master_vm

TASK [docker : Download Docker Compose] ********************************************************************************
ok: [master_vm]

TASK [docker : Verify Docker Compose installation] *********************************************************************
skipping: [master_vm]

PLAY RECAP *************************************************************************************************************
master_vm                  : ok=11   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Inventory Details


```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

```bash
{
    "_meta": {
        "hostvars": {
            "master_vm": {
                "ansible_host": "89.169.155.153",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/home/dm/.ssh/id_rsa",
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

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

```bash
@all:
  |--@ungrouped:
  |  |--master_vm
```
