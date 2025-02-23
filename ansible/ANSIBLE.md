# Ansible

## Deployment Output

To deploy the Docker role, execute the following command:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml

PLAY [Install Docker and Deploy Web App] *********************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
ok: [localhost]

TASK [docker : Update apt cache] *****************************************************************************************************************
skipping: [localhost]

TASK [docker : Include Docker installation tasks] ************************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Check if Docker is installed] *****************************************************************************************************
changed: [localhost]

TASK [docker : Install Python dependencies for package management (Debian/Ubuntu)] ***************************************************************
skipping: [localhost]

TASK [docker : Install packages (Arch Linux)] ****************************************************************************************************
skipping: [localhost]

TASK [docker : Install packages (Debian/Ubuntu)] *************************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker GPG key (Debian/Ubuntu)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (Debian/Ubuntu)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker (Debian/Ubuntu)] ***************************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker (Arch Linux)] ******************************************************************************************************
skipping: [localhost]

TASK [docker : Ensure Docker service is enabled and started] *************************************************************************************
ok: [localhost]

TASK [docker : Add users to docker group] ********************************************************************************************************
skipping: [localhost]

TASK [docker : Add current user to docker group] *************************************************************************************************
ok: [localhost]

TASK [docker : Verify Docker Installation] *******************************************************************************************************
ok: [localhost]

TASK [docker : Debug Docker Version] *************************************************************************************************************
ok: [localhost] => {
    "msg": "Docker installed successfully: Docker version 27.5.1, build 9f9e405801"
}

TASK [docker : Include Docker Compose installation tasks] ****************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] **********************************************************************************************************
ok: [localhost]

TASK [web_app : Pull Docker image] ***************************************************************************************************************
ok: [localhost]

TASK [web_app : Create Docker Compose directory] *************************************************************************************************
ok: [localhost]

TASK [web_app : Template Docker Compose file] ****************************************************************************************************
ok: [localhost]

TASK [web_app : Start Docker Compose services] ***************************************************************************************************
ok: [localhost]

TASK [web_app : Start Docker container] **********************************************************************************************************
ok: [localhost]

TASK [web_app : Remove Docker container] *********************************************************************************************************
skipping: [localhost]

TASK [web_app : Remove Docker Compose files] *****************************************************************************************************
skipping: [localhost]

TASK [docker : Restart Docker] *******************************************************************************************************************
ok: [localhost]

PLAY RECAP ***************************************************************************************************************************************
localhost                  : ok=15   changed=1    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0
```

### Sample Deployment Output

Below are the last 50 lines of the output from the deployment command:

```bash
PLAY [Install Docker] ****************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.13, but future installation of another
Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Include Docker installation tasks] ************************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install packages (Arch Linux)] ****************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker GPG key (Debian/Ubuntu)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker GPG key (RedHat/CentOS)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (Debian/Ubuntu)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (RedHat/CentOS)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker packages] **********************************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker packages (Arch Linux)] *********************************************************************************************
ok: [localhost]

TASK [docker : Ensure Docker service is enabled and started] *************************************************************************************
ok: [localhost]

TASK [docker : Add users to docker group] ********************************************************************************************************
skipping: [localhost]

TASK [docker : Add current user to docker group] *************************************************************************************************
ok: [localhost]

TASK [docker : Include Docker Compose installation tasks] ****************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] **********************************************************************************************************
ok: [localhost]

PLAY RECAP ***************************************************************************************************************************************
localhost                  : ok=8    changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0

```

### Dry Run

To perform a dry run and verify changes before applying them, use the `--check` flag:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff --check

PLAY [Install Docker] ****************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.13, but future installation of another
Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Include Docker installation tasks] ************************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install packages (Arch Linux)] ****************************************************************************************************
changed: [localhost]

TASK [docker : Add Docker GPG key (Debian/Ubuntu)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker GPG key (RedHat/CentOS)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (Debian/Ubuntu)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (RedHat/CentOS)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker packages] **********************************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker packages (Arch Linux)] *********************************************************************************************
changed: [localhost]

TASK [docker : Ensure Docker service is enabled and started] *************************************************************************************
ok: [localhost]

TASK [docker : Add users to docker group] ********************************************************************************************************
skipping: [localhost]

TASK [docker : Add current user to docker group] *************************************************************************************************
ok: [localhost]

TASK [docker : Include Docker Compose installation tasks] ****************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] **********************************************************************************************************
changed: [localhost]

PLAY RECAP ***************************************************************************************************************************************
localhost                  : ok=8    changed=3    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0
```

## Inventory Details

### Inventory List

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Output:

```json
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}

```

### Inventory Graph

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Output:

```
@all:
  |--@ungrouped:
  |  |--localhost
```