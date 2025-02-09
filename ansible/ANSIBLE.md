# Ansible

## Best Practices

1. Use `ansible-lint`:
    - Use `ansible.builtin` naming
    - Always give `name`
    - Always mention the `state`
2. Use `fact_caching` (see `ansible.cfg`)

## `ansible-playbook playbooks/dev/main.yml -i inventory --diff`

Please note that I have already executed my playbook,
so the output is concise due to the successful deployment.

```text
PLAY [Dev playbook] *************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] **************************************************************************
included: /home/mihdenis85/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Update apt package index] ****************************************************************
changed: [terraform-vm]

TASK [docker : Install required system packages] ********************************************************
ok: [terraform-vm] => (item=apt-transport-https)
ok: [terraform-vm] => (item=ca-certificates)
ok: [terraform-vm] => (item=curl)
ok: [terraform-vm] => (item=gnupg-agent)
ok: [terraform-vm] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***********************************************************
ok: [terraform-vm]

TASK [docker : Add Docker's official apt repository] ****************************************************
ok: [terraform-vm]

TASK [docker : Install Docker and dependencies] *********************************************************
ok: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] ******************************************************************
included: /home/mihdenis85/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ******************************************************************
ok: [terraform-vm]

PLAY RECAP **********************************************************************************************
terraform-vm               : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## `ansible-inventory -i inventory/yacloud_compute.yml --list | tail -n 50`

```text
                },
                "ansible_user_gecos": {
                    "__ansible_unsafe": "Ubuntu"
                },
                "ansible_user_gid": 1001,
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
                    "__ansible_unsafe": "/usr/bin/python3"
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
            "terraform-vm"
        ]
    }
}
```
