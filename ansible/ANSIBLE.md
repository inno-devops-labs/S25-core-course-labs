# Ansible and Docker Deployment

## Using Ansible Galaxy for Docker Role

i use the `geerlingguy.docker` role from Ansible Galaxy to simplify Docker installation.

Install the role:

```sh
ansible-galaxy install geerlingguy.docker
```



## Playbook for Docker Deployment

The playbook for deploying Docker is defined as follows:

```yaml
- name: Ansible and Docker Deployment
  hosts: all  
  become: true 
  roles:
    - geerlingguy.docker 
```

### Inventory File (`inventory/default_aws_ec2.yml`)

```yaml
ec2:
  vars:
    ansible_user: ubuntu
    ansible_ssh_private_key_file: /home/saleem/Downloads/lab5_key.pem
  hosts:
    ec2-18-234-235-90.compute-1.amazonaws.com
```

---

## Running the Playbook

To execute the playbook, run:

```sh
ansible-playbook -i ~/Documents/DevOps/S25-core-course-labs/ansible/inventory/default_aws_ec2.yml ~/Documents/DevOps/S25-core-course-labs/ansible/playbooks/dev/main.yaml
```

### Execution Output

<details>
<summary>output</summary>

```cmd
(devops) devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/ansible$ ansible-playbook -i ~/Documents/DevOps/S25-core-course-labs/ansible/inventory/default_aws_ec2.yml ~/Documents/DevOps/S25-core-course-labs/ansible/playbooks/dev/main.yaml

PLAY [Ansible and Docker Deployment] *****************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
[WARNING]: Platform linux on host ec2-18-234-235-90.compute-1.amazonaws.com is using the discovered Python interpreter at /usr/bin/python3.10, but
future installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Load OS-specific vars.] ***************************************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************
included: /home/saleem/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ec2-18-234-235-90.compute-1.amazonaws.com

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ***************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *****************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***************************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ****************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key.] ******************************************************************************************************
changed: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *******************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **********************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Add Docker repository.] ***************************************************************************************************
changed: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages.] *************************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *************************************************************************
changed: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose plugin.] *******************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *******************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Configure Docker daemon options.] *****************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ****************************************************************************
ok: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ************************************************************************************************
changed: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Get docker group info using getent.] **************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *****************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************
skipping: [ec2-18-234-235-90.compute-1.amazonaws.com]

PLAY RECAP *******************************************************************************************************************************************
ec2-18-234-235-90.compute-1.amazonaws.com : ok=15   changed=4    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   


```
</details>

### Result Verification

To confirm Docker installation, connect to the AWS server and check the Docker version:

```sh
docker --version
```

Output:
<details>
<summary>output</summary>

```cmd

ubuntu@ip-172-31-29-58:~$ docker -v
Docker version 27.5.1, build 9f9e405
ubuntu@ip-172-31-29-58:~$ 

```
</details>


## Deployment Output

<details>
<summary>output</summary>

```cmd

(devops) devopssaleem@saleem-MCLF-XX:~/Documents/DevOps/S25-core-course-labs/ansible$ ansible-playbook  playbooks/dev/main.yaml

PLAY [Ansible and Docker Deployment] ***********************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [aws_instance]

TASK [docker : Ensure apt key is not present in trusted.gpg.d] *********************************************************************************
ok: [aws_instance]

TASK [docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***********************************************************
ok: [aws_instance]

TASK [docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ******************************************************
ok: [aws_instance]

TASK [docker : Ensure old versions of Docker are not installed] ********************************************************************************
ok: [aws_instance]

TASK [docker : Ensure dependencies are installed] **********************************************************************************************
ok: [aws_instance]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] **********************************************************************************
ok: [aws_instance]

TASK [docker : Add Docker apt key] *************************************************************************************************************
changed: [aws_instance]

TASK [docker : Add Docker repository] **********************************************************************************************************
changed: [aws_instance]

TASK [docker : Install Docker packages] ********************************************************************************************************
changed: [aws_instance]

TASK [docker : Install Docker Compose] *********************************************************************************************************
changed: [aws_instance]

TASK [docker : Ensure docker users are added to the docker group] ******************************************************************************
changed: [aws_instance] => (item=ubuntu)

TASK [docker : Reset SSH connection to apply user changes] *************************************************************************************

TASK [docker : Ensure Docker daemon.json exists with secure configuration] *********************************************************************
changed: [aws_instance]

RUNNING HANDLER [docker : restart docker] ******************************************************************************************************
changed: [aws_instance]

PLAY RECAP *************************************************************************************************************************************
aws_instance               : ok=14   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


```
</details>


<summary>On the server</summary>

<details>

```cmd

ubuntu@ip-172-31-20-88:~$ docker --version
Docker version 27.5.1, build 9f9e405
ubuntu@ip-172-31-20-88:~$ docker-compose --version
Docker Compose version v2.33.0
ubuntu@ip-172-31-20-88:~$
```

</details>


To list the inventory details, run:

```sh
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Output:

<summary>On the server</summary>

<details>

```cmd
{
    "_meta": {
        "hostvars": {
            "aws_instance": {
                "ansible_host": "ec2-18-209-6-147.compute-1.amazonaws.com",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/Downloads/lab5_key.pem",
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
            "aws_instance"
        ]
    }
}

```
</details>


To visualize the inventory structure, run:

```sh
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Output:

```sh
@all:
  |--@ungrouped:
  |  |--aws_instance
```

### Inventory File

The inventory file `default_aws_ec2.yml` is structured as follows:

```yaml
all:
  hosts:
    aws_instance:
      ansible_host: ec2-18-209-6-147.compute-1.amazonaws.com
      ansible_user: ubuntu
      ansible_ssh_private_key_file: ~/Downloads/lab5_key.pem
      ansible_python_interpreter: /usr/bin/python3

```

## Best Practices for Building the Role

The custom Docker role was developed following Ansible best practices:

### 1. **Role Structure**

- The role follows the standard directory structure (`defaults`, `handlers`, `tasks`, etc.), making it easy to organize and maintain.

- Tasks are modularized into separate files (e.g., `install_docker.yml`, `install_compose.yml`) for better readability and reusability.

### 2. **Idempotency**

- All tasks are designed to be idempotent, ensuring that running the playbook multiple times does not cause unintended changes.


### 3. **Variables and Defaults**

- Role variables are defined in `defaults/main.yml`, making it easy to customize the role without modifying the tasks.
- Sensible defaults are provided for all variables, such as `docker_edition: 'ce'` and `docker_users: ["ubuntu"]`.

### 4. **Handlers**

- Handlers are used to restart Docker only when necessary (e.g., after installing Docker packages), reducing unnecessary service restarts.


### 5. **Linting with `ansible-lint`**

- `ansible-lint` was installed and used to check the role for common issues and ensure compliance with best practices.
- To install `ansible-lint`:

  ```sh
  sudo apt-get install ansible-lint
  ```

- To lint the role:

  ```sh
  ansible-lint ansible
  ```
