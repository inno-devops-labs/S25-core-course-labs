ansible-playbook playbooks/dev/main.yaml --diff
```
PLAY [Install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [docker_vm]

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [docker_vm]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [docker_vm]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /etc/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for docker_vm

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *****
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ***
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ******
ok: [docker_vm]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [docker_vm]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [docker_vm]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
changed: [docker_vm]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [docker_vm]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [docker_vm]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [docker_vm]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [docker_vm]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [docker_vm]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [docker_vm]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [docker_vm]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [docker_vm]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [docker_vm]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [docker_vm]

PLAY RECAP *********************************************************************
docker_vm                  : ok=14   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list

```
{
    "_meta": {
        "hostvars": {
            "docker_vm": {
                "ansible_host": "192.168.0.104",
                "ansible_user": "dariashib"
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
            "docker_vm"
        ]
    }
}

```
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph

```
@all:
  |--@ungrouped:
  |--@myhosts:
  |  |--docker_vm

```
Deploy docker role:

```
PLAY [Install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [docker_vm]

TASK [docker : Install apt dependencies] ***************************************
ok: [docker_vm]

TASK [docker : Add Docker’s GPG key] *******************************************
ok: [docker_vm]

TASK [docker : Add Docker apt repository] **************************************
ok: [docker_vm]

TASK [docker : Install Docker] *************************************************
ok: [docker_vm]

TASK [docker : Install compose via apt] ****************************************
changed: [docker_vm]

TASK [docker : Add user to the Docker group] ***********************************
changed: [docker_vm]

PLAY RECAP *********************************************************************
docker_vm                  : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
