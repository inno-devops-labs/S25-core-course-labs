# Ansible

## Existing Ansible Role for Docker

Firstly, I installed existing Ansible role for Docker:

```shell
$ ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /home/dmitriy/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

Using the provided Github page for existing Ansible Role for Docker, I populated `ansible/playbooks/dev/main.yaml` file. Then I created `ansible/inventory/default_aws_ec2.yml` inventory file to point to my Yandex cloud.

So, I developed an Ansible playbook for deploying Docker:

```shell
$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] *************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
included: /home/dmitriy/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for my_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] **********************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker repository.] *************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Install Docker packages.] ***********************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***********************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] *****************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *****************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [my_vm]

PLAY RECAP *****************************************************************************************************************************
my_vm                      : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

Then I tested it by logging into my cloud using SSH (`ssh ubuntu@158.160.34.19`) and running the following command:

```shell
$ docker --version
Docker version 27.5.1, build 9f9e405
```
