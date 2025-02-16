# Ansible playbook

I have created Ansible playbook that deploys Docker.
During its development, I employed the following practices:

- Kept the things as simple as possible
- Kept playbooks, roles, and other Ansible-related stuff in `git`
- Avoided configuration-dependent content as possible
- Generously used whitespaces
- All tasks, plays, and blocks are named
- States are always mentioned (even when they are optional)
- The comments used where the additional explanation is required
- Fully qualified collection names (FQCN) are used
- Root access for Docker is disabled in the `docker` role implementation during one of the tasks

## Task 1

To simplify the process of testing of this task, I passed the flag `--ask-become-pass`, which asked the password for the user of local machine where I tested the execution of playbook.

The output is the following:

```bash
> ANSIBLE_CONFIG=/mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/ansible.cfg ansible-playbook playbooks/dev/main.yaml --ask-become-pass
BECOME password:

PLAY [Deploy Docker] *************************************************************************************************************************************************
TASK [Gathering Facts] ***********************************************************************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Load OS-specific vars.] *******************************************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************************included: /home/dan/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for localhost

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *******************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *********************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ****************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *****************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *******************************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ********************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Add Docker apt key.] **********************************************************************************************************************changed: [localhost]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***********************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Add Docker repository.] *******************************************************************************************************************changed: [localhost]

TASK [geerlingguy.docker : Install Docker packages.] *****************************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *****************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Install docker-compose plugin.] ***********************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***********************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ****************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Configure Docker daemon options.] *********************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ********************************************************************************************ok: [localhost]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ****************************************************************************
TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Get docker group info using getent.] ******************************************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *********************************************************************************skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************************skipping: [localhost]

PLAY RECAP ***********************************************************************************************************************************************************localhost                  : ok=14   changed=2    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```

## Task 2

To simplify the process of testing of this task, I passed the flag `--ask-become-pass`, which asked the password for the user of local machine where I tested the execution of playbook.

The output is the following:

```bash
> ANSIBLE_CONFIG=/mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/ansible.cfg ansible-playbook playbooks/dev/main.yaml --ask-become-pass
BECOME password:

PLAY [Deploy Docker] *************************************************************************************************************************************************
TASK [Gathering Facts] ***********************************************************************************************************************************************ok: [localhost]

TASK [docker : Install Docker] ***************************************************************************************************************************************included: /mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/roles/docker/tasks/install-docker.yml for localhost

TASK [docker : Delete conflicting packages] **************************************************************************************************************************ok: [localhost] => (item=docker.io)
ok: [localhost] => (item=docker.doc)
ok: [localhost] => (item=docker-compose)
ok: [localhost] => (item=docker-compose-v2)
ok: [localhost] => (item=podman-docker)
ok: [localhost] => (item=containerd)
ok: [localhost] => (item=runc)

TASK [docker : Install Docker dependencies] **************************************************************************************************************************ok: [localhost] => (item=ca-certificates)
ok: [localhost] => (item=curl)

TASK [docker : Add Docker's official GPG key] ************************************************************************************************************************changed: [localhost]

TASK [docker : Add the repository to Apt sources] ********************************************************************************************************************changed: [localhost]

TASK [docker : Install Docker] ***************************************************************************************************************************************ok: [localhost] => (item=docker-ce)
ok: [localhost] => (item=docker-ce-cli)
ok: [localhost] => (item=containerd.io)
ok: [localhost] => (item=docker-buildx-plugin)

TASK [docker : Configure Docker to start on boot] ********************************************************************************************************************ok: [localhost]

TASK [docker : Configure containerd to start on boot] ****************************************************************************************************************ok: [localhost]

TASK [docker : Create "docker" group] ********************************************************************************************************************************ok: [localhost]

TASK [docker : Add user to the "docker" group] ***********************************************************************************************************************ok: [localhost]

TASK [docker : Install Docker Compose] *******************************************************************************************************************************included: /mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/roles/docker/tasks/install-compose.yml for localhost

TASK [docker : Install Docker Compose] *******************************************************************************************************************************ok: [localhost]

PLAY RECAP ***********************************************************************************************************************************************************localhost                  : ok=13   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Bonus Task: Dynamic Inventory

In this task, the private SSH key path was specified in ansible.cfg.

The output is the following:

```bash
> ANSIBLE_CONFIG=/mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/ansible.cfg ansible-playbook playbooks/dev/main.yaml

PLAY [Deploy Docker] *************************************************************************************************************************************************
TASK [Gathering Facts] ***********************************************************************************************************************************************[WARNING]: Platform linux on host terraform1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform1]

TASK [docker : Install Docker] ***************************************************************************************************************************************included: /mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/roles/docker/tasks/install-docker.yml for terraform1

TASK [docker : Delete conflicting packages] **************************************************************************************************************************ok: [terraform1] => (item=docker.io)
ok: [terraform1] => (item=docker.doc)
ok: [terraform1] => (item=docker-compose)
ok: [terraform1] => (item=docker-compose-v2)
ok: [terraform1] => (item=podman-docker)
ok: [terraform1] => (item=containerd)
ok: [terraform1] => (item=runc)

TASK [docker : Install Docker dependencies] **************************************************************************************************************************ok: [terraform1] => (item=ca-certificates)
ok: [terraform1] => (item=curl)

TASK [docker : Add Docker's official GPG key] ************************************************************************************************************************ok: [terraform1]

TASK [docker : Add the repository to Apt sources] ********************************************************************************************************************ok: [terraform1]

TASK [docker : Install Docker] ***************************************************************************************************************************************ok: [terraform1] => (item=docker-ce)
ok: [terraform1] => (item=docker-ce-cli)
ok: [terraform1] => (item=containerd.io)
ok: [terraform1] => (item=docker-buildx-plugin)

TASK [docker : Configure Docker to start on boot] ********************************************************************************************************************ok: [terraform1]

TASK [docker : Configure containerd to start on boot] ****************************************************************************************************************ok: [terraform1]

TASK [docker : Create "docker" group] ********************************************************************************************************************************ok: [terraform1]

TASK [docker : Add user to the "docker" group] ***********************************************************************************************************************ok: [terraform1]

TASK [docker : Secure Docker Configuration] **************************************************************************************************************************included: /mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/roles/docker/tasks/secure-docker-configuration.yml for terraform1

TASK [docker : Disable root access] **********************************************************************************************************************************changed: [terraform1]

TASK [docker : Install Docker Compose] *******************************************************************************************************************************included: /mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/roles/docker/tasks/install-compose.yml for terraform1

TASK [docker : Install Docker Compose] *******************************************************************************************************************************ok: [terraform1]

RUNNING HANDLER [docker : Restart Docker] ****************************************************************************************************************************changed: [terraform1]

PLAY RECAP ***********************************************************************************************************************************************************terraform1                 : ok=16   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739711978.396702   46236 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

### Inventory documentation

#### List

The output is the following:

```bash
> ANSIBLE_CONFIG=/mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/ansible.cfg ansible-inventory -i inventory/yacloud_compute.yml --list

{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "89.169.158.0"
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
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739712218.287918   47051 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

#### Graph

The output is the following:

```bash
> ANSIBLE_CONFIG=/mnt/d/dev/inno_dev/new/S25-core-course-labs/ansible/ansible.cfg ansible-inventory -i inventory/yacloud_compute.yml --graph

@all:
  |--@ungrouped:
  |--@yacloud:
  |  |--terraform1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739712303.112037   47109 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```
