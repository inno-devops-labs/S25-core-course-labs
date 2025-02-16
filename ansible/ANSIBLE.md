# Ansible Deployment Documentation

## Playbook Execution Output

Executed the following command:

```bash
ansible-playbook -i ./inventory/my_inventory.yml ./playbooks/deploy_docker.yml --check --diff
```

### Output

```bash
PLAY [Deploy Docker] ************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************
ok: [192.168.50.10]

TASK [docker : Install dependencies] *******************************************************************************
ok: [192.168.50.10]

TASK [docker : Add Docker GPG key] **********************************************************************************
changed: [192.168.50.10]

TASK [docker : Add Docker repository] *******************************************************************************
changed: [192.168.50.10]

TASK [docker : Install Docker] **************************************************************************************
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
The following packages will be upgraded:
  docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras
4 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
changed: [192.168.50.10]

TASK [docker : Install Docker Compose] ******************************************************************************
ok: [192.168.50.10]

TASK [docker : Enable Docker service on boot] ***********************************************************************
ok: [192.168.50.10]

TASK [docker : Add user to Docker group] ****************************************************************************
changed: [192.168.50.10]

PLAY RECAP **********************************************************************************************************
192.168.50.10            : ok=8    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details

Executed the following command:

```bash
ansible-inventory -i ./inventory/my_inventory.yml --list
```

### Inventory Output

```json
{
    "_meta": {
        "hostvars": {
            "192.168.50.10": {
                "ansible_host": "192.168.50.10",
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
            "192.168.50.10"
        ]
    }
}
```

## Inventory Graph Structure

Executed the following command:

```bash
ansible-inventory -i ./inventory/my_inventory.yml --graph
```

### Graph Output

```bash
@all:
  |--@ungrouped:
  |  |--192.168.50.10
```
