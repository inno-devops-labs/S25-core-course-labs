# Docker Role

This Ansible role installs and configures Docker and Docker Compose on a target host. It is designed to work on Ubuntu or similar Debian-based distributions.

## Requirements

- **Ansible:** Version 2.9 or later.
- **Target System:** Ubuntu 22.04 (or a compatible Debian-based distribution).
- **Privileges:** Sudo privileges are required on the target host.
- **Internet Access:** Necessary to download Docker packages and dependencies.

## Role Variables

The following variables can be overridden in your inventory or playbook:

- `docker_version`: The version of Docker to install.  
  **Default:** `"latest"`
- `docker_compose_version`: The version of Docker Compose to install.  
  **Default:** `"2.32.1"`

Example of variable usage:
```yaml
docker_version: "ce"
docker_compose_version: "v2.32.1"
```

## Role Structure

The role is organized into several directories to ensure modularity:

1. **`default/main.yml`** - Contains configurations for installing and managing Docker and Docker Compose.
2. **`handlers/main.yml`** - Includes a handler for the service module to restart the Docker service when triggered.
3. **`tasks/install_compose.yml`** - Handles the installation of Docker Compose using the pip module.
4. **`tasks/install_docker.yml`** - Manages the installation of Docker on Debian-based systems using the `apt` module.
5. **`tasks/main.yml`** - Defines tasks to update the apt cache, install `Python 3` and `pip3`, and imports and executes tasks for installing Docker and Docker Compose.

## Example Playbook

Below is an example playbook that uses the Docker role:
```yaml
- name: Deploy Docker on VM
  hosts: all
  become: true
  roles:
    - docker
```

## Usage

1. **Include the Role:**  
   In your playbook, add the Docker role under the `roles` section as shown above.

2. **Set Variables (Optional):**  
   Override any default variables in your inventory file or directly in the playbook if needed.

3. **Run the Playbook:**  
   Execute your playbook with:
   ```sh
   ansible-playbook -i <your_inventory_file> <your_playbook>.yaml
   ```
   For example, if using a local inventory:
   ```sh
   ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_local.yml
   ```

4. **Verify Installation:**  
   After the playbook runs, verify that Docker and Docker Compose are installed correctly:
   ```sh
   docker --version
   docker-compose --version
   systemctl status docker
   ```

## Additional Information

- **Security:**  
  The role includes tasks to configure Docker to start on boot and add the current user to the `docker` group to avoid using `sudo` for Docker commands. Optionally, a secure Docker daemon configuration can be applied.

- **Best Practices:**  
  - Modular role design using separate task files.
  - Use of role defaults to allow flexibility.
  - Handlers are used to restart Docker when configuration changes.
  - Follows Ansible best practices for readability and maintainability.



