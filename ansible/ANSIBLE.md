# Overview

## Best Practices in Ansible Playbook Execution

## 1. Pre-Deployment Validation & Syntax Checking
Before deploying, comprehensive validations were performed. The playbook’s syntax was rigorously checked using the `--syntax-check` flag, and a dry-run simulation was executed with the `--check` flag. This process ensured that all potential issues were identified and resolved before any changes were applied.

## 2. Enhanced Readability and Documentation
Each task is given a clear, descriptive name to improve readability and simplify debugging. In addition, detailed documentation (via README files and an `ANSIBLE.md` document) explains role requirements, configurations, and usage instructions. This makes it easier for team members to understand and maintain the playbook.

## 3. Modular and Idempotent Design
The playbook is organized into modular roles and tasks. This approach ensures idempotence—running the playbook multiple times produces consistent results without unintended changes—and allows for easy reuse and maintenance of components.

## 4. Secure Docker Configuration
A dedicated task enhances Docker’s security by modifying the `daemon.json` file to disable root access. This measure ensures that the Docker environment adheres to security best practices and minimizes potential vulnerabilities.

## 5. Optimized Service Management with Handlers
Handlers are implemented to restart services (such as Docker) only when necessary. By triggering service restarts only after configuration changes, downtime is minimized and resource usage is optimized during the deployment process.


### Running Ansible playbook

Command : ``` ansible-playbook -i ansible/inventory/default_regcloud.yml ansible/playbooks/dev/main.yaml ```

#### Output


```shell 
PLAY [Deploy Docker on yacloud vm with custom docker role] ****************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Load OS-specific vars.] ************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : include_tasks] *********************************************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : include_tasks] *********************************************************************************************************************************************************************
included: /home/anushervon/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for reg_instance_1

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] *********************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **********************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Add Docker apt key.] ***************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ****************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *******************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Add Docker repository.] ************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Install Docker packages.] **********************************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **********************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Install docker-compose plugin.] ****************************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ****************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *********************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Configure Docker daemon options.] **************************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *************************************************************************************************************************************
ok: [reg_instance_1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *********************************************************************************************************************

TASK [geerlingguy.docker : include_tasks] *********************************************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Get docker group info using getent.] ***********************************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **************************************************************************************************************************
skipping: [reg_instance_1]

TASK [geerlingguy.docker : include_tasks] *********************************************************************************************************************************************************************
skipping: [reg_instance_1]

PLAY RECAP ****************************************************************************************************************************************************************************************************
reg_instance_1             : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
```

### Checking Docker Version via SSH

Command: ``` ssh -i ~/.ssh/devops_regru root@193.227.240.176 "docker --version"```

#### Output

```shell
Docker version 27.5.1, build 9f9e405
```

### Running Ansible Playbook (Second Execution)

Command: ```ansible-playbook -i ansible/inventory/default_regcloud.yml ansible/playbooks/dev/main.yaml```

#### Output 

```shell

PLAY [Deploy Docker on regcloud] ******************************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Update apt package index] **********************************************************************************************************************************************************************
changed: [reg_instance_1]

TASK [docker : Install required packages] *********************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Add Docker GPG key] ****************************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Add Docker repository] *************************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Install Docker] ********************************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Enable and start Docker service] ***************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Download Docker Compose] ***********************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Verify Docker Compose installation] ************************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Display installed Docker Compose version] ******************************************************************************************************************************************************
ok: [reg_instance_1] => {
    "msg": "Docker Compose version v2.33.0"
}

TASK [docker : Add current user to the docker group] **********************************************************************************************************************************************************
ok: [reg_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] *********************************************************************************************************************************************
ok: [reg_instance_1]

PLAY RECAP ****************************************************************************************************************************************************************************************************
reg_instance_1             : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### Listing Ansible Inventory

Command: ```ansible-inventory -i ansible/inventory/default_regcloud.yml --list```

#### Output 

```shell
{
    "_meta": {
        "hostvars": {
            "reg_instance_1": {
                "ansible_host": "193.227.240.176",
                "ansible_python_interpreter": "/usr/bin/python3.12",
                "ansible_ssh_private_key_file": "/home/anushervon/.ssh/devops_regru",
                "ansible_user": "root"
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
            "reg_instance_1"
        ]
    }
}
```

### Graphing Ansible Inventory

Command: `ansible-inventory -i ansible/inventory/default_regcloud.yml --graph`

#### Output 

```shell
@all:
  |--@ungrouped:
  |  |--reg_instance_1

```
