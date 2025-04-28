# Ansible
# Deployment output

Current directory: ansible
```bash
ansible-galaxy role install geerlingguy.docker
ansible-playbook playbooks/dev/main-geerlingguy.yaml
```

Output:
```

PLAY [Install Docker using geerlingguy.docker role] ********************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
included: /home/darya/Documents/F25/DevOps/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for my_server

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************************************
changed: [my_server]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************************************************
changed: [my_server]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************************************************
changed: [my_server]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************************************************
changed: [my_server]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************************************************
ok: [my_server]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ******************************************************************************************************************
changed: [my_server]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************************************************
skipping: [my_server]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_server]

PLAY RECAP *************************************************************************************************************************************************************
my_server                  : ok=15   changed=5    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0 

```

```bash
ansible-playbook playbooks/dev/main.yaml
```

Output:

```
(.venv) darya@darya-vivobook:~/Documents/F25/DevOps/ansible$ ansible-playbook playbooks/dev/main.yaml -K
BECOME password: 

PLAY [Install Docker] **************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_server]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /home/darya/Documents/F25/DevOps/ansible/roles/docker/tasks/install_docker.yml for my_server

TASK [docker : Ensure required packages for Docker are installed] ******************************************************************************************************
ok: [my_server]

TASK [docker : Add Docker official GPG key] ****************************************************************************************************************************
ok: [my_server]

TASK [docker : Set up Docker repo] *************************************************************************************************************************************
ok: [my_server]

TASK [docker : Install Docker] *****************************************************************************************************************************************
ok: [my_server]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /home/darya/Documents/F25/DevOps/ansible/roles/docker/tasks/install_compose.yml for my_server

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
ok: [my_server]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /home/darya/Documents/F25/DevOps/ansible/roles/docker/tasks/configure_docker.yml for my_server

TASK [docker : Ensure Docker service is stopped and disabled] **********************************************************************************************************
changed: [my_server]

TASK [docker : Delete Docker socket file if present] *******************************************************************************************************************
ok: [my_server]

TASK [docker : Install required packages for Docker rootless mode] *****************************************************************************************************
ok: [my_server]

TASK [docker : Assign user to docker group] ****************************************************************************************************************************
changed: [my_server]

TASK [docker : Configure Docker daemon to restrict root privileges] ****************************************************************************************************
ok: [my_server]

TASK [docker : Initialize Docker rootless setup for user] **************************************************************************************************************
ok: [my_server]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /home/darya/Documents/F25/DevOps/ansible/roles/docker/tasks/start_docker.yml for my_server

TASK [docker : Start Docker] *******************************************************************************************************************************************
changed: [my_server]

PLAY RECAP *************************************************************************************************************************************************************
my_server                  : ok=17   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
