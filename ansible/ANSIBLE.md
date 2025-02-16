## Documentation

#### inventory/default_yandex_cloud.yml

This Ansible inventory file defines a single host named ```host1``` with the IP address ```158.160.61.228``` and the ```ubuntu``` user as the target for Ansible operations.

#### playbooks/dev/main.yml

This Ansible playbook describes a set of tasks to be applied to all hosts (all). It includes a role named ```docker``` that should be executed with elevated privileges (become: true). 

Additionally, it defines a variable ```ansible_ssh_private_key_file``` pointing to the location of the SSH private key file (~/.ssh/id_ed25519) to use for SSH connections.

#### roles/docker

##### 1.default/main.yml

This Ansible file taken from provided example defines configurations for installing and managing Docker and Docker Compose. Here's a summary of the key configurations:

- `docker_edition`: Specifies the edition of Docker to install (either 'ce' for Community Edition or 'ee' for Enterprise Edition).
- `docker_packages`: Lists the Docker packages to install.
- `docker_service_manage`, `docker_service_state`, `docker_service_enabled`, `docker_restart_handler_state`: Configure the Docker service.
- `docker_install_compose_plugin`, `docker_compose_package`, `docker_compose_package_state`: Configure the Docker Compose plugin.
- `docker_install_compose`, `docker_compose_version`, `docker_compose_arch`, `docker_compose_url`, `docker_compose_path`: Configure Docker Compose installation.
- `docker_add_repo`, `docker_repo_url`, `docker_apt_release_channel`, `docker_apt_ansible_distribution`, `docker_apt_arch`, `docker_apt_repository`, `docker_apt_ignore_key_error`, `docker_apt_gpg_key`, `docker_apt_gpg_key_checksum`, `docker_apt_filename`, `docker_yum_repo_url`, `docker_yum_repo_enable_nightly`, `docker_yum_repo_enable_test`, `docker_yum_gpg_key`: Configure Docker repository setup for different Linux distributions.
- `docker_users`: A list of users to add to the Docker group.
- `docker_daemon_options`: Additional options to configure the Docker daemon.

##### 2. handlers/main.yml

This Ansible handler file defines a handler named "Restart docker" that uses the service module to restart the Docker service (name: docker) when triggered. 

The state parameter is set to ```restarted``` to ensure that the service is restarted.

##### 3. tasks/install_compose.yml

This Ansible task installs Docker Compose using the pip module. It ensures that the latest version of Docker Compose is installed on the target system.

##### 4. tasks/install_docker.yml

This Ansible task installs Docker on a Debian-based system using the ```apt``` module. It ensures that the docker.io package is present on the target system.

##### 5. tasks/main.yml

This Ansible playbook defines tasks to update the apt cache, install ```Python 3``` and ```pip3```, and import and execute tasks from separate files to install Docker and Docker Compose. 

The tasks related to Docker are tagged with 'docker' for organization and can be selectively executed using these tags.

#### roles/web_app

##### 1. default/main.yml

These variables are used to define the Docker image and container settings for a Python application.

- `docker_image`: The name of the Docker image for the Python application. In this case, it is set to `furryowolord/lab2`.
- `docker_image_tag`: The tag of the Docker image. This is set to `latest`.
- `docker_container_name`: The name of the Docker container for the Python application. It is set to `python_app`.
- `docker_container_port`: The port inside the Docker container where the Python application is listening. It is set to `80`.
- `docker_host_port`: The port on the host machine where the Docker container's port `80` is mapped to. It is set to `8080`.

##### 2. handlers/main.yml

This handler is used to restart the Docker container for the web application.

- `name`: Restart web_app container
- `docker_container`: Ansible module used to manage Docker containers.
  - `name`: Name of the Docker container, specified by the `docker_container_name` variable.
  - `state`: Desired state of the Docker container, in this case, `restarted`.

##### 3. mata/main.yml

This file specifies the role dependencies for the `web_app` Ansible role.

- `dependencies`: List of roles that the `web_app` role depends on.
  - `role`: Specifies the name of the role that `web_app` depends on, in this case, `docker`. This means that the `docker` role needs to be included in the playbook before the `web_app` role can be executed, ensuring that Docker is properly set up before deploying the web application.`meta/main.yml`

##### 4. tasks/O-wipe.yml

This Ansible task block defines the wipe logic for the web application, which involves stopping and removing the Docker container.

- `name`: Wipe logic for web app
- `block`: Ansible block used to group related tasks. In this case, it contains a single task to stop and remove the Docker container.
  - `name`: Stop and remove Docker container
  - `docker_container`: Ansible module used to manage Docker containers.
    - `name`: Name of the Docker container to be stopped and removed, specified by the `docker_container_name` variable.
    - `state`: Desired state of the Docker container, set to `absent` to ensure the container is removed.
