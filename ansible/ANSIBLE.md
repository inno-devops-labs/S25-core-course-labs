# Ansible Deployment Documentation

## Overview

This document outlines the configuration and deployment process for the custom Docker role. The role installs Docker and Docker Compose, ensures the Docker service is enabled at boot, and adds the current user to the Docker group so Docker commands can be run without `sudo`.

## Project Structure

```sh
     .
     |-- README.md
     |-- ansible
     |   |-- inventory
     |   |   |-- plugins
     |   |   |  -- yacloud_compute.yml
     |   |   -- default_yc_compute.yml
     |   |   -- token
     |   |   -- yacloud_compute.yaml
     |   |-- playbooks
     |   |   -- dev
     |   |       -- main.yaml
     |   |-- roles
     |   |   |-- docker
     |   |   |   |-- defaults
     |   |   |   |   `-- main.yml
     |   |   |   |-- handlers
     |   |   |   |   `-- main.yml
     |   |   |   |-- tasks
     |   |   |   |   |-- install_compose.yml
     |   |   |   |   |-- install_docker.yml
     |   |   |   |   |-- configure.yml
     |   |   |   |   |-- secure.yml
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
     |   `-- ANDIBLE.md
     |-- app_go
     |-- app_python
     `-- terraform
```


## Inventory Details

- **Inventory File:** `ansible/inventory/default_yc_compute.yml`
- **Example Command to List Inventory:**

  ```bash
  ansible-inventory -i inventory/default_yc_compute.yml --list
  ```
- Output:
    ```
    andrew@Andrews-MacBook-Pro ansible % ansible-inventory -i inventory/default_yc_compute.yml --list
    {
        "_meta": {
            "hostvars": {
                "my-cloud-vm": {
                    "ansible_host": "158.160.64.105",
                    "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                    "ansible_user": "username"
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
                "my-cloud-vm"
            ]
        }
    }
    ```
  
- **Graphical Representation of Inventory:**
  ```bash
  ansible-inventory -i inventory/default_yc_compute.yml --graph
  ```
- Output:
    ```
    andrew@Andrews-MacBook-Pro ansible % ansible-inventory -i inventory/default_yc_compute.yml --graph
    @all:
      |--@ungrouped:
      |  |--my-cloud-vm
    ```
  
## Playbook Execution

### Dry Run (Check Mode)

Before applying changes, perform a dry run to preview potential modifications:

```bash
ansible-playbook playbooks/dev/main.yaml --check --diff
```
**Output**:
```
andrew@Andrews-MacBook-Pro ansible % ansible-playbook playbooks/dev/main.yaml --check --diff 

PLAY [Deploy Docker and Web App on Yandex Cloud (Ubuntu 22.04)] ****************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
[WARNING]: Platform linux on host my-cloud-vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_docker.yml for my-cloud-vm

TASK [docker : Update apt cache] ***********************************************************************************************************************************************
changed: [my-cloud-vm]

TASK [docker : Install dependencies for Docker (Ubuntu)] ***********************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add Docker GPG key for Ubuntu] **********************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add Docker repository for Ubuntu] *******************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_compose.yml for my-cloud-vm

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/configure.yml for my-cloud-vm

TASK [docker : Ensure Docker service is enabled and started on boot] ***********************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add current user to docker group] *******************************************************************************************************************************
changed: [my-cloud-vm]

PLAY RECAP *********************************************************************************************************************************************************************
my-cloud-vm                : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Actual Deployment

To deploy the Docker role, run:
```bash
ansible-playbook playbooks/dev/main.yaml
```
**Output**:
```
andrew@Andrews-MacBook-Pro ansible % ansible-playbook playbooks/dev/main.yaml

PLAY [Deploy Docker and Web App on Yandex Cloud (Ubuntu 22.04)] ****************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
[WARNING]: Platform linux on host my-cloud-vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_docker.yml for my-cloud-vm

TASK [docker : Update apt cache] ***********************************************************************************************************************************************
changed: [my-cloud-vm]

TASK [docker : Install dependencies for Docker (Ubuntu)] ***********************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add Docker GPG key for Ubuntu] **********************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add Docker repository for Ubuntu] *******************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_compose.yml for my-cloud-vm

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : include_tasks] **************************************************************************************************************************************************
included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/configure.yml for my-cloud-vm

TASK [docker : Ensure Docker service is enabled and started on boot] ***********************************************************************************************************
ok: [my-cloud-vm]

TASK [docker : Add current user to docker group] *******************************************************************************************************************************
changed: [my-cloud-vm]

PLAY RECAP *********************************************************************************************************************************************************************
my-cloud-vm                : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Additional Notes

- **Custom Docker Role Features:**
  - **Installation:** Installs Docker and Docker Compose.
  - **Service Configuration:** Enables Docker to start on boot (`systemctl enable docker`).
  - **User Configuration:** Adds the current user (specified by `ansible_user`) to the Docker group to avoid the need for `sudo` with Docker commands.
  
- **Variables in Use:**
  - `docker_version`: Version of Docker to install (default is `latest`).
  - `docker_compose_version`: Version of Docker Compose to install (default: `2.32.4`).
  - Additional variables like `docker_gpg_key_url`, `docker_repo`, and `docker_package_name` are defined in the role's defaults.

