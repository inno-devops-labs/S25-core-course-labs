# Lab 5: Ansible and Docker Deployment

## Overview

In this lab, you will get acquainted with Ansible, a powerful configuration management and automation tool. Your objective is to use Ansible to deploy Docker on a newly created cloud VM. This knowledge will be essential for your application deployment in the next lab.

## Task 1: Initial Setup

**6 Points:**

1. Repository Structure:
   - Organize your repository following the recommended structure below:

     ```sh
     .
     |-- README.md
     |-- ansible
     |   |-- inventory
     |   |   `-- default_aws_ec2.yml
     |   |-- playbooks
     |   |   `-- dev
     |   |       `-- main.yaml
     |   |-- roles
     |   |   |-- docker
     |   |   |   |-- defaults
     |   |   |   |   `-- main.yml
     |   |   |   |-- handlers
     |   |   |   |   `-- main.yml
     |   |   |   |-- tasks
     |   |   |   |   |-- install_compose.yml
     |   |   |   |   |-- install_docker.yml
     |   |   |   |   `-- main.yml
     |   |   |   `-- README.md
     |   |   `-- web_app
     |   |       |-- defaults
     |   |       |   `-- main.yml
     |   |       |-- handlers
     |   |       |   `-- main.yml
     |   |       |-- meta
     |   |       |   `-- main.yml
     |   |       |-- tasks
     |   |       |   `-- main.yml
     |   |       `-- templates
     |   |           `-- docker-compose.yml.j2
     |   `-- ansible.cfg
     |-- app_go
     |-- app_python
     `-- terraform
     ```

2. Installation and Introduction:
   - Install Ansible and familiarize yourself with its basics. You can follow the [Ansible installation guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

3. Use an Existing Ansible Role for Docker:
   - Utilize an existing Ansible role for Docker from `ansible-galaxy` as a template. You can explore [this Docker role](https://github.com/geerlingguy/ansible-role-docker) as an example.

4. Create a Playbook and Testing:
   - Develop an Ansible playbook for deploying Docker.
   - Test your playbook to ensure it works as expected.

## Task 2: Custom Docker Role

**4 Points:**

1. Create Your Custom Docker Role:
   - Develop a custom Ansible role for Docker with the following tasks:
     1. Install Docker and Docker Compose.
     2. Update your playbook to utilize this custom role. [Tricks and Tips](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html).
     3. Test your playbook with the custom role to ensure successful deployment.
     4. Make sure the role has a task to configure Docker to start on boot (`systemctl enable docker`).
     5. Include a task to add the current user to the `docker` group to avoid using `sudo` for Docker commands.

2. Documentation:
   - Develop an `ANSIBLE.md` file in the `ansible` folder to document your Ansible-related work.
   - Create a `README.md` file in the `ansible/roles/docker` folder.
   - Use a Markdown template to describe your Docker role, its requirements and usage.
   - Example `README.md` template for the Docker role:

   ```markdown
      # Docker Role

      This role installs and configures Docker and Docker Compose.

      ## Requirements

      - Ansible 2.9+
      - Ubuntu 22.04

      ## Role Variables

      - `docker_version`: The version of Docker to install (default: `latest`).
      - `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

      ## Example Playbook

      ```yaml
      - hosts: all
         roles:
            - role: docker
   ```

3. Deployment Output:
   - Execute your playbook to deploy the Docker role.
   - Provide the last 50 lines of the output from your deployment command in the `ANSIBLE.md` file.
   - Use the `--check` flag with `ansible-playbook` to perform a dry run and verify changes before applying them.

   Example command:

   ```sh
    ansible-playbook <path_to your_playbook> --diff
   ```

4. **Inventory Details:**
   - Execute the following command `ansible-inventory -i <name_of_your_inventory_file>.yaml --list` and provide its output in the `ANSIBLE.md` file.
   - Validate the inventory file using `ansible-inventory -i <name_of_your_inventory_file>.yaml --graph` to visualize the inventory structure.
   - Ensure you have documented the inventory information.

## Bonus Task: Dynamic Inventory

**2.5 Points:**

1. Set up Dynamic Inventory:
   - Implement dynamic inventory for your cloud environment, if available.
   - You may explore ready-made solutions for dynamic inventories:

     - [AWS Example](https://docs.ansible.com/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html)
     - [Yandex Cloud (Note: Not tested)](https://github.com/rodion-goritskov/yacloud_compute)

   Implementing dynamic inventory can enhance your automation capabilities.

2. Secure Docker Configuration:
   - Add a task to configure Docker security settings, disable root access.
   - Use the `copy` module and modify the `daemon.json` file.

### Guidelines

- Use proper Markdown formatting and structure for documentation files.
- Organize files within the lab folder with suitable naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Ensure that your repository is well-structured, follow Ansible best practices, and provide clear documentation for a successful submission.
