# Ansible

## Installing the (prepared) docker role

Doing the role for docker is as simple as a single command (after installing ansible itself, that is):

```bash
❯ ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /home/ropero/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

Then, by creating `default_aws_ec2.yml` and then redirecting it to yandex config file (cause that's what we're using), we can develop as follows:

```bash
❯ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Load OS-specific vars.] *************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
included: /home/dmitriy/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for compute-vm-2-2-20-ssd-1739694545649

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] **********************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] **************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Add Docker repository.] *************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Install Docker packages.] ***********************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***********************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Install docker-compose plugin.] *****************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *****************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Get docker group info using getent.] ************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

TASK [geerlingguy.docker : include_tasks] **********************************************************************************************
skipping: [compute-vm-2-2-20-ssd-1739694545649]

PLAY RECAP *****************************************************************************************************************************
compute-vm-2-2-20-ssd-1739694545649                      : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

We can see the result of our hard labour by testing it through ssh (key is at `~/.ssh`, but I won't tell ya what's inside :) ) console:

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete
Digest: sha256:e0b569a5163a5e6be84e210a2587e7d447e08f87a0e90798363fa44a0464a1e8
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Custom role for Docker

For this part a few modifications to the playbook are necessary, after which we will get something like this:

```bash
❯ ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff

PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for compute-vm-2-2-20-ssd-1739694545649

TASK [docker : Install prerequisites] **************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 11 not upgraded.
changed: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : Add Docker GPG key] *****************************************************************************************************
changed: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : Add Docker repo] ********************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu noble stable

changed: [compute-vm-2-2-20-ssd-1739694545649]

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
0 upgraded, 10 newly installed, 0 to remove and 11 not upgraded.
changed: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for compute-vm-2-2-20-ssd-1739694545649

TASK [docker : Download Docker Compose] ************************************************************************************************
changed: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/configure_docker.yml for compute-vm-2-2-20-ssd-1739694545649

TASK [docker : Add user to Docker group] ***********************************************************************************************
changed: [compute-vm-2-2-20-ssd-1739694545649]

TASK [docker : Enable Docker service] **************************************************************************************************
ok: [compute-vm-2-2-20-ssd-1739694545649]

RUNNING HANDLER [docker : Docker Restart] **********************************************************************************************
changed: [compute-vm-2-2-20-ssd-1739694545649]

PLAY RECAP *****************************************************************************************************************************
compute-vm-2-2-20-ssd-1739694545649                      : ok=12   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

And, as expected from ssh testing, everything is working just fine, docker happily returning "hello world" container on request.

## Inventory

Here are some details of the inventory:

```bash
❯ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "compute-vm-2-2-20-ssd-1739694545649": {
                "ansible_host": "158.160.159.61",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "gendiro"
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
            "compute-vm-2-2-20-ssd-1739694545649"
        ]
    }
}
```

## Set up Dynamic Inventory

Now it's time to up the game and make the invetory dynamic:

```bash
❯ ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml --diff

PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
[WARNING]: Platform linux on host terraform1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install prerequisites] **************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker GPG key] *****************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker repo] ********************************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] *********************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Download Docker Compose] ************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/configure_docker.yml for terraform1

TASK [docker : Add user to Docker group] ***********************************************************************************************
ok: [terraform1]

TASK [docker : Enable Docker service] **************************************************************************************************
ok: [terraform1]

PLAY RECAP *****************************************************************************************************************************
terraform1                 : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739132182.744746   86091 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

Then the invenory will look like this:

```bash
❯ ansible-inventory -i inventory/yacloud_compute.yml --list
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.159.61"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "terraform1"
        ]
    }
}
```

## Secure Docker Configuration

Once again modyfiying the file, we get:

```bash
❯ ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml --diff

PLAY [Install and Configure Docker] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
[WARNING]: Platform linux on host terraform1 is using the discovered Python interpreter at /usr/bin/python3.12, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install prerequisites] **************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker GPG key] *****************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker repo] ********************************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] *********************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Download Docker Compose] ************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] **********************************************************************************************************
included: /mnt/f/magic/Documents/Projects/S25-core-course-labs/ansible/roles/docker/tasks/configure_docker.yml for terraform1

TASK [docker : Add user to Docker group] ***********************************************************************************************
ok: [terraform1]

TASK [docker : Disable root access] ****************************************************************************************************
--- before
+++ after: /etc/docker/daemon.json
@@ -0,0 +1,3 @@
+{
+  "userns-remap": "default"
+}

changed: [terraform1]

TASK [docker : Enable Docker service] **************************************************************************************************
ok: [terraform1]

RUNNING HANDLER [docker : Docker Restart] **********************************************************************************************
changed: [terraform1]

PLAY RECAP *****************************************************************************************************************************
terraform1                 : ok=13   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739134397.145184   95036 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```
