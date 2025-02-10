# Ansible

I used *Yandex Cloud Compute VM* that I created with `Terraform` as targets to run my playbooks.

## Best practices

- Properly structured Ansible project
- Use Dynamic Inventory for Cloud Environments
- Write Idempotent Playbooks
- Use Handlers for Service Restarts
- Write Reusable Roles
- Use `fact_caching`
- Test Playbooks Before Running on Production
  - Use `ansible-lint` to check for best practices.
  - Use `--check` mode to preview changes (`ansible-playbook main.yml --check`)
- Use `loop` instead of duplicating tasks

## Execute playbook to deploy the Docker role

```bash
ebob@laptop ansible % ansible-playbook playbooks/dev/main.yml -i inventory/yacloud_compute.yml --diff --check

PLAY [Install and configure Docker] **********************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [vm-1]

TASK [docker : Install Docker] ***************************************************************************************
included: /Users/ebob/Code/devops-labs/ansible/roles/docker/tasks/install_docker.yml for vm-1

TASK [docker : Update apt package index] *****************************************************************************
changed: [vm-1]

TASK [docker : Install required system packages] *********************************************************************
ok: [vm-1] => (item=apt-transport-https)
ok: [vm-1] => (item=ca-certificates)
ok: [vm-1] => (item=curl)
ok: [vm-1] => (item=gnupg-agent)
ok: [vm-1] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ************************************************************************
ok: [vm-1]

TASK [docker : Add Docker's official apt repository] *****************************************************************
ok: [vm-1]

TASK [docker : Install Docker and dependencies] **********************************************************************
ok: [vm-1]

TASK [docker : Add user to docker group] *****************************************************************************
ok: [vm-1]

TASK [docker : Enable Docker service to start on boot] ***************************************************************
ok: [vm-1]

TASK [docker : Install Docker Compose] *******************************************************************************
included: /Users/ebob/Code/devops-labs/ansible/roles/docker/tasks/install_docker_compose.yml for vm-1

TASK [docker : Install Docker Compose] *******************************************************************************
ok: [vm-1]

PLAY RECAP ***********************************************************************************************************
vm-1                       : ok=11   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739210586.456952 1547116 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

## Inventory Details

### `ansible-inventory -i <name_of_your_inventory_file>.yaml --list`

```bash
venvebob@laptop ansible % ansible-inventory -i inventory/yacloud_compute.yml --list | tail -n 50

                },
                "ansible_user_gecos": {
                    "__ansible_unsafe": "Ubuntu"
                },
                "ansible_user_gid": 1000,
                "ansible_user_id": {
                    "__ansible_unsafe": "ubuntu"
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 1000,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_virtualization_tech_guest": [],
                "ansible_virtualization_tech_host": [],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "NA"
                },
                "discovered_interpreter_python": {
                    "__ansible_unsafe": "/usr/bin/python3.12"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "vm-1"
        ]
    }
}
```

### `ansible-inventory -i <name_of_your_inventory_file>.yaml --graph`

```bash
ebob@laptop ansible % ansible-inventory -i inventory/yacloud_compute.yml --graph
@all:
  |--@ungrouped:
  |--@yacloud:
  |  |--vm-1
```
