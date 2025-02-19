# Lab 5

## Task 1

1. I installed Ansible:

```bash
pipx install ansible-core
⚠️ Found a space in the pipx home path. We heavily discourage this,
    due to multiple incompatibilities. Please check our docs for more
    information on this, as well as some pointers on how to migrate
    to a different home path.
  installed package ansible-core 2.18.2, installed using Python 3.13.2
  These apps are now globally available
    - ansible
    - ansible-config
    - ansible-console
    - ansible-doc
    - ansible-galaxy
    - ansible-inventory
    - ansible-playbook
    - ansible-pull
    - ansible-test
    - ansible-vault
done! ✨ 🌟 ✨
```

2. I installed the role suggested in lab:

```bash
ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /Users/akss/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

3. I created and tested the playbook:
   ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

```bash
PLAY [Install Docker] ****************************\*\*****************************

TASK [Gathering Facts] ****************************\*****************************
ok: [my_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] **************\***************
ok: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************\*\*******************
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************\*\*******************
included: /Users/akss/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for my_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] **\***
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] \*\*\*
ok: [my_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] \*\*\*
ok: [my_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] \*\*\*
ok: [my_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********\*********
changed: [my_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **\*\***
ok: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key.] **************\*\*\*\***************
changed: [my_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] \*\*\*
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] \*\*\*
skipping: [my_vm]

TASK [geerlingguy.docker : Add Docker repository.] **************\***************
changed: [my_vm]

TASK [geerlingguy.docker : Install Docker packages.] ************\*\*\*************
skipping: [my_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] \*\*\*
changed: [my_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********\***********
skipping: [my_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] \*\*\*
ok: [my_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******\*\*******
skipping: [my_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********\*\*\*********
skipping: [my_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **\*\***
ok: [my_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] \*\*\*

RUNNING HANDLER [geerlingguy.docker : restart docker] ************\*\*************
changed: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************\*\*******************
skipping: [my_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ******\*\*\*\*******
skipping: [my_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] \*\*\*
skipping: [my_vm]

TASK [geerlingguy.docker : include_tasks] ******************\*\*******************
skipping: [my_vm]

PLAY RECAP **********************************\***********************************
my_vm : ok=15 changed=5 unreachable=0 failed=0 skipped=11 rescued=0 ignored=0
```

After completion of the previous command, I run:

```bash
ssh -l mangocandle 158.160.165.93
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-52-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Feb 16 07:53:21 PM UTC 2025

  System load:  0.34              Processes:             145
  Usage of /:   35.7% of 9.76GB   Users logged in:       0
  Memory usage: 13%               IPv4 address for eth0: 10.130.0.14
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


Last login: Sun Feb 16 19:52:09 2025 from 188.130.155.165
mangocandle@ubuntu:~$ docker --version
Docker version 27.5.1, build 9f9e405
```

# Lab 6

## Deployment Output:

```bash
ok: [my_vm]

TASK [docker : Adding GPG key] *************************************************
ok: [my_vm]

TASK [docker : Adding a Docker repository to APT] ******************************
ok: [my_vm]

TASK [docker : Installing Docker] **********************************************
ok: [my_vm]

TASK [docker : include_tasks] **************************************************
included: /Users/akss/Desktop/study/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for my_vm

TASK [docker : Downloading Docker Compose] *************************************
ok: [my_vm]

TASK [docker : include_tasks] **************************************************
included: /Users/akss/Desktop/study/S25-core-course-labs/ansible/roles/docker/tasks/start.yml for my_vm

TASK [docker : Add user to Docker group] ***************************************
ok: [my_vm]

TASK [docker : Disable root login] *********************************************
ok: [my_vm]

TASK [docker : Start the Docker service] ***************************************
ok: [my_vm]

TASK [web_app : App dir existence] *********************************************
skipping: [my_vm]

TASK [web_app : Docker compose existence] **************************************
skipping: [my_vm]

TASK [web_app : Remove docker compose] *****************************************
skipping: [my_vm]

TASK [web_app : Remove directory] **********************************************
skipping: [my_vm]

TASK [web_app : Create Web App directory] **************************************
ok: [my_vm]

TASK [web_app : Copy docker compose] *******************************************
ok: [my_vm]

PLAY RECAP *********************************************************************
my_vm                      : ok=14   changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
```

Checking if the deployment was successfull:

1. Connect to the VM:

```bash
ssh -l mangocandle 158.160.156.187
```

2. List all the running docker processes:

```bash
mangocandle@compute-vm-2-2-10-hdd-1739977927860:~$ docker ps
CONTAINER ID   IMAGE                    COMMAND           CREATED          STATUS          PORTS                                     NAMES
70f8c6e8402d   mangocandle/app_python   "python app.py"   43 minutes ago   Up 43 minutes   0.0.0.0:80->5000/tcp, [::]:80->5000/tcp   python_web_app
```

Removing the deployed image:

```bash
ansible-playbook -i inventory/default_yacloud_compute.yml -i inventory/default_aws_ec2.yml playbooks/dev/app_python/main.yml --tags wipe

PLAY [Deploy python web app] **********************************************************************

TASK [Gathering Facts] ****************************************************************************
ok: [my_vm]

PLAY RECAP ****************************************************************************************
my_vm                      : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
