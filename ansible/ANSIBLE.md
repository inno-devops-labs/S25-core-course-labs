# Ansible

## Best practices
- Use `ansible-lint` to enforce coding standards and detect potential issues.
- Mostly use the `ansible.builtin` namespace for better compatibility.
- Always specify the state parameter explicitly to avoid unintended behavior.
- Always provide name attributes for all tasks.
- Use `fact caching` (configured in ansible.cfg) to improve performance.

## Local Ansible usage

- To run ansible fully autonomly, I used Docker container with ssh-server.
You can find `Dockerfile` and `docker-compose.yml` at `ansible/misc`.
This setup requires running with root priveledged to install Docker-inside-Docker.

To run container use

```bash
sudo docker-compose up --build -d
```

## Task 1: Initial setup + deploy docker with `geerlingguy.docker` role

- Install role using `ansible-galaxy`

```bash
ansible-galaxy install geerlingguy.docker
```

- Create playbook: see `playbooks/dev/geerlingguy_docker.yaml`

- Check playbook syntax

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/geerlingguy_docker.yaml --syntax-check

playbook: playbooks/dev/geerlingguy_docker.yaml
```

- Run a playbook

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/geerlingguy_docker.yaml

PLAY [Install Docker using Ansible role] ****************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************************************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for test_host

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ******************************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ********************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ***************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****************************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] *******************************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **********************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ***************************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=15   changed=6    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   

```

## Task 2: Custom Docker Role

### Deployment output

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/main.yaml --syntax-check

playbook: playbooks/dev/main.yaml
```

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/main.yaml --diff

PLAY [all] **********************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [test_host]

TASK [docker : Include tasks to install Docker] *********************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for test_host

TASK [docker : Update apt package index] ****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Install required system packages] ********************************************************************************************************************************
ok: [test_host] => (item=apt-transport-https)
ok: [test_host] => (item=ca-certificates)
ok: [test_host] => (item=curl)
ok: [test_host] => (item=gnupg-agent)
ok: [test_host] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***********************************************************************************************************************************
ok: [test_host]

TASK [docker : Add Docker's official apt repository] ****************************************************************************************************************************
ok: [test_host]

TASK [docker : Install Docker and dependencies] *********************************************************************************************************************************
ok: [test_host] => (item=docker-ce)
ok: [test_host] => (item=docker-ce-cli)
ok: [test_host] => (item=containerd.io)

TASK [docker : Include tasks to install Docker Compose] *************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for test_host

TASK [docker : Download Docker Compose] *****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Include tasks to configure Docker] *******************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/configure_docker.yml for test_host

TASK [docker : Add user to docker group] ****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Configure Docker daemon security] ********************************************************************************************************************************
ok: [test_host]

TASK [docker : Detect init system] **********************************************************************************************************************************************
ok: [test_host]

TASK [docker : Enable Docker service (Systemd only)] ****************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Systemd only)] ***********************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Service)] ****************************************************************************************************************************************
changed: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=14   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```

### Inventory details

- `ansible-inventory -i inventory/local.yml --list`

```bash
~ ansible-inventory -i inventory/local.yml --list | tail -n 50
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 0,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "guest"
                },
                "ansible_virtualization_tech_guest": [
                    {
                        "__ansible_unsafe": "container"
                    },
                    {
                        "__ansible_unsafe": "docker"
                    }
                ],
                "ansible_virtualization_tech_host": [
                    {
                        "__ansible_unsafe": "kvm"
                    }
                ],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "docker"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
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
            "test_host"
        ]
    }
}
```

- `ansible-inventory -i inventory/local.yml --graph`

```bash
~ ansible-inventory -i inventory/local.yml --graph 
@all:
  |--@ungrouped:
  |  |--test_host
```

## Bonus task

### Dynamic inventory

Not possible for me without cloud service.  `(ㆆ _ ㆆ)`

### Secure Docker Configuration

I configured `daemon.json` in `tasks/configure_docker.yml`:

```json
{
    "no-new-privileges": true,
    "userns-remap": "default",
    "restart": "always",
}
```

This ensures that Docker containers run without root privileges.
