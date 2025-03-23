# Ansible and Docker Deployment

## Overview

This document describes the steps taken to set up Ansible for deploying Docker on a cloud VM. It includes repository structuring, installation of Ansible, using an Ansible role from Ansible Galaxy, and testing the playbook to ensure correct deployment.

## Installing Ansible

To install Ansible, follow the official [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

## Using Ansible Galaxy for Docker Role

We use the `geerlingguy.docker` role from Ansible Galaxy to simplify Docker installation.

Install the role:

```sh
ansible-galaxy install geerlingguy.docker
```

---

## Playbook for Docker Deployment

The playbook for deploying Docker is defined as follows:

```yaml
---
- name: Ansible and Docker Deployment
  hosts: all
  remote_user: ubuntu
  roles:
    - geerlingguy.docker
```

### Inventory File (`inventory/default_aws_ec2.yml`)

```yaml
aws:
  hosts: ec2-3-92-134-8.compute-1.amazonaws.com
  vars:
    ansible_ssh_private_key_file: ~/.ssh/haidars_aws_academy.pem
    ansible_user: ubuntu
```

---

## Running the Playbook

To execute the playbook, run:

```sh
ansible-playbook -i ./inventory/default_aws_ec2.yml ./playbooks/dev/main.yaml
```

## Task 2: Custom Docker Role

### Tasks in the Role

1. **Install Docker and Docker Compose**:
   - Handled in `install_docker.yml` and `install_compose.yml`.
2. **Configure Docker to start on boot**:
   - Handled in `main.yml` using the `service` module.
3. **Add the current user to the `docker` group**:
   - Handled in `docker_users.yml`.
     Tasks in the Role
4. **Secure Docker Configuration**:
   - Handled in `secure_docker.yml` by modifying the `daemon.json` file.

### Playbook for Custom Role

The playbook `main.yaml` was updated to use the custom role:

```yaml
---
- name: Ansible and Docker Deployment
  hosts: aws
  become: true
  roles:
    - roles/docker
```

### Testing the Custom Role

The playbook was tested using the following commands:

#### Dry Run

```sh
ansible-playbook playbooks/dev/main.yaml --check
```

#### Apply Changes

```sh
ansible-playbook playbooks/dev/main.yaml
```

### Verification

After running the playbook, the Docker version was checked on the target machine to confirm the installation:

```sh
docker --version
```

Output:

```sh
Docker version 24.0.7, build afdd53b
```

---

## Deployment Output

The playbook was executed to deploy the Docker role. Below are the last 50 lines of the output:

```sh
PLAY [Ansible and Docker Deployment] **************************************************************************************************************\*\*\*\***************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************\*\***********************************************************************************************************************
[WARNING]: Platform linux on host ec2-3-92-134-8.compute-1.amazonaws.com is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************\*\*\*******************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/setup_debian.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Ensure apt key is not present in trusted.gpg.d] **************************************************************************************************\*\***************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **************************************************************************************\*\*\*\***************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ************************************************************************************\*\*\*************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure old versions of Docker are not installed] **************************************************************************************************\***************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure dependencies are installed] ********************************************************************************************************\*\*\*********************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************************************************\*\*\***************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Add Docker apt key] ****************************************************************************************************************\*\*****************************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Add Docker repository] **************************************************************************************************************\*\*\***************************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************\*\*\*******************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Install Docker packages] **************************************************************************************************************\***************************************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************\*\*\*******************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Install docker-compose plugin] **********************************************************************************************************\*\*\***********************************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************\*\*\*******************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Ensure /etc/docker directory exists] ********************************************************************************************************\*********************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure Docker daemon.json exists with secure configuration] ********************************************************************************************\*\*********************************************************************************************
changed: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure Docker is started and enabled at boot] **************************************************************************************************\*\*\*\***************************************************************************************************
changed: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts] ******************************************************************************************\*\*\*\*******************************************************************************************

RUNNING HANDLER [docker : restart docker] ************************************************************************************************************\*\*\*************************************************************************************************************
changed: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Get docker group info using getent] ********************************************************************************************************\*\*********************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Check if there are any users to add to the docker group] **********************************************************************************************\***********************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com] => (item=ubuntu)

TASK [docker : include_tasks] ******************************************************************************************************************\*\*\*******************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/docker_users.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Ensure docker users are added to the docker group] ************************************************************************************************\*\*\*************************************************************************************************
changed: [ec2-3-92-134-8.compute-1.amazonaws.com] => (item=ubuntu)

TASK [docker : Reset SSH connection to apply user changes] ****************************************************************************************************\*\*****************************************************************************************************

PLAY RECAP ****************************************************************************************************************************\*\*****************************************************************************************************************************
ec2-3-92-134-8.compute-1.amazonaws.com : ok=21 changed=4 unreachable=0 failed=0 skipped=2 rescued=0 ignored=0
```

### Dry Run Output

A dry run was performed using the `--check` flag to verify changes before applying them:

```sh
ansible-playbook playbooks/dev/main.yaml --check
```

Output:

```sh
PLAY [Ansible and Docker Deployment] ******************************************************************************************************\*\*\*******************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************\***************************************************************************************************************
[WARNING]: Platform linux on host ec2-3-92-134-8.compute-1.amazonaws.com is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************\*\***********************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/setup_debian.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Ensure apt key is not present in trusted.gpg.d] ******************************************************************************************\*******************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ******************************************************************************\*\*\*******************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ****************************************************************************\*\*****************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure old versions of Docker are not installed] ****************************************************************************************\*\*\*\*****************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure dependencies are installed] ************************************************************************************************\*\*************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] ******************************************************************************************\*\*******************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Add Docker apt key] ********************************************************************************************************\*********************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Add Docker repository] ******************************************************************************************************\*\*******************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************\*\***********************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Install Docker packages] ****************************************************************************************************\*\*\*\*****************************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************\*\***********************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Install docker-compose plugin] **************************************************************************************************\*\***************************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************\*\***********************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-3-92-134-8.compute-1.amazonaws.com

TASK [docker : Ensure /etc/docker directory exists] **********************************************************************************************\*\*\*\***********************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure Docker daemon.json exists with secure configuration] ************************************************************************************\*************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure Docker is started and enabled at boot] ******************************************************************************************\*\*\*******************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts] **********************************************************************************\*\*\***********************************************************************************

TASK [docker : Get docker group info using getent] ************************************************************************************************\*************************************************************************************************
ok: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : Check if there are any users to add to the docker group] ************************************************************************************\*\*\*\*************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com] => (item=ubuntu)
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************\*\***********************************************************************************************************
skipping: [ec2-3-92-134-8.compute-1.amazonaws.com]

PLAY RECAP ********************************************************************************************************************\*********************************************************************************************************************
ec2-3-92-134-8.compute-1.amazonaws.com : ok=17 changed=0 unreachable=0 failed=0 skipped=4 rescued=0 ignored=0
```

---

## Inventory Details

The inventory file `default_aws_ec2.yml` defines the target host and connection details. Below are the inventory details:

### Inventory Listing

To list the inventory details, run:

```sh
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Output:

```json
{
  "\_meta": {
  "hostvars": {
    "ec2-3-92-134-8.compute-1.amazonaws.com": {
        "ansible_ssh_private_key_file": "~/.ssh/haidars_aws_academy.pem",
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
        "ec2-3-92-134-8.compute-1.amazonaws.com"
      ]
    }
  }
}

```

### Inventory Graph

To visualize the inventory structure, run:

```sh
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Output:

```sh
@all:
|--@ungrouped:
|--@aws:
| |--ec2-3-92-134-8.compute-1.amazonaws.com
```

### Inventory File

The inventory file `default_aws_ec2.yml` is structured as follows:

```yaml
---
plugin: aws_ec2
regions:
  - us-east-1
filters:
  instance-state-name: running
```

---

## Best Practices for Building the Role

The custom Docker role follows these key Ansible best practices:

### 1. **Role Structure**

- Standard directory structure with `defaults`, `handlers`, and `tasks`
- Modular task files for better organization

### 2. **Idempotency & Error Handling**

- Tasks are idempotent and include proper error handling
- Service and user modules used appropriately

### 3. **Variables & Handlers**

- Role variables defined in `defaults/main.yml`
- Handlers restart Docker only when needed

### 4. **Code Quality**

- Validated with `ansible-lint` for best practices
- Run linting with:

  ```sh
  ansible-lint ansible
  ```

## Web App Deployment Output

```sh
TASK [docker : Install docker-compose plugin] **************************************************************************************************************************************\*\*\***************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : include_tasks] **********************************************************************************************************************************************\*\*\***********************************************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-3-95-56-237.compute-1.amazonaws.com

TASK [docker : Ensure /etc/docker directory exists] ************************************************************************************************************************************\*************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Ensure Docker daemon.json exists with secure configuration] ************************************************************************************************************************\*\*************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Ensure Docker daemon is running] **************************************************************************************************************************************\***************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Verify Docker is running] ****************************************************************************************************************************************\*\*\*\*****************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts] **********************************************************************************************************************\*\*\*\***********************************************************************************************************************

RUNNING HANDLER [docker : restart docker] ****************************************************************************************************************************************\*\*\*****************************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Get docker group info using getent] ************************************************************************************************************************************\*\*************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [docker : Check if there are any users to add to the docker group] **************************************************************************************************************************\***************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com] => (item=ubuntu)

TASK [docker : include_tasks] **********************************************************************************************************************************************\*\*\***********************************************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/docker/tasks/docker_users.yml for ec2-3-95-56-237.compute-1.amazonaws.com

TASK [docker : Ensure docker users are added to the docker group] ****************************************************************************************************************************\*\*\*****************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com] => (item=ubuntu)

TASK [docker : Reset SSH connection to apply user changes] ********************************************************************************************************************************\*\*********************************************************************************************************************************

TASK [web_app : Pull Docker image] ********************************************************************************************************************************************\*\*********************************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [web_app : Start Docker container] ******************************************************************************************************************************************\*******************************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [web_app : Execute wipe logic if enabled] **************************************************************************************************************************************\*\***************************************************************************************************************************************
included: /Users/haidarjbeily/MyWorkspaces/Haidar/github/S25-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for ec2-3-95-56-237.compute-1.amazonaws.com

TASK [web_app : Remove existing web_app(moscow_time) container] ******************************************************************************************************************************\*******************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [web_app : Remove leftover Docker files] **************************************************************************************************************************************\*\*\***************************************************************************************************************************************
ok: [ec2-3-95-56-237.compute-1.amazonaws.com]

TASK [web_app : Deploy Docker Compose File] ****************************************************************************************************************************************\*****************************************************************************************************************************************
changed: [ec2-3-95-56-237.compute-1.amazonaws.com]

PLAY RECAP ********************************************************************************************************************************************************\*\*********************************************************************************************************************************************************
ec2-3-95-56-237.compute-1.amazonaws.com : ok=30 changed=7 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```