- **Reference Role:**
  
  For an alternative solution, it is possible to install the geerlingguy.docker role from Ansible Galaxy:
  
  ```bash
  ansible-galaxy role install geerlingguy.docker
  ```

## Conclusion
This document provides all the necessary steps and commands to validate your Ansible setup, run a dry run, and deploy the custom Docker role on your target machine.

## Bonus Tasks

### Dynamic Inventory Setup

This project includes a dynamic inventory plugin for Yandex Cloud. The dynamic inventory configuration file (e.g., `inventory/yacloud_compute.yaml`) should contain your Yandex Cloud settings. For example:

```yaml
plugin: yacloud_compute
yacloud_token_file: "./inventory/token"
yacloud_clouds:
  - "cloud-jandr21"
yacloud_folders:
  - "azaki"
```

Also, do not forget to create `token` file. Just paste OAuth token from Yandex Cloud (`yc init`)

### Important Notes:
- **Python Dependency:**
- 
  Make sure you have the `yandexcloud` Python package installed:
  `pip install yandexcloud`
- **Ansible Configuration:**
- 
  To ensure Ansible recognizes your custom dynamic inventory plugin, add the following lines to your `ansible.cfg`:
  ```yaml
  [defaults]
  inventory_plugins = inventory/plugins/
  enable_plugins = yacloud_compute
  ```
- **Run:**
- 
  Run your playbook with the -u flag (`username`):

  `ansible-playbook playbooks/dev/main.yaml -u username`
  Output:
  ```
  andrew@Andrews-MacBook-Pro ansible % ansible-playbook playbooks/dev/main.yaml -u username
  
  PLAY [Deploy Docker and Web App on Yandex Cloud (Ubuntu 22.04)] ****************************************************************************************************************
  
  TASK [Gathering Facts] *********************************************************************************************************************************************************
  [WARNING]: Platform linux on host ansible is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
  the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
  ok: [ansible]
  
  TASK [docker : include_tasks] **************************************************************************************************************************************************
  included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_docker.yml for ansible
  
  TASK [docker : Update apt cache] ***********************************************************************************************************************************************
  changed: [ansible]
  
  TASK [docker : Install dependencies for Docker (Ubuntu)] ***********************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : Add Docker GPG key for Ubuntu] **********************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : Add Docker repository for Ubuntu] *******************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : Install Docker CE] **********************************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : include_tasks] **************************************************************************************************************************************************
  included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/install_compose.yml for ansible
  
  TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : include_tasks] **************************************************************************************************************************************************
  included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/configure.yml for ansible
  
  TASK [docker : Ensure Docker service is enabled and started on boot] ***********************************************************************************************************
  ok: [ansible]
  
  TASK [docker : Add current user to docker group] *******************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : include_tasks] **************************************************************************************************************************************************
  included: /Users/andrew/PycharmProjects/S25-devops/ansible/roles/docker/tasks/secure.yml for ansible
  
  TASK [docker : Copy secure Docker daemon configuration] ************************************************************************************************************************
  ok: [ansible]
  
  TASK [docker : Validate Docker daemon configuration JSON syntax] ***************************************************************************************************************
  ok: [ansible]
  
  PLAY RECAP *********************************************************************************************************************************************************************
  ansible                    : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
  
  WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
  E0000 00:00:1739640273.810580  486288 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
  ```
  While writing logs, there were a mistake with validation. So, be careful with commands.

## Secure Docker Configuration

To enhance Docker security, the custom Docker role includes tasks that configure the Docker daemon with secure settings without relying on an external file. Instead, the configuration is defined inline.

For example, the task to configure Docker's secure settings is as follows:

```yaml
- name: Copy secure Docker daemon configuration
  copy:
    content: |
      {
          "userns-remap": "default"
      }
    dest: /etc/docker/daemon.json
    owner: root
    group: root
    mode: '0644'
  notify: restart docker
```

This task creates a `/etc/docker/daemon.json` file that enables user namespace remapping (`"userns-remap": "default"`), which maps the container's root user to a non-privileged host user, thereby enhancing container security.

To ensure that the JSON syntax in the configuration file is valid, the following validation task is used:
```yaml
- name: Validate Docker daemon configuration JSON syntax
  command: python3 -m json.tool /etc/docker/daemon.json
  changed_when: false
```

This command verifies that `/etc/docker/daemon.json` contains syntactically valid JSON. If the file has invalid JSON, the task will fail, preventing the deployment of an incorrect configuration.

## Bonus Conclusion

These bonus tasks extend your Ansible deployment by integrating two key enhancements:

- **Dynamic Inventory for Yandex Cloud:**  
  Automatically discovers and manages your hosts from Yandex Cloud, reducing the need for manual inventory maintenance.

- **Secure Docker Configuration:**  
  Enhances the security of your Docker installation by enabling user namespace remapping and validating the Docker daemon configuration inline, ensuring that only valid, secure settings are applied.

Together, these improvements not only streamline your automation process but also strengthen the overall security and maintainability of your deployment. Customize these configurations further to suit your specific environment and operational requirements.
