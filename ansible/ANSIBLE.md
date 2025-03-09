# Ansible

## Best practices

1. Names for tasks

   Every task has a descriptive name for better readability and debugging.

2. Using Handlers

   Use handlers to restart services only when needed, reducing unnecessary downtime.

3. Checked syntax

   Validated syntax with `ansible-playbook --syntax-check` before deploying to production for errors reducing.

## Docker with `ansible-galaxy`

Playbook to run existing Ansible role:

```yml
    ---
    - name: Install Docker
    hosts: all
    become: true

    roles:
        - geerlingguy.docker
```

As in the task requirements the inventory file is named `default_aws_ec2.yml`, at first I created file with this name and named host
`aws_instance`. Later it was renamed as `yc_instance` and vm from previous lab with terraform was used. Output of
`ansible-playbook -i inventory/default_yandex_cloud.yml playbooks/dev/main.yaml`:

```bash
    PLAY [Install Docker] 
    ************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***********************************************************************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Load OS-specific vars.] 
    *******************************************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : include_tasks] 
    ****************************************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : include_tasks] 
    ****************************************************************************************************************************
    included: 
    /Users/ilsianasibullina/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml 
    for aws_instance

    TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] 
    *******************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure old apt source list is not present in 
    /etc/apt/sources.list.d] 
    *********************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure the repo referencing the previous 
    trusted.gpg.d key is not present] 
    ****************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure old versions of Docker are not 
    installed.] 
    *****************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure dependencies are installed.] 
    *******************************************************************************************************
    changed: [aws_instance]

    TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] 
    ********************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Add Docker apt key.] 
    **********************************************************************************************************************
    changed: [aws_instance]

    TASK [geerlingguy.docker : Ensure curl is present (on older systems 
    without SNI).] 
    ***********************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Add Docker apt key (alternative for older 
    systems without SNI).] 
    **************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Add Docker repository.] 
    *******************************************************************************************************************
    changed: [aws_instance]

    TASK [geerlingguy.docker : Install Docker packages.] 
    *****************************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Install Docker packages (with downgrade 
    option).] 
    *****************************************************************************************
    changed: [aws_instance]

    TASK [geerlingguy.docker : Install docker-compose plugin.] 
    ***********************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade 
    option).] 
    ***********************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] 
    ****************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Configure Docker daemon options.] 
    *********************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] 
    ********************************************************************************************
    ok: [aws_instance]

    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid 
    firewall conflicts.] 
    ****************************************************************************

    RUNNING HANDLER [geerlingguy.docker : restart docker] 
    ****************************************************************************************************************
    changed: [aws_instance]

    TASK [geerlingguy.docker : include_tasks] 
    ****************************************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Get docker group info using getent.] 
    ******************************************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : Check if there are any users to add to the 
    docker group.] 
    *********************************************************************************
    skipping: [aws_instance]

    TASK [geerlingguy.docker : include_tasks] 
    ****************************************************************************************************************************
    skipping: [aws_instance]

    PLAY RECAP 
    ***********************************************************************************************************************************************************
    aws_instance               : ok=15   changed=5    unreachable=0    
    failed=0    skipped=11   rescued=0    ignored=0    
```

## Custom Docker role

The output of command `ansible-playbook -i inventory/default_yandex_cloud.yml playbooks/dev/main.yaml`:

```bash
    PLAY [Install Docker] 
    ************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***********************************************************************************************************************************************
    [WARNING]: Platform linux on host yc_instance is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another 
    Python
    interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html 
    for more
    information.
    ok: [yc_instance]

    TASK [docker : Install required packages] 
    ****************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Add Docker GPG key] 
    ***********************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Add Docker repository] 
    ********************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Install Docker] 
    ***************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Enable and start Docker service] 
    **********************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Download Docker Compose] 
    ******************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Verify Docker Compose installation] 
    *******************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Display installed Docker Compose version] 
    *************************************************************************************************************
    ok: [yc_instance] => {
        "msg": "Docker Compose version v2.32.4"
    }

    TASK [docker : Add current user to the docker group] 
    *****************************************************************************************************************
    changed: [yc_instance]

    PLAY RECAP 
    ***********************************************************************************************************************************************************
    yc_instance                : ok=10   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    ```

    The output of command `ansible-playbook -i inventory/default_yandex_cloud.yml playbooks/dev/main.yaml --check --diff`:

    ```bash

    PLAY [Install Docker] 
    ************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***********************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Install required packages] 
    ****************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Add Docker GPG key] 
    ***********************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Add Docker repository] 
    ********************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Install Docker] 
    ***************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Enable and start Docker service] 
    **********************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Download Docker Compose] 
    ******************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Verify Docker Compose installation] 
    *******************************************************************************************************************
    skipping: [yc_instance]

    TASK [docker : Display installed Docker Compose version] 
    *************************************************************************************************************
    ok: [yc_instance] => {
        "msg": ""
    }

    TASK [docker : Add current user to the docker group] 
    *****************************************************************************************************************
    ok: [yc_instance]

    PLAY RECAP 
    ***********************************************************************************************************************************************************
    yc_instance                : ok=9    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```

The output of command `ansible-inventory -i inventory/default_yandex_cloud.yml --list`:

```bash
    {
        "_meta": {
            "hostvars": {
                "yc_instance": {
                    "ansible_host": "158.160.85.1",
                    "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
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
                "yc_instance"
            ]
        }
    }
```

The output of command `ansible-inventory -i inventory/default_yandex_cloud.yml --graph`:

```bash
    @all:
    |--@ungrouped:
    |  |--yc_instance

```

## Bonus Task

### Dynamic inventory with Yandex cloud

