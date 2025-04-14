# Ansible

All playbooks is executed by the following command
```bash
ansible-playbook -e "ansible_user=* yc_vm1=* yc_vm2=*" playbooks/dev/main.yml --check
```

## Docker existing role
- Install the existing role `ansible-galaxy role install geerlingguy.docker`
- `geerlingguy.docker` was added in the role folder
- Add the role in playbooks/dev/main.yml
- Run the playbook

The output:
```
PLAY [Install and Configure Docker] **************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************
[WARNING]: Platform linux on host yc_vm_2 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_2]
[WARNING]: Platform linux on host yc_vm_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_1]

TASK [geerlingguy.docker : Load OS-specific vars.] ***********************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************
included: /home/maco/Desktop/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yc_vm_1, yc_vm_2

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ***********************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ********************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *********************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***********************************************************************************************************
changed: [yc_vm_1]
changed: [yc_vm_2]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Add Docker apt key.] **************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ******************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Add Docker repository.] ***********************************************************************************************************************
changed: [yc_vm_1]
changed: [yc_vm_2]

TASK [geerlingguy.docker : Install Docker packages.] *********************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *********************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Install docker-compose plugin.] ***************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ********************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Configure Docker daemon options.] *************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ********************************************************************************

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ********************************************************************************

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Get docker group info using getent.] **********************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************************************
skipping: [yc_vm_1]
skipping: [yc_vm_2]

PLAY RECAP ***************************************************************************************************************************************************************
yc_vm_1                    : ok=14   changed=2    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
yc_vm_2                    : ok=14   changed=2    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
```

## Custom docker 
- I created docker role
- Docker role contains tasks
- Tasks contains 3 modules: 1 configuration, 2 install docker and docker-compose, 3 main that includes modules before
- configuration.yml modules was written based on the official docker installation guide https://docs.docker.com/engine/install/ubuntu/
- install_docker.yml includes download docker and docker-compose and it's service enabling
- Run the playbook

The output:
```
PLAY [Install and Configure Docker] **************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************
[WARNING]: Platform linux on host yc_vm_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_1]
[WARNING]: Platform linux on host yc_vm_2 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_2]

TASK [docker : include_tasks] ********************************************************************************************************************************************
included: /home/maco/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/configuration.yml for yc_vm_1, yc_vm_2

TASK [docker : Update apt cache and install prerequisites] ***************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Create /etc/apt/keyrings directory] ***********************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Download Docker's official GPG key] ***********************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Add Docker apt repository] ********************************************************************************************************************************
changed: [yc_vm_1]
changed: [yc_vm_2]

TASK [docker : Update apt cache after adding Docker repository] **********************************************************************************************************
changed: [yc_vm_1]
changed: [yc_vm_2]

TASK [docker : include_tasks] ********************************************************************************************************************************************
included: /home/maco/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yc_vm_1, yc_vm_2

TASK [docker : Install Docker] *******************************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Start and enable service docker] **************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Create docker group] **************************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Add user to docker group] *********************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

PLAY RECAP ***************************************************************************************************************************************************************
yc_vm_1                    : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
yc_vm_2                    : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Web app
- if VM is not stopped then it can be accessd via `http://158.160.164.193:8000/`

The output of the run playbook command:
```
PLAY [Install and Configure Docker] **************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************
[WARNING]: Platform linux on host yc_vm_1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_1]
[WARNING]: Platform linux on host yc_vm_2 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yc_vm_2]

TASK [docker : include_tasks] ********************************************************************************************************************************************
included: /home/maco/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/configuration.yml for yc_vm_1, yc_vm_2

TASK [docker : Update apt cache and install prerequisites] ***************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Create /etc/apt/keyrings directory] ***********************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Download Docker's official GPG key] ***********************************************************************************************************************
ok: [yc_vm_2]
ok: [yc_vm_1]

TASK [docker : Add Docker apt repository] ********************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Update apt cache after adding Docker repository] **********************************************************************************************************
changed: [yc_vm_1]
changed: [yc_vm_2]

TASK [docker : include_tasks] ********************************************************************************************************************************************
included: /home/maco/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yc_vm_1, yc_vm_2

TASK [docker : Install Docker] *******************************************************************************************************************************************
ok: [yc_vm_2]
ok: [yc_vm_1]

TASK [docker : Start and enable service docker] **************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Create docker group] **************************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [docker : Add user to docker group] *********************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [web_app : Pull the latest Docker image] ****************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

TASK [web_app : Run Docker container] ************************************************************************************************************************************
ok: [yc_vm_1]
ok: [yc_vm_2]

PLAY RECAP ***************************************************************************************************************************************************************
yc_vm_1                    : ok=14   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
yc_vm_2                    : ok=14   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
