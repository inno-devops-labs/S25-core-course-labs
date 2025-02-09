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
