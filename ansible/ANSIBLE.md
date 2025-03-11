# Ansible Deployment Documentation

## Playbook Execution Output (with template)

```bash
ansible-playbook -i ./inventory/default_aws_ec2.yml ./playbooks/dev/main.yml
```

Output:

```bash
PLAY [Setup Docker] *********************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [geerlingguy.docker : Load OS-specific vars.] **************************************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
included: /Users/pupolina/Documents/Innopolis/DevOps_labs/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_cloud

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] **************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ****************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ***********************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **************************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ***************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker apt key.] *****************************************************************************************
changed: [yandex_cloud]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ******************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *********************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker repository.] **************************************************************************************
changed: [yandex_cloud]

TASK [geerlingguy.docker : Install Docker packages.] ************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Install docker-compose plugin.] ******************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ******************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***********************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Configure Docker daemon options.] ****************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***********************************************

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Get docker group info using getent.] *************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ****************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

PLAY RECAP ******************************************************************************************************************************
yandex_cloud               : ok=14   changed=2    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
```

```bash
ansible all -m ping
```

Output:

```bash
yandex_cloud | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.12"
    },
    "changed": false,
    "ping": "pong"
}
```

## Playbook Execution Output (without template)

```bash
ansible-playbook -i ./inventory/default_aws_ec2.yml ./playbooks/dev/main.yml --check --diff
```

```bash
PLAY [Setup Docker] *********************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [docker : Install dependencies] ****************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker GPG key] ******************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker repository] ***************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install Docker] **********************************************************************************************************
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following packages will be upgraded:
  docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras
4 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.
changed: [yandex_cloud]

TASK [docker : Install Docker Compose] **************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Enable Docker service on boot] *******************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add user to Docker group] ************************************************************************************************
changed: [yandex_cloud]

PLAY RECAP ******************************************************************************************************************************
yandex_cloud               : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Inventory Details

```bash
ansible-inventory -i ./inventory/default_aws_ec2.yml --list 
```

Output:

```bash
{
    "_meta": {
        "hostvars": {
            "yandex_cloud": {
                "ansible_host": "89.169.144.64",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "polilia"
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
            "yandex_cloud"
        ]
    }
}
```

```bash
ansible-inventory -i ./inventory/default_aws_ec2.yml --graph
```

Output:

```bash
@all:
  |--@ungrouped:
  |  |--yandex_cloud
```

## Lab6: Application Deployment

```bash
ansible-playbook -i ./inventory/default_aws_ec2.yml ./playbooks/dev/main.yml 
```

```bash
PLAY [Deploy application with Docker container] *****************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [docker : Install dependencies] ****************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker GPG key] ******************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker repository] ***************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install Docker] **********************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install Docker Compose] **************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Enable Docker service on boot] *******************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add user to Docker group] ************************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Install pip for Python3 (Debian/Ubuntu)] ********************************************************************************
skipping: [yandex_cloud]

TASK [web_app : Pull Docker image for web_app] ******************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Start web_app container] ************************************************************************************************
changed: [yandex_cloud]

PLAY RECAP ******************************************************************************************************************************
yandex_cloud               : ok=10   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```