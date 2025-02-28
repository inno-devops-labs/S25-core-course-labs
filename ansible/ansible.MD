Step 1: Setting Up the Environment

1.1. Cloning the Docker Role
I started by cloning the geerlingguy.docker Ansible role from GitHub into my local roles directory. This role automates the installation and configuration of Docker on target machines.
cd roles
git clone https://github.com/geerlingguy/ansible-role-docker.git

1.2. Verifying the Role
After cloning the role, I ensured it was correctly placed in the roles directory by listing its contents:
ls roles/ansible-role-docker

Step 2: Creating the Ansible Playbook

2.1. Writing the Playbook
I created a playbook named main.yaml in the playbooks/dev/ directory. This playbook defines the tasks to be executed on the target hosts. Here’s the content of the playbook:
---
- name: Install Docker via Ansible Galaxy role
  hosts: all
  become: yes
  roles:
    - role: ansible-role-docker

2.2. Configuring the Inventory

I created an inventory file named default_aws_ec2.yml to define the target hosts. In this case, I targeted a single host (yandex_vm) with the following details:
all:
  hosts:
    yandex_vm:
      ansible_host: 158.160.128.245
      ansible_user: almaz
      ansible_ssh_private_key_file: ~/.ssh/id_rsa

Step 3: Running the Playbook

3.1. Executing the Playbook
With the playbook and inventory ready, I ran the following command to execute the playbook:

ansible-playbook -i default_aws_ec2.yml playbooks/dev/main.yaml

This command instructed Ansible to:
Use the inventory file default_aws_ec2.yml.
Execute the tasks defined in playbooks/dev/main.yaml.

Step 4: Verifying the Installation

After the playbook completed, I verified that Docker was installed and running on the target machine (yandex_vm). I SSHed into the machine and ran the following commands:
ssh -i ~/.ssh/id_rsa almaz@158.160.128.245
docker --version
sudo systemctl status docker
docker --version: Confirmed the installed Docker version.
systemctl status docker: Verified that the Docker service was running and enabled.