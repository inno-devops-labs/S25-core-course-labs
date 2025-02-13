# Ansible Docker Deployment

## Deployment output

```bash
> ANSIBLE_ROLES_PATH=ansible/roles ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Install Docker on VM] *******************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm

TASK [docker : Update apt package index] ******************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Install required packages] *****************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker GPG key] ************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker repository] *********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install Docker] ****************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Enable and start Docker service] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm

TASK [docker : Install Docker Compose] ********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Verify Docker Compose installation] ********************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Display installed Docker Compose version] **************************************************************************************************************
ok: [yandex_vm] => {
    "msg": "Installed Docker Compose version: Docker Compose version v2.33.0"
}

PLAY RECAP ************************************************************************************************************************************************************
yandex_vm                  : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Inventory list

```bash
> ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_vm": {
                "ansible_host": "158.160.9.225",
                "ansible_ssh_private_key_file": "~/.ssh/my-yandex-key",
                "ansible_user": "renalaty"
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

## Inventory graph

```bash
> ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_vm
```
