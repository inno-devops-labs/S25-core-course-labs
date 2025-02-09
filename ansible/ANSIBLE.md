# Ansible

## Best Practices Implemented in This Lab  

1. Pre-Execution Validation  

    - Dry-Run Execution : Before executing the playbook, it was run in dry-run mode using the --check flag to simulate changes without applying them.
    - Syntax Check : The playbook's syntax was validated using the --syntax-check flag to ensure there were no errors before deployment.

2. Use of Handlers  

    - Handlers were used to ensure that services like Docker are only restarted when necessary. This minimizes unnecessary downtime and optimizes resource usage.

3. Descriptive Task Names  

    - Every task in the playbook has a clear and descriptive name, improving readability and simplifying debugging during execution.

4. Secure Docker Configuration  

    - A task was added to configure Docker security settings:
        Disable Root Access : Modified the daemon.json file using the copy module to disable root access for Docker, enhancing security.

5. Validated Syntax Before Deployment  

    - The playbook was thoroughly checked with ansible-playbook --syntax-check to identify and fix any potential issues before deploying to production, reducing the risk of errors.

## Roles Utilizing for docker with template

```bash
yeaphm@DESKTOP-A1FDFJ3:/mnt/e/Documents/Innop/C3/S2/devops/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy Docker on Yandex Cloud VM with Custom Docker Role] **********************************************************************************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Load OS-specific vars.] ***********************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************included: /home/yeaphm/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_instance_1

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ***********************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ********************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *********************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***********************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Add Docker apt key.] **************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ******************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Add Docker repository.] ***********************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Install Docker packages.] *********************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *********************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Install docker-compose plugin.] ***************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ********************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Configure Docker daemon options.] *************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ********************************************************************************************************************************************************

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Get docker group info using getent.] **********************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

PLAY RECAP ***************************************************************************************************************************************************************************************************************************************yandex_instance_1          : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

### Check docker installed

```bash
yeaphm@DESKTOP-A1FDFJ3:/mnt/e/Documents/Innop/C3/S2/devops/S25-core-course-labs$ ssh -i ~/.ssh/yacloud rwkals@89.169.162.114 "docker --version"
Docker version 27.5.1, build 9f9e405
```

## Custom docker role with BONUS Secure Config

```bash
yeaphm@DESKTOP-A1FDFJ3:/mnt/e/Documents/Innop/C3/S2/devops/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy Docker on Yandex Cloud VM with Custom Docker Role] **********************************************************************************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Update apt package index] *********************************************************************************************************************************************************************************************************changed: [yandex_instance_1]

TASK [docker : Install required packages] ********************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] ***************************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Add Docker repository] ************************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Install Docker] *******************************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Enable and start Docker service] **************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] **********************************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Verify Docker Compose installation] ***********************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Display installed Docker Compose version] *****************************************************************************************************************************************************************************************ok: [yandex_instance_1] => {
    "msg": "Docker Compose version v2.32.4"
}

TASK [docker : Add current user to the docker group] *********************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] ********************************************************************************************************************************************************************************ok: [yandex_instance_1]

PLAY RECAP ***************************************************************************************************************************************************************************************************************************************yandex_instance_1          : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Ansible Inventory

`--list`

```bash
yeaphm@DESKTOP-A1FDFJ3:/mnt/e/Documents/Innop/C3/S2/devops/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_instance_1": {
                "ansible_host": "89.169.162.114",
                "ansible_ssh_private_key_file": "~/.ssh/yacloud",
                "ansible_user": "rwkals"
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
            "yandex_instance_1"
        ]
    }
}
```

`--graph`

```bash
yeaphm@DESKTOP-A1FDFJ3:/mnt/e/Documents/Innop/C3/S2/devops/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_instance_1
```
