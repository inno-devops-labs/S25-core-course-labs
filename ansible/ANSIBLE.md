# Ansible

## Installation

I have installed Ansible before, basically I remember that I just followed instructions for installation on WSL.

## Using existing ansible role for Docker

First of all, we need to install by:

```bash
ansible-galaxy install geerlingguy.docker
```

Then paste role name `playbooks/dev/main.yaml`. In inventory we should specify to run by root, write down hosts IP, user and path to ssh key to connect, also there was some issue, so I added lines for python interpreter.

```bash
$ ansible-playbook -i inventory/default_yc.yml playbooks/dev/main.yaml
[WARNING]: Ansible is being run in a world writable directory (/mnt/c/users/muhammad/devops-fork/ansible), ignoring it as an ansible.cfg
source. For more information see https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir

PLAY [all] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************************
ok: [host_01]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************
included: /home/user/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for host_01

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************************
changed: [host_01]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************************
changed: [host_01]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************************
changed: [host_01]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************************
changed: [host_01]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ******************************************************************************************
changed: [host_01]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************************
skipping: [host_01]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************************
skipping: [host_01]

PLAY RECAP *************************************************************************************************************************************
host_01                    : ok=15   changed=5    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

## Test

To ensure that we have installed docker, we can connect to vm and check:

```bash
$ ssh -i .\id_ed255 ubuntu@158.160.88.93
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Feb 16 02:17:51 PM UTC 2025

  System load:  0.0                Processes:             139
  Usage of /:   17.8% of 19.59GB   Users logged in:       1
  Memory usage: 13%                IPv4 address for eth0: 192.168.10.11
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

16 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Sun Feb 16 12:37:53 2025 from 176.15.222.92
ubuntu@epd6j4q4rtdfqj3do4fu:~$ docker --version
Docker version 27.5.1, build 9f9e405
```

## Custom Docker role

Run:

```bash
$ ansible-playbook -i inventory/default_yc.yml playbooks/dev/main.yaml

PLAY [all] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-docker.yml for host_01

TASK [docker : install dependencies] ***********************************************************************************************************
ok: [host_01] => (item=apt-transport-https)
ok: [host_01] => (item=ca-certificates)
ok: [host_01] => (item=curl)
ok: [host_01] => (item=gnupg-agent)
ok: [host_01] => (item=software-properties-common)

TASK [docker : add GPG key] ********************************************************************************************************************
changed: [host_01]

TASK [docker : add docker repository to apt] ***************************************************************************************************
changed: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
ok: [host_01] => (item=docker-ce)
ok: [host_01] => (item=docker-ce-cli)
ok: [host_01] => (item=containerd.io)

TASK [docker : adding ubuntu to docker group] **************************************************************************************************
changed: [host_01]

TASK [docker : install docker compose] *********************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-compose.yml for host_01

TASK [docker : Install docker-compose] *********************************************************************************************************
changed: [host_01]

TASK [docker : Change file ownership, group and permissions] ***********************************************************************************
changed: [host_01]

PLAY RECAP *************************************************************************************************************************************
host_01                    : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```bash
$ ansible-playbook -i inventory/default_yc.yml playbooks/dev/main.yaml --check

PLAY [all] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-docker.yml for host_01

TASK [docker : install dependencies] ***********************************************************************************************************
ok: [host_01] => (item=apt-transport-https)
ok: [host_01] => (item=ca-certificates)
ok: [host_01] => (item=curl)
ok: [host_01] => (item=gnupg-agent)
ok: [host_01] => (item=software-properties-common)

TASK [docker : add GPG key] ********************************************************************************************************************
ok: [host_01]

TASK [docker : add docker repository to apt] ***************************************************************************************************
ok: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
ok: [host_01] => (item=docker-ce)
ok: [host_01] => (item=docker-ce-cli)
ok: [host_01] => (item=containerd.io)

TASK [docker : adding ubuntu to docker group] **************************************************************************************************
ok: [host_01]

TASK [docker : install docker compose] *********************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-compose.yml for host_01

TASK [docker : Install docker-compose] *********************************************************************************************************
ok: [host_01]

TASK [docker : Change file ownership, group and permissions] ***********************************************************************************
ok: [host_01]

PLAY RECAP *************************************************************************************************************************************
host_01                    : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Check if everything accomplished:

```pwsh
> ssh -i .\id_ed255 ubuntu@158.160.88.93
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Feb 16 06:57:28 PM UTC 2025

  System load:  0.01               Processes:             138
  Usage of /:   18.1% of 19.59GB   Users logged in:       0
  Memory usage: 13%                IPv4 address for eth0: 192.168.10.11
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

