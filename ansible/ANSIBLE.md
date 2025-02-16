# Lab 5

1. ```bash ansible-playbook playbooks/dev/main.yaml --check```
```
PLAY [Deploying docker] ************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Install docker] *****************************************************************************************************************************************************
included: /home/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install prerequisites] **********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
changed: [localhost]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [localhost]

TASK [docker : Ensure Docker service is enabled and running] ***********************************************************************************************************************
ok: [localhost]

TASK [docker : Add users to the Docker group] **************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Verify Docker installation] *****************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Display Docker version] *********************************************************************************************************************************************
ok: [localhost] => {
    "msg": ""
}

TASK [docker : Install docker compose] *********************************************************************************************************************************************
included: /home/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Verify Docker Compose installation] *********************************************************************************************************************************
skipping: [localhost]

TASK [docker : Display Docker Compose version] *************************************************************************************************************************************
ok: [localhost] => {
    "msg": ""
}

PLAY RECAP *************************************************************************************************************************************************************************
localhost                  : ok=11   changed=4    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```

2. ```bash 
    ansible-inventory -i inventory/default_aws_ec2.yml --list
    ```
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
            "ungrouped",
            "local"
        ]
    },
    "local": {
        "hosts": [
            "localhost"
        ]
    }
}


2. ```bash 
   ansible-inventory -i inventory/default_aws_ec2.yml --graph
   ```
```
@all:
  |--@ungrouped:
  |--@local:
  |  |--localhost
```

# Lab 6
1. ```bash 
   ansible-playbook playbooks/dev/main.yaml --check
   ```
```
PLAY [Deploying docker] ************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************
included: /home/devops/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for localhost

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************************************************************
changed: [localhost]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************************************************************

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************
skipping: [localhost]

TASK [web_app : Install Docker] ****************************************************************************************************************************************************
changed: [localhost]

TASK [web_app : Start Docker Service] **********************************************************************************************************************************************
ok: [localhost]

TASK [web_app : Pull Docker Image] *************************************************************************************************************************************************
ok: [localhost]

TASK [web_app : Deploy Docker Compose File] ****************************************************************************************************************************************
changed: [localhost]

TASK [web_app : Start Container] ***************************************************************************************************************************************************
skipping: [localhost]

PLAY RECAP *************************************************************************************************************************************************************************
localhost                  : ok=18   changed=3    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```