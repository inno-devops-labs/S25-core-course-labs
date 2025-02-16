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