# Ansible Docker Installation

## Overview

This project uses Ansible to automate the installation of Docker and Docker Compose on an AWS EC2 instance.

## Prerequisites

- Ansible installed on your local machine
- An AWS EC2 instance
- SSH key configured for Ansible access

## Inventory Configuration

The inventory file `default_aws_ec2.yml` specifies the target host and required SSH variables.

```yaml
aws:
  hosts:
    54.208.142.142
  vars:
    ansible_ssh_private_key_file: ${ANSIBLE_KEY}
    ansible_user: ubuntu
```

`ANSIBLE_KEY` is a local variable holding the directory to the `.pem` file we generated so we can connect to the instance.

## Role: Docker Installation

The `docker` role is responsible for installing Docker and Docker Compose. It contains three tasks:

- `main.yml`
- `install_docker.yml`
- `install_compose.yml`

## Playbook

The playbook applies the `docker` role to the AWS instance.

```yaml
- hosts: aws # Targets all hosts under the aws group (from the inventory file).
  become: true # Runs tasks with sudo privileges.
  roles:
    - roles/docker # Calls the docker role from the roles/docker directory.
```

## Running the Playbook

1. Ensure Ansible is installed and configured.
2. Navigate to the project directory.
3. Run the playbook:

   ```bash
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
   ```

## Logs

```bash
TASK [docker : Ensure curl is present (on older systems without SNI).] *********
skipping: [54.208.142.142]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [54.208.142.142]

TASK [docker : Add Docker repository.] *****************************************
ok: [54.208.142.142]

TASK [docker : include_tasks] **************************************************
included: /home/moze/Documents/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 54.208.142.142

TASK [docker : Install Docker packages.] ***************************************
skipping: [54.208.142.142]

TASK [docker : Install Docker packages (with downgrade option).] ***************
ok: [54.208.142.142]

TASK [docker : Install docker-compose plugin.] *********************************
skipping: [54.208.142.142]

TASK [docker : Install docker-compose-plugin (with downgrade option).] *********
ok: [54.208.142.142]

TASK [docker : Ensure /etc/docker/ directory exists.] **************************
skipping: [54.208.142.142]

TASK [docker : Configure Docker daemon options.] *******************************
skipping: [54.208.142.142]

TASK [docker : Ensure Docker is started and enabled at boot.] ******************
ok: [54.208.142.142]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [docker : include_tasks] **************************************************
skipping: [54.208.142.142]

TASK [docker : Get docker group info using getent.] ****************************
skipping: [54.208.142.142]

TASK [docker : Check if there are any users to add to the docker group.] *******
skipping: [54.208.142.142]

TASK [docker : Ensure docker users are added to the docker group.] *************
skipping: [54.208.142.142]

TASK [docker : Reset ssh connection to apply user changes.] ********************

PLAY RECAP *********************************************************************
54.208.142.142             : ok=13   changed=0    unreachable=0    failed=0    skipped=10   rescued=0    ignored=0 
```

## Inventory Details

```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "54.208.142.142": {
                "ansible_ssh_private_key_file": "${ANSIBLE_KEY}",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws"
        ]
    },
    "aws": {
        "hosts": [
            "54.208.142.142"
        ]
    }
}
```

```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |--@aws:
  |  |--54.208.142.142

```
