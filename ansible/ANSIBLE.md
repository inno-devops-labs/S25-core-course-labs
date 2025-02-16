# Ansible
## playbook output:
```bash
$ansible-playbook playbooks/dev/main.yaml --diff

PLAY [setup docker] ***************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************
[WARNING]: Platform linux on host 52.91.173.229 is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [52.91.173.229]

TASK [docker : include_tasks] *****************************************************************************************************
included: /home/anas/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/setup-Debian.yml for 52.91.173.229

TASK [docker : Ensure old versions of Docker are not installed.] ******************************************************************
ok: [52.91.173.229]

TASK [docker : Ensure dependencies are installed.] ********************************************************************************
ok: [52.91.173.229]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***************************
skipping: [52.91.173.229]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ************************************************
ok: [52.91.173.229]

TASK [docker : Add Docker apt key.] ***********************************************************************************************
ok: [52.91.173.229]

TASK [docker : Ensure curl is present (on older systems without SNI).] ************************************************************
skipping: [52.91.173.229]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************
skipping: [52.91.173.229]

TASK [docker : Add Docker repository.] ********************************************************************************************
ok: [52.91.173.229]

TASK [docker : include_tasks] *****************************************************************************************************
included: /home/anas/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 52.91.173.229

TASK [docker : Install Docker packages.] ******************************************************************************************
skipping: [52.91.173.229]

TASK [docker : Ensure /etc/docker/ directory exists.] *****************************************************************************
skipping: [52.91.173.229]

TASK [docker : Configure Docker daemon options.] **********************************************************************************
skipping: [52.91.173.229]

TASK [docker : Ensure Docker is started and enabled at boot.] *********************************************************************
ok: [52.91.173.229]

TASK [docker : include_tasks] *****************************************************************************************************
included: /home/anas/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 52.91.173.229

TASK [docker : Check current docker-compose version.] *****************************************************************************
ok: [52.91.173.229]

TASK [docker : set_fact] **********************************************************************************************************
ok: [52.91.173.229]

TASK [docker : Delete existing docker-compose version if it's different.] *********************************************************
skipping: [52.91.173.229]

TASK [docker : Install Docker Compose (if configured).] ***************************************************************************
skipping: [52.91.173.229]

TASK [docker : Install docker-compose plugin.] ************************************************************************************
skipping: [52.91.173.229]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ************************************************************
ok: [52.91.173.229]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************

TASK [docker : Get docker group info using getent.] *******************************************************************************
skipping: [52.91.173.229]

TASK [docker : Check if there are any users to add to the docker group.] **********************************************************
skipping: [52.91.173.229]

TASK [docker : include_tasks] *****************************************************************************************************
skipping: [52.91.173.229]

PLAY RECAP ************************************************************************************************************************
52.91.173.229              : ok=13   changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   


```
## Inventory Documentation:
```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "52.91.173.229": {
                "ansible_ssh_private_key_file": "~/.ssh/lasttry.pem",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "ec2"
        ]
    },
    "ec2": {
        "hosts": [
            "52.91.173.229"
        ]
    }
}

```

```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |--@ec2:
  |  |--52.91.173.229
```