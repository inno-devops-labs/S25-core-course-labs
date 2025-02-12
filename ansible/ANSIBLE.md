# Overview

## Best practices implemented

1. Syntax Validation
Before deployment, the playbook's syntax was rigorously validated using the --syntax-check flag to ensure error-free execution.
Additionally, a dry-run simulation was performed with the --check flag to preview changes without applying them, ensuring confidence in the playbook's behavior.
2. Optimized Service Management with Handlers
Handlers were implemented to restart services such as Docker only when necessary. This approach minimizes downtime and optimizes resource usage during playbook execution.
3. Enhanced Readability with Descriptive Task Names
Each task within the playbook is accompanied by a clear and descriptive name. This improves readability and simplifies debugging, making it easier to track progress and resolve issues during execution.
4. Secure Docker Configuration
A dedicated task was included to enhance Docker security by disabling root access. This was achieved by modifying the daemon.json file using Ansible's copy module, ensuring a more secure Docker environment.
5. Pre-Deployment Validation
To mitigate risks associated with production deployments, the playbook underwent comprehensive pre-deployment checks. These included syntax validation and dry-run simulations, ensuring all potential issues were identified and resolved before deployment.

## Outputs

```shell

```bash
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy Docker on Yandex Cloud VM with Custom Docker Role] **********************************************************************************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Load OS-specific vars.] ***********************************************************************************************************************************************************************************************ok: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************************************************************************************included: /root/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_instance_1

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

```shell
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs/ansible# ssh -i ~/.ssh/yacloud rwkals@89.169.162.114 "docker --version"
Docker version 27.5.1, build 9f9e405
```

```shell
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yaml

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

`ansible-inventory -i <name_of_your_inventory_file>.yaml --list`

```shell
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --list
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

`ansible-inventory -i <name_of_your_inventory_file>.yaml --graph`

```shell
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_instance_1
```

## Web App deployment

### Python

```shell

root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-playbook -i ansible/inventory/default_yacloud.yml ansible/playbooks/dev/app_python/main.yml

PLAY [Deploy Python app] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Update apt package index] *******************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [docker : Install required packages] ******************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Enable and start Docker service] ************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Verify Docker Compose installation] *********************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Display installed Docker Compose version] ***************************************************************************************************************************
ok: [yandex_instance_1] => {
    "msg": "Docker Compose version v2.33.0"
}

TASK [docker : Add current user to the docker group] *******************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] ******************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy App] ********************************************************************************************************************************************************
included: /root/.ansible/roles/web_app/tasks/deploy_app.yml for yandex_instance_1

TASK [web_app : Pull Docker image] *************************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [web_app : Start container] ***************************************************************************************************************************************************
[DEPRECATION WARNING]: The default value "ignore" for image_name_mismatch has been deprecated and will change to "recreate" in community.docker 4.0.0. In the current situation, 
this would cause the container to be recreated since the current container's image name "efimpuzhalov/moscow-time-py-app" does not match the desired image name
"rwkals/app_python_distroless". This feature will be removed from community.docker in version 4.0.0. Deprecation warnings can be disabled by setting deprecation_warnings=False in  
ansible.cfg.
changed: [yandex_instance_1]

TASK [web_app : Create directory for docker-compose file] **************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy docker-compose file] ****************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [web_app : Remove container] **************************************************************************************************************************************************
skipping: [yandex_instance_1]

TASK [web_app : Remove docker-compose file] ****************************************************************************************************************************************
skipping: [yandex_instance_1]

PLAY RECAP *************************************************************************************************************************************************************************
yandex_instance_1          : ok=17   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

### Kotlin

```shell
root@DESKTOP-D43KHFL:/mnt/c/Users/egora/PycharmProjects/S25-core-course-labs# ansible-playbook -i ansible/inventory/default_yacloud.yml ansible/playbooks/dev/app_kotlin/main.yml

PLAY [Deploy Python app] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Update apt package index] *******************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [docker : Install required packages] ******************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Enable and start Docker service] ************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Verify Docker Compose installation] *********************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Display installed Docker Compose version] ***************************************************************************************************************************
ok: [yandex_instance_1] => {
    "msg": "Docker Compose version v2.33.0"
}

TASK [docker : Add current user to the docker group] *******************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] ******************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy App] ********************************************************************************************************************************************************
included: /root/.ansible/roles/web_app/tasks/deploy_app.yml for yandex_instance_1


TASK [web_app : Pull Docker image] *************************************************************************************************************************************************changed: [yandex_instance_1]

TASK [web_app : Start container] ***************************************************************************************************************************************************changed: [yandex_instance_1]

TASK [web_app : Create directory for docker-compose file] **************************************************************************************************************************ok: [yandex_instance_1]

TASK [web_app : Deploy docker-compose file] ****************************************************************************************************************************************changed: [yandex_instance_1]

TASK [web_app : Remove container] **************************************************************************************************************************************************skipping: [yandex_instance_1]

TASK [web_app : Remove docker-compose file] ****************************************************************************************************************************************skipping: [yandex_instance_1]

PLAY RECAP *************************************************************************************************************************************************************************yandex_instance_1          : ok=17   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```
