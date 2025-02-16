# Ansible

## Docker 

### Deployment Output:
1. The **last 50 lines** of the output from deployment command:

**Command:**
```bash
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml | tail -n 50
```
**Output:**
```bash
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [vm]

TASK [docker : Update apt package index] ***************************************
changed: [vm]

TASK [docker : Install required packages] **************************************
ok: [vm]

TASK [docker : Add Docker GPG key] *********************************************
ok: [vm]

TASK [docker : Add Docker repository] ******************************************
ok: [vm]

TASK [docker : Install Docker] *************************************************
ok: [vm]

TASK [docker : Enable and start Docker service] ********************************
ok: [vm]

TASK [docker : Download Docker Compose] ****************************************
ok: [vm]

TASK [docker : Verify Docker Compose installation] *****************************
ok: [vm]

TASK [docker : Display installed Docker Compose version] ***********************
ok: [vm] => {
    "msg": "Docker Compose version v2.33.0"
}

TASK [docker : add current user to the docker group] ***************************
ok: [vm]

TASK [docker : secure Docker Configuration - Disable Root Access] **************
ok: [vm]

PLAY RECAP *********************************************************************
vm                         : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

2. Perform a **dry run** to see potential changes without applying them:

**Command:**
```bash
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --check --diff
```
**Output:**
```bash 
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Platform linux on host vm is using the discovered Python interpreter
at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [vm]

TASK [docker : Update apt package index] ***************************************
changed: [vm]

TASK [docker : Install required packages] **************************************
ok: [vm]

TASK [docker : Add Docker GPG key] *********************************************
ok: [vm]

TASK [docker : Add Docker repository] ******************************************
ok: [vm]

TASK [docker : Install Docker] *************************************************
ok: [vm]

TASK [docker : Enable and start Docker service] ********************************
ok: [vm]

TASK [docker : Download Docker Compose] ****************************************
ok: [vm]

TASK [docker : Verify Docker Compose installation] *****************************
skipping: [vm]

TASK [docker : Display installed Docker Compose version] ***********************
ok: [vm] => {
    "msg": ""
}

TASK [docker : add current user to the docker group] ***************************
ok: [vm]

TASK [docker : secure Docker Configuration - Disable Root Access] **************
ok: [vm]

PLAY RECAP *********************************************************************
vm                         : ok=11   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

### Inventory Details:

1. Inventory **list**

**Command:**
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```
**Output:**
```bash
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_host": "158.160.58.46",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "vm"
        ]
    }
}
```

2. Inventory **structure**

**Command:**
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```
**Output:**
```bash
@all:
  |--@ungrouped:
  |--@virtual_machines:
  |  |--vm
```
