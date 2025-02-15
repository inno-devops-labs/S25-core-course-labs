# Ansible Documentation

## Project Structure
```
ansible/
├── inventory/
│   └── default_aws_ec2.yml
├── roles/
│   └── docker/
├── playbooks/
│   └── dev/
│       └── main.yaml
└── ansible.cfg
```

## Inventory

### Inventory Structure
```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--localhost
```

### Detailed Inventory Output
```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}
```

## Deployment Output

```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

PLAY [Install Docker] *******************************************************************

TASK [Gathering Facts] ****************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Install Docker packages] ***********************************
ok: [localhost]

TASK [geerlingguy.docker : Install docker-compose-plugin] *****************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot] **************
ok: [localhost]

PLAY RECAP **************************************************************************
localhost                  : ok=18   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

## Installation Verification

### Component Versions
```bash
$ docker --version
Docker version 27.5.1, build 9f9e405

$ docker-compose --version
Docker Compose version v2.32.1
```

### Service Status
```bash
$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running)
```

### Docker Group Check
```bash
$ groups | grep docker
m7 ... docker ...
```

## Basic Commands

### Running Playbook
```bash
# Standard execution
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml

# Execute with sudo privileges
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

# Syntax check
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --syntax-check

# Dry run
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --check -K

# Run with diff output
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --diff -K
```