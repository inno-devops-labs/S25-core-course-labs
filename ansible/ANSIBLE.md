# Docker with Ansible

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
    3.86.193.8
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
   ansible-playbook playbooks/dev/main.yaml
   ```

## Docker Installation Logs

```bash
TASK [docker : Install Docker packages.] ***************************************
skipping: [3.86.193.8]

TASK [docker : Install Docker packages (with downgrade option).] ***************
ok: [3.86.193.8]

TASK [docker : Install docker-compose plugin.] *********************************
skipping: [3.86.193.8]

TASK [docker : Install docker-compose-plugin (with downgrade option).] *********
ok: [3.86.193.8]

TASK [docker : Ensure /etc/docker/ directory exists.] **************************
skipping: [3.86.193.8]

TASK [docker : Configure Docker daemon options.] *******************************
skipping: [3.86.193.8]

TASK [docker : Ensure Docker is started and enabled at boot.] ******************
ok: [3.86.193.8]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [docker : include_tasks] **************************************************
included: /home/moze/Documents/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 3.86.193.8

TASK [docker : Check current docker-compose version.] **************************
ok: [3.86.193.8]

TASK [docker : set_fact] *******************************************************
skipping: [3.86.193.8]

TASK [docker : Delete existing docker-compose version if it different.] ******
skipping: [3.86.193.8]

TASK [docker : Install Docker Compose (if configured).] ************************
changed: [3.86.193.8]

TASK [docker : Get docker group info using getent.] ****************************
skipping: [3.86.193.8]

TASK [docker : Check if there are any users to add to the docker group.] *******
skipping: [3.86.193.8]

TASK [docker : Ensure docker users are added to the docker group.] *************
skipping: [3.86.193.8]

TASK [docker : Reset ssh connection to apply user changes.] ********************

PLAY RECAP *********************************************************************
3.86.193.8                 : ok=16   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

If we go login to our instance we can see that the docker service is running:

```bash
$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Sat 2025-02-15 13:39:32 UTC; 8min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 762 (dockerd)
      Tasks: 8
     Memory: 69.8M (peak: 103.4M)
        CPU: 480ms
     CGroup: /system.slice/docker.service
             └─762 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

```bash
$ docker-compose version
Docker Compose version v2.32.1
```

## Inventory Details

```bash
$ ansible-inventory --list
{
    "_meta": {
        "hostvars": {
            "3.86.193.8": {
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
            "3.86.193.8"
        ]
    }
}
```

```bash
$ ansible-inventory --graph
@all:
  |--@ungrouped:
  |--@aws:
  |  |--3.86.193.8
```

Inventory code:

```yaml
# https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html
aws:
  hosts:
    3.86.193.8 # IP address of our instance
  vars:
    ansible_ssh_private_key_file: ${ANSIBLE_KEY} # Path to the SSH key (.pem file) stored in the machine as an environment variable
    ansible_user: ubuntu # The username used to access the instance
```

## Application Deployment

### Application Deployment Logs

```bash
TASK [docker : Ensure /etc/docker/ directory exists.] **************************
skipping: [3.86.193.8]

TASK [docker : Configure Docker daemon options.] *******************************
skipping: [3.86.193.8]

TASK [docker : Ensure Docker is started and enabled at boot.] ******************
ok: [3.86.193.8]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [docker : include_tasks] **************************************************
included: /home/moze/Documents/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 3.86.193.8

TASK [docker : Check current docker-compose version.] **************************
ok: [3.86.193.8]

TASK [docker : set_fact] *******************************************************
ok: [3.86.193.8]

TASK [docker : Delete existing docker-compose version if its different.] ******
skipping: [3.86.193.8]

TASK [docker : Install Docker Compose (if configured).] ************************
skipping: [3.86.193.8]

TASK [docker : Get docker group info using getent.] ****************************
skipping: [3.86.193.8]

TASK [docker : Check if there are any users to add to the docker group.] *******
skipping: [3.86.193.8]

TASK [docker : Ensure docker users are added to the docker group.] *************
skipping: [3.86.193.8]

TASK [docker : Reset ssh connection to apply user changes.] ********************

TASK [web_app : Pull the docker image for hayderuni/moscow-time-flask] *********
ok: [3.86.193.8]

TASK [web_app : Run the docker container] **************************************
changed: [3.86.193.8]

TASK [web_app : Deliver the docker-compose.yml file] ***************************
ok: [3.86.193.8]

TASK [web_app : include_tasks] *************************************************
skipping: [3.86.193.8]

PLAY RECAP *********************************************************************
3.86.193.8                 : ok=19   changed=1    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

### Playbook Changes

After adding a the new role we added a dependency in the `meta/main.yml`:

```yaml
dependencies:
  - role: roles/docker
```

This will execute the role `docker` even if it wasn't mentioned in the playbook.
