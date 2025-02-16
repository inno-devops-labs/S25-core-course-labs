# 1 Task

## Use an Existing Ansible Role for Docker

```
ansible-galaxy role install geerlingguy.docker
```
```
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /home/angelika2707/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

## Create a Playbook and Testing

```
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```
```
PLAY [Install and Configure Docker] ************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
included: /home/angelika2707/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for my_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************************************************
changed: [my_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************************************************
changed: [my_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************************************************
changed: [my_vm]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************************************************
changed: [my_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************************************************
ok: [my_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ******************************************************************************************************************
changed: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************************************************
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************************************
skipping: [my_vm]

PLAY RECAP *************************************************************************************************************************************************************
my_vm                      : ok=15   changed=5    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

## Test

```
ssh -i ~/.ssh/id_rsa angelika2707@51.250.98.0
```
```
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat Feb 15 11:17:54 PM UTC 2025

  System load:  0.01              Processes:             136
  Usage of /:   35.7% of 9.76GB   Users logged in:       0
  Memory usage: 13%               IPv4 address for eth0: 10.129.0.18
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

21 updates can be applied immediately.
5 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Sat Feb 15 22:59:37 2025 from 188.130.155.167
```

```
angelika2707@valera:~$ docker --version
```
```
Docker version 27.5.1, build 9f9e405
```

# 2 Task

## Custom Docker Role
```
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```
```
PLAY [Install and Configure Docker] ************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my_vm

TASK [docker : Install prerequisites] **********************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add GPG key] ********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker repository to APT] ***************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install Docker] *****************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for my_vm

TASK [docker : Download Docker Compose] ********************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/setup.yml for my_vm

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [my_vm]

TASK [docker : Disable root login] *************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Start the Docker service] *******************************************************************************************************************************
ok: [my_vm]

PLAY RECAP *************************************************************************************************************************************************************
my_vm                      : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Testing
```
angelika2707@valera:~$ docker --version
Docker version 27.5.1, build 9f9e405
```
```
angelika2707@valera:~$ docker compose version
Docker Compose version v2.32.4
```
```
angelika2707@valera:~$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Sat 2025-02-15 22:59:39 UTC; 1h 27min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 3339 (dockerd)
      Tasks: 9
     Memory: 20.3M (peak: 21.5M)
        CPU: 652ms
     CGroup: /system.slice/docker.service
             └─3339 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```
```
angelika2707@valera:~$ groups
angelika2707 docker google-sudoers
```
## Deployment Output
```
ansible-playbook ansible/playbooks/dev/main.yaml --check
```

```
PLAY [Install and Configure Docker] ************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my_vm

TASK [docker : Install prerequisites] **********************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add GPG key] ********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker repository to APT] ***************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install Docker] *****************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for my_vm

TASK [docker : Download Docker Compose] ********************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/setup.yml for my_vm

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [my_vm]

TASK [docker : Disable root login] *************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Start the Docker service] *******************************************************************************************************************************
ok: [my_vm]

PLAY RECAP *************************************************************************************************************************************************************
my_vm                      : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```
ansible-playbook ansible/playbooks/dev/main.yaml --diff
```
```
PLAY [Install and Configure Docker] ************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my_vm

TASK [docker : Install prerequisites] **********************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add GPG key] ********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker repository to APT] ***************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install Docker] *****************************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for my_vm

TASK [docker : Download Docker Compose] ********************************************************************************************************************************
ok: [my_vm]

TASK [docker : include_tasks] ******************************************************************************************************************************************
included: /mnt/c/Users/anzel/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/setup.yml for my_vm

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [my_vm]

TASK [docker : Disable root login] *************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Start the Docker service] *******************************************************************************************************************************
ok: [my_vm]

PLAY RECAP *************************************************************************************************************************************************************
my_vm                      : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details
```
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```
```
{
    "_meta": {
        "hostvars": {
            "my_vm": {
                "ansible_host": "51.250.98.0",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "angelika2707"
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
            "my_vm"
        ]
    }
}
```

```
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
```
```
@all:
  |--@ungrouped:
  |  |--my_vm
```