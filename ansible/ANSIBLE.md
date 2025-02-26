# Ansible

## Existing role (`girlingguy/docker`)

### Deploying

```bash
PLAY [Deploy Container] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************
Enter passphrase for key '/home/azeeez/Desktop/ycld': 
[WARNING]: Platform linux on host instance is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [instance]

TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************************************
included: /home/azeeez/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for instance

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************************************************************************************
changed: [instance]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************************************************************************************
changed: [instance]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************************************************************************************
changed: [instance]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************************************************************************************
changed: [instance]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************************************************************************************
ok: [instance]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ******************************************************************************************************************************************************
changed: [instance]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************************************************************************************
skipping: [instance]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************************************************
skipping: [instance]

PLAY RECAP *************************************************************************************************************************************************************************************************
instance                   : ok=15   changed=5    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0  
```

### Checking YCloud (`docker --version`)

```bash
Docker version 27.5.1, build 9f9e405
```

## Custom Role

### Using `--check`

```bash
PLAY [Deploy Container] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************
Enter passphrase for key '/home/azeeez/Desktop/ycld': 
[WARNING]: Platform linux on host instance is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [instance]

TASK [../../roles/docker : include_tasks] ******************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for instance

TASK [../../roles/docker : Install dependencies] ***********************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add GPG key] ********************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add repository] *****************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Install] ************************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Run] ****************************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add user to group] **************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : include_tasks] ******************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for instance

TASK [../../roles/docker : Download Docker Compose] ********************************************************************************************************************************************************
ok: [instance]

PLAY RECAP *************************************************************************************************************************************************************************************************
instance                   : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Deploying

```bash
PLAY [Deploy Container] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host instance is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [instance]

TASK [../../roles/docker : include_tasks] ******************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for instance

TASK [../../roles/docker : Install dependencies] ***********************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add GPG key] ********************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add repository] *****************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Install] ************************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Run] ****************************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : Add user to group] **************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/docker : include_tasks] ******************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for instance

TASK [../../roles/docker : Download Docker Compose] ********************************************************************************************************************************************************
ok: [instance]

PLAY RECAP *************************************************************************************************************************************************************************************************
instance                   : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

**Running `docker --version`**:

```bash
Docker version 27.5.1, build 9f9e405
```

**Running `docker-compose --version`**:

```bash
docker-compose version 1.29.2, build 5becea4c
```

**Running `ansible-inventory -i inventory/default_aws_ec2.yml --list`**:

```bash
{
    "_meta": {
        "hostvars": {
            "instance": {
                "ansible_host": "158.160.49.241",
                "ansible_ssh_private_key_file": "~/Desktop/ycld",
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
            "instance"
        ]
    }
}
```

**Running `ansible-inventory -i inventory/default_aws_ec2.yml --graph`**:

```bash
@all:
  |--@ungrouped:
  |  |--instance
```

## Lab 6 Deployment

```bash
PLAY [Deploy Container] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************
Enter passphrase for key '/home/azeeez/Desktop/ycld': 
[WARNING]: Platform linux on host instance is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [instance]

TASK [docker : include_tasks] ******************************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for instance

TASK [docker : Install dependencies] ***********************************************************************************************************************************************************************
ok: [instance]

TASK [docker : Add GPG key] ********************************************************************************************************************************************************************************
ok: [instance]

TASK [docker : Add repository] *****************************************************************************************************************************************************************************
ok: [instance]

TASK [docker : Install] ************************************************************************************************************************************************************************************
ok: [instance]

TASK [docker : Run] ****************************************************************************************************************************************************************************************
ok: [instance]

TASK [docker : Add user to group] **************************************************************************************************************************************************************************
ok: [instance]

TASK [docker : include_tasks] ******************************************************************************************************************************************************************************
included: /home/azeeez/Desktop/courses/devops/kdi/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for instance

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/web_app : Pull Docker image] *************************************************************************************************************************************************************
ok: [instance]

TASK [../../roles/web_app : Start Docker container] ********************************************************************************************************************************************************
changed: [instance]

PLAY RECAP *************************************************************************************************************************************************************************************************
instance                   : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**We can also verify that the image is isntalled and running in the virtual machine by running `docker image ls` and `docker ps`**

**Running `docker image ls`:**

```bash
REPOSITORY                   TAG       IMAGE ID       CREATED      SIZE
azeeeez/python_moscow_time   latest    27f91384b2fd   4 days ago   67.7MB
```

**Running `docker ps`:**

```bash
CONTAINER ID   IMAGE                        COMMAND           CREATED         STATUS         PORTS                            NAMES
de6207567a97   azeeeez/python_moscow_time   "python app.py"   4 minutes ago   Up 4 minutes   5000/tcp, 0.0.0.0:5000->80/tcp   web_app
```