Output of `ansible-inventory -i inventory/yacloud_compute.yml --list`

```bash
    {
        "_meta": {
            "hostvars": {
                "terraform-vm-1": {
                    "ansible_host": "51.250.107.29"
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
                "terraform-vm-1"
            ]
        }
    }

```

### Secure Docker Configuration

Output of running ansible docker role with secure docker configuration:

```bash
    PLAY [Install Docker] 
    ****************************************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***************************************************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Update apt package index] 
    *********************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Install required packages] 
    ********************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Add Docker GPG key] 
    ***************************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Add Docker repository] 
    ************************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Install Docker] 
    *******************************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Enable and start Docker service] 
    **************************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Download Docker Compose] 
    **********************************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Verify Docker Compose installation] 
    ***********************************************************************************************************************************************
    ok: [yc_instance]

    TASK [docker : Display installed Docker Compose version] 
    *****************************************************************************************************************************************
    ok: [yc_instance] => {
        "msg": "Docker Compose version v2.32.4"
    }

    TASK [docker : Add current user to the docker group] 
    *********************************************************************************************************************************************
    changed: [yc_instance]

    TASK [docker : Secure Docker Configuration - Disable Root Access] 
    ********************************************************************************************************************************
    changed: [yc_instance]

    RUNNING HANDLER [docker : Restart Docker] 
    ********************************************************************************************************************************************************
    changed: [yc_instance]

    PLAY RECAP 
    ***************************************************************************************************************************************************************************************
    yc_instance                : ok=13   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Ansible web_app CD

### Task 1 - Simple Ansible Role

In this task I defined variables and added tasks to pull image and start container using ansible. This is the output of running playbook with web_app role with
command `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml`:

```bash
    PLAY [Install Docker] *******************************************************************************************************

    TASK [Gathering Facts] ******************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Update apt package index] ************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Install required packages] ***********************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Add Docker GPG key] ******************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Add Docker repository] ***************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Install Docker] **********************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Enable and start Docker service] *****************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Download Docker Compose] *************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Verify Docker Compose installation] **************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Display installed Docker Compose version] ********************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134] => {
        "msg": "Docker Compose version v2.32.4"
    }

    TASK [docker : Add current user to the docker group] ************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Secure Docker Configuration - Disable Root Access] ***********************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Pull the latest Docker image] *******************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Run the Web App container] **********************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    PLAY RECAP ******************************************************************************************************************
    compute-vm-2-2-20-ssd-1739036897134 : ok=14   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

### Task 2

After applying first three steps of best practices I tried to run specific tag to escape of running same steps^ which have already been done, every time. The
command I used `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml --tags deploy`:

```bash
    PLAY [Install Docker] 
    ****************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Pull the latest Docker image] 
    ****************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Run the Web App container] 
    *******************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    PLAY RECAP 
    ***************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739036897134 : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

Outut of running wipe tasks independently using `wipe` tag in command `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml --tags wipe`:

```bash

    PLAY [Install Docker] 
    ****************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Stop and remove the web app container] 
    *******************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Remove Docker image] 
    *************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Remove application data directory] 
    ***********************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    PLAY RECAP 
    ***************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739036897134 : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

Output of running ansible with docker-compose template `ansible-playbook playbooks/dev/main.yaml -i inventory/yacloud_compute.yml`:

```bash
    PLAY [Install Docker] 
    ****************************************************************************************************************************************************

    TASK [Gathering Facts] 
    ***************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Update apt package index] 
    *********************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Install required packages] 
    ********************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Add Docker GPG key] 
    ***************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Add Docker repository] 
    ************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Install Docker] 
    *******************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Enable and start Docker service] 
    **************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Download Docker Compose] 
    **********************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Verify Docker Compose installation] 
    ***********************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Display installed Docker Compose version] 
    *****************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134] => {
        "msg": "Docker Compose version v2.32.4"
    }

    TASK [docker : Add current user to the docker group] 
    *********************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [docker : Disable Root Access] 
    **************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Stop and remove the web app container] 
    *******************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Remove Docker image] 
    *************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Remove application data directory] 
    ***********************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Ensure Web App Directory Exists] 
    *************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Generate docker-compose.yml file from template] 
    **********************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Pull the latest Docker image] 
    ****************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Ensure Docker service is running] 
    ************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739036897134]

    TASK [web_app : Create and start the services] 
    ***************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739036897134]

    PLAY RECAP 
    ***************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739036897134 : ok=20   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

### Bonus Task - Lab6

Output of running playbook for app_python with command `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/app_python/main.yaml
--tags deploy`:

```bash
    PLAY [Deploy Web App] 
    ******************************************************************************************************************************************************************************

    TASK [Gathering Facts] 
    *****************************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Ensure Web App Directory Exists] 
    ***************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Generate docker-compose.yml file from template] 
    ************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Pull the latest Docker image] 
    ******************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Ensure Docker service is running] 
    **************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Create and start the services] 
    *****************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    PLAY RECAP 
    *****************************************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739276511287 : ok=6    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

Output of running playbook for app_nodejs with command `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/app_nodejs/main.yaml
--tags deploy`:

```bash
    PLAY [Deploy Web App] 
    ******************************************************************************************************************************************************************************

    TASK [Gathering Facts] 
    *****************************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Ensure Web App Directory Exists] 
    ***************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Generate docker-compose.yml file from template] 
    ************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Pull the latest Docker image] 
    ******************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Ensure Docker service is running] 
    **************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739276511287]

    TASK [web_app : Create and start the services] 
    *****************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739276511287]

    PLAY RECAP 
    *****************************************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739276511287 : ok=6    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