16 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Sun Feb 16 18:54:19 2025 from 176.15.222.92
ubuntu@epd6j4q4rtdfqj3do4fu:~$ docker --version
Docker version 27.5.1, build 9f9e405
ubuntu@epd6j4q4rtdfqj3do4fu:~$ docker-compose -v
Docker Compose version v2.33.0
ubuntu@epd6j4q4rtdfqj3do4fu:~$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Sun 2025-02-16 12:34:33 UTC; 6h ago
       Docs: https://docs.docker.com
   Main PID: 4595 (dockerd)
      Tasks: 9
     Memory: 19.9M (peak: 21.0M)
        CPU: 3.143s
     CGroup: /system.slice/docker.service
             └─4595 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.318041035Z" level=info msg="OTEL tracing is not configured, using no-op tracer >
Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.318243939Z" level=info msg="detected 127.0.0.53 nameserver, assuming systemd-re>
Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.440700516Z" level=info msg="[graphdriver] using prior storage driver: overlay2"
Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.441132699Z" level=info msg="Loading containers: start."
Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.849433734Z" level=info msg="Default bridge (docker0) is assigned with an IP add>
Feb 16 12:34:32 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:32.991857409Z" level=info msg="Loading containers: done."
Feb 16 12:34:33 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:33.018919617Z" level=info msg="Docker daemon" commit=4c9b3b0 containerd-snapshotte>
Feb 16 12:34:33 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:33.019057629Z" level=info msg="Daemon has completed initialization"
Feb 16 12:34:33 epd6j4q4rtdfqj3do4fu dockerd[4595]: time="2025-02-16T12:34:33.057155268Z" level=info msg="API listen on /run/docker.sock"
Feb 16 12:34:33 epd6j4q4rtdfqj3do4fu systemd[1]: Started docker.service - Docker Application Container Engine.
ubuntu@epd6j4q4rtdfqj3do4fu:~$ groups
ubuntu adm dip video plugdev lxd docker google-sudoers
```

```bash
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [all] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-docker.yml for host_01

TASK [docker : install dependencies] ***********************************************************************************************************
ok: [host_01] => (item=apt-transport-https)
ok: [host_01] => (item=ca-certificates)
ok: [host_01] => (item=curl)
ok: [host_01] => (item=gnupg-agent)
ok: [host_01] => (item=software-properties-common)

TASK [docker : add GPG key] ********************************************************************************************************************
ok: [host_01]

TASK [docker : add docker repository to apt] ***************************************************************************************************
ok: [host_01]

TASK [docker : install docker] *****************************************************************************************************************
ok: [host_01] => (item=docker-ce)
ok: [host_01] => (item=docker-ce-cli)
ok: [host_01] => (item=containerd.io)

TASK [docker : adding ubuntu to docker group] **************************************************************************************************
ok: [host_01]

TASK [docker : install docker compose] *********************************************************************************************************
included: /mnt/c/users/muhammad/devops-fork/ansible/roles/docker/tasks/install-compose.yml for host_01

TASK [docker : Install docker-compose] *********************************************************************************************************
ok: [host_01]

TASK [docker : Change file ownership, group and permissions] ***********************************************************************************
ok: [host_01]

PLAY RECAP *************************************************************************************************************************************
host_01                    : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```bash
$ ansible-inventory -i inventory/default_yc.yml --list
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_connection": "ssh",
                "ansible_host": "158.160.88.93",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/ssh_keys/id_ed255",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```

```bash
$ ansible-inventory -i inventory/default_yc.yml --graph
@all:
  |--@ungrouped:
  |--@myhosts:
  |  |--host_01
```

## Acknowledgements

Credits to: [habr-article](https://habr.com/ru/companies/otus/articles/721166/) for helping with setup of custom docker