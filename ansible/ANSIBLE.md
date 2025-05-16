# Ansible-Based Docker Deployment on AWS EC2

## Project Summary

This lab leverages Ansible to automate the setup of Docker and Docker Compose on a remote AWS EC2 instance. All configuration and task orchestration is handled via Ansible roles and playbooks.

---

## Requirements

- Ansible installed locally
- Access to an AWS EC2 instance
- A valid SSH key configured (exported as `ANSIBLE_KEY`)

---

## Inventory Setup

The `default_aws_ec2.yml` file defines the target host and required SSH variables for Ansible to connect:

```yaml
aws:
  hosts:
    3.86.193.8
  vars:
    ansible_ssh_private_key_file: ${ANSIBLE_KEY}
    ansible_user: ubuntu
```

`ANSIBLE_KEY` should point to the local path of your `.pem` file used to SSH into the instance.

---

## Docker Role Overview

The Docker installation is broken into a modular Ansible role:

- `main.yml` – Entry point for task execution
- `install_docker.yml` – Installs Docker engine
- `install_compose.yml` – Installs Docker Compose

---

## Playbook Execution

The deployment playbook targets the EC2 instance using the Docker role:

```yaml
- name: Setup Docker on EC2
  hosts: aws
  become: true
  roles:
    - roles/docker
```

---

## Running the Playbook

Ensure the environment is properly configured, then run:

```bash
ansible-playbook playbooks/dev/main.yaml
```

---

## Output from Docker Setup

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
included: /home/user/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 3.86.193.8

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

---

## Verifying Docker Installation

You can confirm Docker is running on the EC2 instance with:

```bash
$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Sat 2025-04-03 18:39:32 UTC; 7min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 762 (dockerd)
      Tasks: 8
     Memory: 69.8M (peak: 103.4M)
        CPU: 480ms
     CGroup: /system.slice/docker.service
             └─762 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

---

## Inventory Graph


```bash
$ ansible-inventory --graph
```

Result:

```
@all:
  |--@ungrouped:
  |--@aws:
  |  |--3.86.193.8
```
## Inventory Listing
```bash
$ ansible-inventory --list
```
Result:
```bash
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
---

## Inventory File Reference

```yaml
aws:
  hosts:
    3.86.193.8
  vars:
    ansible_ssh_private_key_file: ${ANSIBLE_KEY}
    ansible_user: ubuntu
```


---
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
included: /home/user/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 3.86.193.8

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

TASK [web_app : Pull the docker image for alimansour000/moscow-time-app] *********
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