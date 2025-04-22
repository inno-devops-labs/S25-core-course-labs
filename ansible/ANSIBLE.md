# Ansible Deployment Documentation

## Playbook Execution Output

Executed the following command:

 ```bash
 ansible-playbook -i ./inventory/my_inventory.yml ./playbooks/deploy_docker.yml --check --diff
 ```

### Output

 ```bash
 PLAY [Deploy Docker] ************************************************************************************************

 TASK [Gathering Facts] **********************************************************************************************
 ok: [130.193.40.214]

 TASK [docker : Install dependencies] *******************************************************************************
 ok: [130.193.40.214]

 TASK [docker : Add Docker GPG key] **********************************************************************************
 changed: [130.193.40.214]

 TASK [docker : Add Docker repository] *******************************************************************************
 changed: [130.193.40.214]

 TASK [docker : Install Docker] **************************************************************************************
 The following additional packages will be installed:
   docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
 The following packages will be upgraded:
   docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras
 4 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
 changed: [130.193.40.214]

 TASK [docker : Install Docker Compose] ******************************************************************************
 ok: [130.193.40.214]

 TASK [docker : Enable Docker service on boot] ***********************************************************************
 ok: [130.193.40.214]

 TASK [docker : Add user to Docker group] ****************************************************************************
 changed: [130.193.40.214]

 PLAY RECAP **********************************************************************************************************
 130.193.40.214            : ok=8    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
 ```

## Inventory Details

Executed the following command:

 ```bash
 ansible-inventory -i ./inventory/my_inventory.yml --list
 ```

### Inventory Output

 ```json
 {
  "_meta": {
    "hostvars": {
      "130.193.40.214": {
        "ansible_host": "130.193.40.214",
        "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
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
      "130.193.40.214"
    ]
  }
}
 ```

## Inventory Graph Structure

Executed the following command:

 ```bash
 ansible-inventory -i ./inventory/my_inventory.yml --graph
 ```

### Graph Output

 ```bash
 @all:
   |--@ungrouped:
   |  |--130.193.40.214
 ```

## Lab6: Application Deployment

 ```bash
 ansible-playbook -i ./inventory/default_aws_ec2.yml ./playbooks/dev/main.yml 
 ```

 ```bash
 PLAY [Deploy application with Docker container] *************************************************************************************

 TASK [Gathering Facts] *************************************************************************************************************
 [WARNING]: Platform linux on host my_server is using the discovered Python interpreter at /usr/bin/python3, but future
 installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
 core/2.18/reference_appendices/interpreter_discovery.html for more information.
 ok: [my_server]

 TASK [docker : Install dependencies] ************************************************************************************************
 ok: [my_server]

 TASK [docker : Add Docker GPG key] **************************************************************************************************
 ok: [my_server]

 TASK [docker : Add Docker repository] ***********************************************************************************************
 ok: [my_server]

 TASK [docker : Install Docker] ******************************************************************************************************
 ok: [my_server]

 TASK [docker : Install Docker Compose] **********************************************************************************************
 ok: [my_server]

 TASK [docker : Enable Docker service on boot] ***************************************************************************************
 ok: [my_server]

 TASK [docker : Add user to Docker group] ********************************************************************************************
 ok: [my_server]

 TASK [web_app : Pull Docker image for web_app] **************************************************************************************
 ok: [my_server]

 TASK [web_app : Generate docker-compose.yml from template] ***************************************************************************
 changed: [my_server]

 TASK [web_app : Start web_app container with Docker Compose] ************************************************************************
 changed: [my_server]

 PLAY RECAP **************************************************************************************************************************
 my_server               : ok=10   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
 ```