- `when`: Conditional statement that checks if the `web_app_full_wipe` variable is `true`. If it is, the block of tasks will be executed; otherwise, it will be skipped.
- `tags`: Tags assigned to the task, in this case, `wipe`. This allows the task to be selectively executed using tags in the playbook.

##### 5. tasks/main.yml

This Ansible task block includes tasks related to managing the Docker image and container for the web application.

- `name`: Web App Tasks
- `block`: Ansible block used to group related tasks. It contains the following tasks:
  - `name`: Pull Docker image
    - `docker_image`: Ansible module used to manage Docker images.
      - `name`: Name of the Docker image to pull, specified by the `docker_image` variable.
      - `tag`: Tag of the Docker image to pull, specified by the `docker_image_tag` variable.
      - `source`: Source of the Docker image, set to `pull` to pull the image from a registry.
  - `name`: Run Docker container
    - `docker_container`: Ansible module used to manage Docker containers.
      - `name`: Name of the Docker container, specified by the `docker_container_name` variable.
      - `image`: Name of the Docker image to use for the container, specified by the `docker_image` variable.
      - `state`: Desired state of the Docker container, set to `started` to ensure the container is running.
      - `ports`: Port mapping configuration, mapping the host port `docker_host_port` to the container port `docker_container_port`.
  - `name`: Wipe Docker container
    - `import_tasks`: Import the tasks from the `tasks/0-wipe.yml` file, which contains the wipe logic for the Docker container.
    - `vars`: Set the `web_app_full_wipe` variable to `true` to ensure that the wipe logic is executed.

- `tags`: Tags assigned to the block, in this case, `web_app`. This allows the block of tasks to be selectively executed using tags in the playbook.

##### 6. templates/docker-compose.yml.j2

This is a Docker Compose template file used to define the configuration for the web application container.

- `version`: Specifies the version of the Docker Compose file format, set to `3.8`.
- `services`: Defines the services (containers) managed by Docker Compose. In this case, there is one service named `web_app`.
  - `web_app` service:
    - `image`: Specifies the Docker image to use for the `web_app` service, using the `docker_image` and `docker_image_tag` variables.
    - `container_name`: Sets the name of the Docker container to `docker_container_name`.
    - `ports`: Maps the host port `docker_host_port` to the container port `docker_container_port`, allowing access to the web application from the host machine.

#### ansible.ctg

This Ansible configuration file (`ansible.cfg`) specifies default settings for Ansible. Here's a breakdown of the key configurations:

- `playbook_dir`: Specifies the directory where playbooks are located.
- `inventory`: Specifies the directory where the inventory file is located.
- `roles_path`: Specifies the directory where Ansible roles are located.
- `remote_user`: Specifies the default user to use for SSH connections (`ubuntu` in this case).
- `host_key_checking`: Disables host key checking for SSH connections (set to `False`).
- `private_key_file`: Specifies the path to the SSH private key (`~/.ssh/id_ed25519`).
- `control_path`: Specifies the path template for the control path used for SSH connections.

These settings help configure Ansible to use specific directories and settings by default, reducing the need to specify them in each playbook.

### Deployment output for docker role
```
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-playbook playbooks/dev/main.yaml --diff --check

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/AntonChulakov/.ssh/id_ed25519': 
ok: [host1]

TASK [docker : Update apt] *****************************************************
changed: [host1]

TASK [docker : Python3 and pip3 installation] **********************************
changed: [host1]

TASK [docker : Install docker] *************************************************
changed: [host1]

TASK [docker : Install docker compose] *****************************************
changed: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Deployment output for docker and web_app role
```
~/Desktop/S25-core-course-labs/ansible  ‹lab6*› $ ansible-playbook playbooks/dev/main.yaml
PLAY [all] *********************************************************************
TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/AntonChulakov/.ssh/id_ed25519': 
Enter passphrase for key '/home/AntonChulakov/.ssh/id_ed25519': 
ok: [host1]
TASK [docker : Update apt] *****************************************************
ok: [host1]
TASK [docker : Python3 and pip3 installation] **********************************
ok: [host1]
TASK [docker : Install docker] *************************************************
ok: [host1]
TASK [docker : Install docker compose] *****************************************
ok: [host1]
TASK [web_app : Pull Docker image] *********************************************
changed: [host1]
TASK [web_app : Run Docker container] ******************************************
changed: [host1]
PLAY RECAP *********************************************************************
host1                      : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### Inventory details

```
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "158.160.61.228",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "hosts": [
            "host1"
        ]
    }
}
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all
 |--host1
```