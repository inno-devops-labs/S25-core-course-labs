# Ansible-related work

First, Ansible with use of pip was installed.

Next, I've implemented the ansible directory structure and installed geerlingguy.docker role from Ansible Galaxy:

```ssh
ansible-galaxy install geerlingguy.docker
```

Docker role deploy report (last 50 lines):

```text
PLAY [Deploy Docker using the custom role] *****************************************************************************

TASK [Gathering Facts] *************************************************************************************************
[WARNING]: Platform linux on host yandex_terraform1 is using the discovered Python interpreter at /usr/bin/python3.10, but
future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_terraform1]

TASK [docker : Update apt cache] ***************************************************************************************
changed: [yandex_terraform1]

TASK [docker : Install prerequisites] **********************************************************************************
changed: [yandex_terraform1]

TASK [docker : Add Docker’s official GPG key] **************************************************************************
changed: [yandex_terraform1]

TASK [docker : Add Docker repository] **********************************************************************************
changed: [yandex_terraform1]

TASK [docker : Install Docker] *****************************************************************************************
changed: [yandex_terraform1]

TASK [docker : Download Docker Compose binary] *************************************************************************
changed: [yandex_terraform1]

TASK [docker : Verify Docker Compose installation] *********************************************************************
ok: [yandex_terraform1]

TASK [docker : Ensure Docker service is enabled and started] ***********************************************************
ok: [yandex_terraform1]

TASK [docker : Add current user to the docker group] *******************************************************************
changed: [yandex_terraform1]

PLAY RECAP *************************************************************************************************************
yandex_terraform1                   : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Output of ```ansible-inventory -i ansible/inventory/default_yandex.yml --list```:

```text
{
    "_meta": {
        "hostvars": {
            "yandex_terraform1": {
                "ansible_host": "89.169.168.47",
                "ansible_ssh_common_args": "-o StrictHostKeyChecking=no",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
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
            "yandex_terraform1"
        ]
    }
}
```

Output of ```ansible-inventory -i ansible/inventory/default_yandex.yml --graph``:

```text
@all:
  |--@ungrouped:
  |  |--yandex_terraform1
```