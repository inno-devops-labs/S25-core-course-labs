# Ansible

## Inventory

In inventory, we have single host (Kali VM), authorization is by SSH private key. To properly use it, you need first to run `ssh-copy-id` or manually add your public key to `authorized_keys`

Details:

```json
{
    "_meta": {
        "hostvars": {
            "dev-vm": {
                "ansible_host": "172.16.41.130",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "kali"
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
            "dev-vm"
        ]
    }
}
```

```bash
@all:
  |--@ungrouped:
  |  |--dev-vm
```

## Deployment output

For diff (install Docker and Docker compose on kali):

```bash
➜  ansible git:(lab5) ✗ ansible-playbook -i ./inventory/default.yml playbooks/dev/main.yml --diff -K
BECOME password:

PLAY [all] ************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host dev-vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [dev-vm]

TASK [docker : Install packages] **************************************************************************************************************************************
ok: [dev-vm]

TASK [docker : Add Docker GPG key] ************************************************************************************************************************************
ok: [dev-vm]

TASK [docker : Add Docker repository] *********************************************************************************************************************************
ok: [dev-vm]

TASK [docker : Install Docker] ****************************************************************************************************************************************
included: /home/ucat/Study/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for dev-vm

TASK [docker : Install Docker packages] *******************************************************************************************************************************
ok: [dev-vm]

TASK [docker : Ensure Docker service is started and enabled] **********************************************************************************************************
ok: [dev-vm]

TASK [docker : Add users to Docker group] *****************************************************************************************************************************
ok: [dev-vm] => (item=kali)

TASK [docker : Install Docker Compose] ********************************************************************************************************************************
included: /home/ucat/Study/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for dev-vm

TASK [docker : Ensure Docker Compose is installed] ********************************************************************************************************************
ok: [dev-vm]

PLAY RECAP ************************************************************************************************************************************************************
dev-vm                     : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
