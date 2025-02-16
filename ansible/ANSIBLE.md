# Task 1

After configuring ansible roles/inventory/playbook I runned it on my yandex cloud VM with the following result (all commands running inside `ansible` folder): 

```bash
[nvy@nvy ansible]$ ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main.yaml

PLAY [Install and configure Docker] ********************************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [docker : Remove existing Docker repositories] ****************************************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install prerequisites] ******************************************************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Create directory for Docker GPG key] ****************************************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker GPG key] *********************************************************************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Add Docker repo] ************************************************************************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Install Docker] *************************************************************************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Verify Docker Compose installation] *****************************************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Check Docker service] *******************************************************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add current user to the docker group] ***************************************************************************************************************************************************************
changed: [yandex_vm]

PLAY RECAP *********************************************************************************************************************************************************************************************************
yandex_vm                  : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=
```

And after that docker installed in the yandex cloud vm:

```bash
[hacker@nvy ~]$ ssh admin@158.160.144.225
Last login: Sun Feb 16 18:21:36 2025 from 188.130.155.155
admin@compute-vm-2-2-20-ssd-1739717002688:~$ docker --version
Docker version 27.5.1, build 9f9e405
```

Output of configs:

```bash
nvy@nvy ansible]$ ansible-inventory -i inventory/default_yandex.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_vm

[nvy@nvy ansible]$ ansible-inventory -i inventory/default_yandex.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_vm": {
                "ansible_host": "158.160.144.225",
                "ansible_ssh_private_key_file": "ssh_key",
                "ansible_user": "admin"
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

# Best Practices

- variables: configs organization;
- non-root access: for security;
- handler: to check that docker is running after restarts.
