#Ansimble

## Best practices 

**clean directory structure**
**role based playbook:** calls roles rather than specifying tasks directly
**handlers:** used to restart Docker only when necessary

* Provide the last 50 lines of the output from your deployment command in the ANSIBLE.md file. 

```
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy Docker on Cloud VM] ***********************************************

TASK [Gathering Facts] *********************************************************
ok: [my_vm]

TASK [docker : Update apt cache] ***********************************************
changed: [my_vm]

TASK [docker : Install prerequisites] ******************************************
changed: [my_vm]

TASK [docker : Add Docker GPG key] *********************************************
changed: [my_vm]

TASK [docker : Add Docker repository] ******************************************
changed: [my_vm]

TASK [docker : Install Docker CE] **********************************************
ok: [my_vm]

TASK [docker : Download Docker Compose binary] *********************************
changed: [my_vm]

TASK [docker : Verify Docker Compose installation] *****************************
changed: [my_vm]

TASK [docker : Enable and start Docker service] ********************************
ok: [my_vm]

TASK [docker : Add current user to docker group] *******************************
changed: [my_vm]

PLAY RECAP *********************************************************************
my_vm                      : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```
* Execute the following command ansible-inventory -i <name_of_your_inventory_file>.yaml --list and provide its output in the ANSIBLE.md file.

```
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "my_vm": {
                "ansible_become": true,
                "ansible_become_method": "sudo",
                "ansible_host": "94.159.109.179",
                "ansible_ssh_pass": "{{ lookup('env', 'MY_VM_SSH_PASS') }}",
                "ansible_user": "root"
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
* Validate the inventory file using ansible-inventory -i <name_of_your_inventory_file>.yaml --graph to visualize the inventory structure.

```
meowal@meowal-1-2:~/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--my_vm
```

* Execute your playbook to deploy the role.
Provide the last 50 lines of the output from your deployment command in the ANSIBLE.md file.

```
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --check --diff

PLAY [Deploy Docker on Cloud VM] *********************************************************************

TASK [Gathering Facts] *******************************************************************************
ok: [my_vm]

TASK [docker : Update apt cache] *********************************************************************
changed: [my_vm]

TASK [docker : Install prerequisites] ****************************************************************
ok: [my_vm]

TASK [docker : Add Docker GPG key] *******************************************************************
ok: [my_vm]

TASK [docker : Add Docker repository] ****************************************************************
ok: [my_vm]

TASK [docker : Install Docker CE] ********************************************************************
ok: [my_vm]

TASK [docker : Download Docker Compose binary] *******************************************************
ok: [my_vm]

TASK [docker : Verify Docker Compose installation] ***************************************************
skipping: [my_vm]

TASK [docker : Enable and start Docker service] ******************************************************
ok: [my_vm]

TASK [docker : Add current user to docker group] *****************************************************
ok: [my_vm]

TASK [web_app : Ensure application directory exists] *************************************************
ok: [my_vm]

TASK [web_app : Pull Docker image for the web application] *******************************************
ok: [my_vm]

TASK [web_app : Render Docker Compose file for the application] **************************************
ok: [my_vm]

TASK [web_app : Bring up application container with Docker Compose] **********************************
skipping: [my_vm]

PLAY RECAP *******************************************************************************************
my_vm                      : ok=12   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```
