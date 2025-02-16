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

### Deployment output
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