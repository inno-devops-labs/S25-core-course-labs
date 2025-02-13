# Ansible Docker Deployment

## Deployment output

```bash
PLAY [Install Docker] ********************************************************************

TASK [Gathering Facts] *******************************************************************
ok: [my_yandex_vm]

TASK [docker : Install required packages] ************************************************
ok: [my_yandex_vm]

TASK [docker : Create directory for APT keyrings (if missing)] ***************************
ok: [my_yandex_vm]

TASK [docker : Download and save Docker GPG key] *****************************************
ok: [my_yandex_vm]

TASK [docker : Add Docker repository] ****************************************************
ok: [my_yandex_vm]

TASK [docker : Update APT cache and install Docker] **************************************
ok: [my_yandex_vm]

PLAY RECAP *******************************************************************************
my_yandex_vm               : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Inventory list output

```bash
{
    "_meta": {
        "hostvars": {
            "my_yandex_vm": {
                "ansible_host": "89.169.156.215",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/my-yandex-key.pub",
                "ansible_user": "nika"
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
            "my_yandex_vm"
        ]
    }
}
```

## Inventory graph output

```bash
@all:
  |--@ungrouped:
  |  |--my_yandex_vm
```

