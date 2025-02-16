# Ansible

## `geerlingguy/docker` Docker role 

### Execute playbook

```shell
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```

```text
PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Load OS-specific vars.] *************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
included: /home/anijack/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *************************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] **********************************
ok: [vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************
ok: [vm]

TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************************************************
ok: [vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********************************************
ok: [vm]

TASK [geerlingguy.docker : Add Docker repository.] *************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Install Docker packages.] ***********************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***********************************************************
ok: [vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] *****************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *****************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************************************************
ok: [vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************************************************
ok: [vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ************************************************************************
ok: [vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***************************************************
ok: [vm]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
ok: [vm]

PLAY RECAP *****************************************************************************************************************************
vm                         : ok=25   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Custom Docker role

### Verify playbook

```shell
ansible-playbook ansible/playbooks/dev/main.yaml --check
```

```text
PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [vm]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/c/Users/anija/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm
   
TASK [docker : Ensure dependencies are installed] **************************************************************************************
ok: [vm]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************************
ok: [vm]

TASK [docker : Add Docker gpg key] *****************************************************************************************************
ok: [vm]

TASK [docker : Add Docker repository] **************************************************************************************************
ok: [vm]

TASK [docker : Install Docker] *********************************************************************************************************
ok: [vm]

TASK [docker : Add user to Docker group] ***********************************************************************************************
ok: [vm]

TASK [docker : Disable root access] ****************************************************************************************************
ok: [vm]

TASK [docker : Enable Docker service] **************************************************************************************************
ok: [vm]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/c/Users/anija/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm
   
TASK [docker : Install Docker Compose] *************************************************************************************************
ok: [vm]

PLAY RECAP *****************************************************************************************************************************
vm                         : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Execute playbook

```shell
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
```

```text
PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [vm]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/c/Users/anija/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm
   
TASK [docker : Ensure dependencies are installed] **************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 12 not upgraded.
changed: [vm]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************************
ok: [vm]

TASK [docker : Add Docker gpg key] *****************************************************************************************************
changed: [vm]

TASK [docker : Add Docker repository] **************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu noble stable

changed: [vm]

TASK [docker : Install Docker] *********************************************************************************************************
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-rootless-extras docker-compose-plugin
  libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 12 not upgraded.
changed: [vm]

TASK [docker : Add user to Docker group] ***********************************************************************************************
changed: [vm]

TASK [docker : Disable root access] ****************************************************************************************************
--- before
+++ after: /etc/docker/daemon.json
@@ -0,0 +1,3 @@
+{
+  "userns-remap": "default"
+}

changed: [vm]

TASK [docker : Enable Docker service] **************************************************************************************************
ok: [vm]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/c/Users/anija/Desktop/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm
   
TASK [docker : Install Docker Compose] *************************************************************************************************
changed: [vm]

RUNNING HANDLER [docker : Docker Restart] **********************************************************************************************************************************************
changed: [vm]

PLAY RECAP *****************************************************************************************************************************
vm                         : ok=13   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory Details

```shell
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```

```json
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_host": "10.130.0.19",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/yc_rsa",
                "ansible_user": "anijack"
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
            "vm"
        ]
    }
}
```

```shell
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
```

```text
@all:
  |--@ungrouped:
  |  |--vm
```