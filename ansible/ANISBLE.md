# ANSIBLE.md

## Lab 5 Task 1 & Task 2

This lab focuses on using **Ansible** to install **Docker** and **Docker Compose** on a cloud VM. The playbook is structured to ensure Docker starts on boot and adds the current user to the Docker group. Below, you’ll find the execution logs, inventory details, and validation outputs.

---

## **1. Ansible Playbook Execution Output**

Below is the **last 50 lines** of the `ansible-playbook` execution:

```
PLAY [Deploy Docker using Ansible] ********************************************************************

TASK [Gathering Facts] ********************************************************************************
[WARNING]: Platform linux on host dev_vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
ok: [dev_vm]

TASK [docker : Docker installation] *******************************************************************
included: /home/user/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for dev_vm

TASK [docker : Install prerequisite packages] *********************************************************
ok: [dev_vm] => (item=apt-transport-https)
ok: [dev_vm] => (item=ca-certificates)
ok: [dev_vm] => (item=curl)
ok: [dev_vm] => (item=gnupg-agent)
ok: [dev_vm] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] ********************************************************************
ok: [dev_vm]

TASK [docker : Add Docker repository] *****************************************************************
ok: [dev_vm]

TASK [docker : Install Docker] ************************************************************************
ok: [dev_vm]

TASK [docker : Enable Docker service] *****************************************************************
ok: [dev_vm]

TASK [docker : Add user to Docker group] **************************************************************
ok: [dev_vm]

TASK [docker : Docker Compose installation] ***********************************************************
included: /home/user/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for dev_vm

TASK [docker : Download Docker Compose] ***************************************************************
ok: [dev_vm]

TASK [docker : Verify Docker Compose installation] ****************************************************
changed: [dev_vm]

TASK [docker : Display success message if Docker Compose is installed] ********************************
ok: [dev_vm] => {
    "msg": "docker-compose installed"
}

PLAY RECAP *******************************************************************************************
dev_vm                  : ok=14   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

---

## **2. Dry-Run Verification (`-diff --check`)**

Before applying changes, we performed a dry-run with:

```
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff --check
```

The output confirms that changes were correctly planned without execution.

---

## **3. Inventory Details (`-list`)**

To validate the Ansible inventory structure, we ran:

```
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

The output:

```
{
    "_meta": {
        "hostvars": {
            "dev_vm": {
                "ansible_host": "192.168.1.100",
                "ansible_user": "ubuntu"
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
            "dev_vm"
        ]
    }
}
```

---

## **4. Inventory Graph (`-graph`)**

To visualize the inventory structure, we ran:

```
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Output:

```
@all:
  |--@ungrouped:
  |  |--dev_vm
```

## Lab 6

billy@Mohammads-MacBook-Air ansible % ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml

PLAY [Deploy Docker and Web App] ****************************************************\*\*\*****************************************************

TASK [Gathering Facts] **********************************************************\***********************************************************
[WARNING]: Platform linux on host my-cloud-vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html
ok: [my-cloud-vm]

TASK [docker : Include Docker installation tasks] ********************************************\*\*\*********************************************
included: /Users/billy/Documents/Code/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my-cloud-vm

TASK [docker : Installing required system packages] ******************************************\*\*\*******************************************
changed: [my-cloud-vm]

TASK [docker : Add Docker GPG apt Key] ************************************************\*\*\*\*************************************************
ok: [my-cloud-vm]

TASK [docker : Get Ubuntu release version] **********************************************\*\*\*\***********************************************
ok: [my-cloud-vm]

TASK [docker : Add Docker Repository] **************************************************\***************************************************
ok: [my-cloud-vm]

TASK [docker : Install Docker] ****************************************************\*\*\*\*****************************************************
changed: [my-cloud-vm]

TASK [docker : Ensure Docker service is running] ********************************************\*\*********************************************
ok: [my-cloud-vm]

TASK [docker : Ensure current user is added to docker group] **************************************\***************************************
ok: [my-cloud-vm]

TASK [docker : Include Docker Compose installation tasks] ****************************************\*****************************************
included: /Users/billy/Documents/Code/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for my-cloud-vm

TASK [docker : Install Docker Compose] ************************************************\*\*\*\*************************************************
ok: [my-cloud-vm]

TASK [web_app : Ensure the application directory exists] ****************************************\*****************************************
changed: [my-cloud-vm]

TASK [web_app : Generate docker-compose configuration] ****************************************\*\*\*****************************************
changed: [my-cloud-vm]

TASK [web_app : Fetch latest Docker image] **********************************************\*\*\***********************************************
changed: [my-cloud-vm]

TASK [web_app : Run the Python web app container] ******************************************\*\*\*******************************************
changed: [my-cloud-vm]

TASK [web_app : Print Docker version] ************************************************\*\*\*\*************************************************
ok: [my-cloud-vm] => {
"msg": "Docker version 27.5.1, build 9f9e405"
}

TASK [web_app : Print Docker Compose version] ********************************************\*\*\*\*********************************************
ok: [my-cloud-vm] => {
"msg": "docker-compose version 1.29.2, build 5becea4c"
}

TASK [web_app : Restart Docker container] **********************************************\*\*\*\***********************************************
changed: [my-cloud-vm]

PLAY RECAP **************************************************************\*\*\***************************************************************
my-cloud-vm : ok=18 changed=7 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
