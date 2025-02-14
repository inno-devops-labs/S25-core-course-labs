# Ansible Docker Deployment

## Deployment output

```bash
> ANSIBLE_ROLES_PATH=ansible/roles ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yaml

PLAY [Install Docker on VM] *******************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm

TASK [docker : Update apt package index] ******************************************************************************************************************************
changed: [yandex_vm]

TASK [docker : Install required packages] *****************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker GPG key] ************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker repository] *********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install Docker] ****************************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Enable and start Docker service] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm

TASK [docker : Install Docker Compose] ********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Verify Docker Compose installation] ********************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Display installed Docker Compose version] **************************************************************************************************************
ok: [yandex_vm] => {
    "msg": "Installed Docker Compose version: Docker Compose version v2.33.0"
}

PLAY RECAP ************************************************************************************************************************************************************
yandex_vm                  : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Inventory list

```bash
> ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_vm": {
                "ansible_host": "158.160.9.225",
                "ansible_ssh_private_key_file": "~/.ssh/my-yandex-key",
                "ansible_user": "renalaty"
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
            "yandex_vm"
        ]
    }
}
```

## Inventory graph

```bash
> ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_vm
```
# Lab 6 Ansible Web App Deployment

```bash
(base) ┌─[renatalatypova@MacBook-Pro-Renata] - [~/PycharmProjects/S25-core-course-labs] - [Fri Feb 14, 17:18]
└─[$] <git:(lab6*)> ANSIBLE_ROLES_PATH=ansible/roles ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/app_python/site.yml

PLAY [all] ************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **********************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] *****************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [Ensure Docker is installed] *************************************************************************************************************************************
included: geerlingguy.docker for yandex_vm

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **********************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] *****************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [web_app : Deploy application with Docker Compose] ***************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Start application] ************************************************************************************************************************************
changed: [yandex_vm]

PLAY RECAP ************************************************************************************************************************************************************
yandex_vm                  : ok=30   changed=1    unreachable=0    failed=0    skipped=22   rescued=0    ignored=0   

```

# Lab 6 Ansible Web App Deployment Bonus task Javascript app
```bash
> ANSIBLE_ROLES_PATH=ansible/roles ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/app_javascript/main.yml

PLAY [all] ************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **********************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] *****************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [Ensure Docker is installed] *************************************************************************************************************************************
included: geerlingguy.docker for yandex_vm

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
included: /Users/renatalatypova/PycharmProjects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] **********************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] *****************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************
ok: [yandex_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************
skipping: [yandex_vm]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************
skipping: [yandex_vm]

TASK [web_app : Deploy application with Docker Compose] ***************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Start application] ************************************************************************************************************************************
changed: [yandex_vm]

PLAY RECAP ************************************************************************************************************************************************************
yandex_vm                  : ok=30   changed=1    unreachable=0    failed=0    skipped=22   rescued=0    ignored=0   
```
