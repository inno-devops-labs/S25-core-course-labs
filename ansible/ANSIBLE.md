# Ansible

## Installation and Introduction

```bash
> brew install ansible
> ansible --version

ansible [core 2.18.2]
  config file = None
  configured module search path = ['/Users/m.sirozhova/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /opt/homebrew/Cellar/ansible/11.2.0/libexec/lib/python3.13/site-packages/ansible
  ansible collection location = /Users/m.sirozhova/.ansible/collections:/usr/share/ansible/collections
  executable location = /opt/homebrew/bin/ansible
  python version = 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] (/opt/homebrew/Cellar/ansible/11.2.0/libexec/bin/python)
  jinja version = 3.1.5
  libyaml = True
```

## Use an Existing Ansible Role for Docker

```bash
> ansible-galaxy role install geerlingguy.docker                  

Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /Users/m.sirozhova/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

## Create a Playbook and Testing

```bash
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Install Docker] **********************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
included: /Users/m.sirozhova/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for cloud_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *****************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *******************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] **************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************************************************************************************************************
changed: [cloud_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ******************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************************************************************************************************************
changed: [cloud_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *********************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Add Docker repository.] *****************************************************************************************************************************
changed: [cloud_vm]

TASK [geerlingguy.docker : Install Docker packages.] ***************************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***************************************************************************************************
changed: [cloud_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *********************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******************************************************************************************************
ok: [cloud_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] **************************************************************************************************************************
changed: [cloud_vm]

TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************************************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *******************************************************************************************
skipping: [cloud_vm]

TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
skipping: [cloud_vm]

PLAY RECAP *********************************************************************************************************************************************************************
cloud_vm                   : ok=15   changed=5    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

Then I tested it:

```bash
> ssh ubuntu@84.201.158.253                                                                
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Feb  9 05:49:16 PM UTC 2025

  System load:  0.0                Processes:             141
  Usage of /:   18.2% of 19.59GB   Users logged in:       0
  Memory usage: 14%                IPv4 address for eth0: 192.168.0.12
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

10 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


*** System restart required ***
Last login: Sun Feb  9 17:34:50 2025 from 188.130.155.177

> ubuntu@fhm8l97e5pdu2rs2pmlu:~$ docker --version
Docker version 27.5.1, build 9f9e405

```