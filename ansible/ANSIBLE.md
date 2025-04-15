# Ansible

## Best Practices for Using Ansible Effectively

To ensure maintainability, scalability, and security when working with Ansible, follow these best practices:

* **Use Version Control:** Store your playbooks and inventory files in a version control system like Git. This helps track changes, collaborate efficiently, and roll back if needed.
* **Follow a Clear Directory Structure:** Organize your Ansible project by separating roles, inventories, and group variables. A well-structured directory makes troubleshooting easier and improves reusability.
* **Leverage Dynamic Inventory:** When working with cloud providers like AWS, use dynamic inventory scripts or plugins to fetch server details dynamically.
* **Document Everything:** Add comments to playbooks, roles, and variables, and maintain README files to help others (and your future self) understand your configurations.

---

## Deploying Docker on a Web Server Using Ansible

Here you will find steps to set up a web server with Docker using Ansible. The deployment involves setting up SSH access, configuring the Ansible user, verifying the connection, and installing Docker using Ansible playbooks.

### Step 1: Configure SSH Access

Before running Ansible commands, ensure SSH access to the server is properly configured.

#### Generate SSH Keys on the Host Machine

```shell
ssh-keygen -t ed25519
```

#### Configure SSH Access for the Ansible User

Connect to the remote server and set up an Ansible user with SSH access:

```shell
sudo useradd -m -d /home/ansible-user -s /bin/bash ansible-user
sudo su - ansible-user
mkdir .ssh
touch .ssh/authorized_keys
echo "public_key" > /home/ansible-user/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

#### Set a Password for the Ansible User

```shell
sudo passwd ansible-user
```

#### Grant Sudo Privileges to the Ansible User

```shell
sudo usermod -aG sudo ansible-user
```

---

### Step 2: Verify Ansible Connection

Once the SSH setup is complete, test the Ansible connection to ensure the server is reachable:

```shell
ansible web_server -m ping -i inventory/default_aws_ec2.yml
```

Expected output:

```json
web_server | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

If the connection test is successful, proceed to the next step.

---

### Step 3: Install Docker Using Ansible

Docker installation is automated using an Ansible playbook. The following command runs the playbook to set up Docker on the server:

```shell
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -K
```

When prompted, enter the `BECOME` password for privilege escalation.

Sample output of a successful run:

```shell
PLAY [Deploy Docker] **************************************************************************************************************************************************
TASK [Gathering Facts] ************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] *******************************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/pip.yml for web_server

TASK [../../roles/docker : Update apt] ********************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install python] ****************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] *******************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install docker] ****************************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [../../roles/docker : Install docker via pip] ********************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install docker-compose] ********************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [../../roles/docker : Install docker-compose via pip] ************************************************************************************************************
ok: [web_server]

PLAY RECAP ************************************************************************************************************************************************************
web_server                 : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

---

### Step 4: Verify Inventory Configuration

To check that the inventory file correctly includes the web server, use the following command:

```shell
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Expected output:

```json
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "78.153.140.41",
                "ansible_user": "ansible-user"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "web_server"
        ]
    }
}
```

---

### Step 5: Deploy python-app

The playbook installs Docker and Docker Compose, preparing the environment for the app.

```shell
ansible-playbook -i ./inventory/default_aws_ec2.yml playbooks/dev/app_python/main.yaml -K
BECOME password: 

PLAY [python_app] *****************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *******************************************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/pip.yml for web_server

TASK [docker : Update apt] ********************************************************************************************************************************************
changed: [web_server]

TASK [docker : Install python] ****************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *******************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] ****************************************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [docker : Install docker via pip] ********************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker-compose] ********************************************************************************************************************************
included: /Users/maksalena/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [docker : Install docker-compose via pip] ************************************************************************************************************************
ok: [web_server]

PLAY RECAP ************************************************************************************************************************************************************
web_server                 : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
