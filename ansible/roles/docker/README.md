# Docker Role

This role installs and configures Docker and Docker Compose with enhanced security features.

## Requirements

- Ansible 2.9+
- Debian-based system

## Security Features

This role implements several security best practices:

1. User namespace remapping
2. Disabled new privileges escalation
3. Configured logging limits
4. Non-root user setup
5. Secure daemon configuration

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```

## Usage

1. Ensure your inventory file is properly configured
2. Run the playbook: `ansible-playbook playbooks/dev/main.yaml`
    <details>
    <summary>View output</summary>
   
   ```bash
   (venv) dante@dante-pc:~/PycharmProjects/fork-S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/main.yaml
   
   PLAY [Install and configure Docker] **************************************************************************************************************************************************
   
   TASK [Gathering Facts] ***************************************************************************************************************************************************************
   [WARNING]: Platform linux on host ec2-instance is using the discovered Python interpreter at /usr/bin/python3.11, but future installation of another Python interpreter could change
   the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
   ok: [ec2-instance]
   
   TASK [docker : Remove old versions] **************************************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/remove_old_versions.yml for ec2-instance
   
   TASK [docker : Remove conflicting packages] ******************************************************************************************************************************************
   ok: [ec2-instance]
   
   TASK [docker : Add repo] *************************************************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_repo.yml for ec2-instance
   
   TASK [docker : Update apt] ***********************************************************************************************************************************************************
   changed: [ec2-instance]
   
   TASK [docker : Install prerequisites for key addition] *******************************************************************************************************************************
   changed: [ec2-instance]
   
   TASK [docker : Add Docker apt repository key.] ***************************************************************************************************************************************
   changed: [ec2-instance]
   
   TASK [docker : Add Docker's official apt repository] *********************************************************************************************************************************
   changed: [ec2-instance]
   
   TASK [docker : Install Docker] *******************************************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-instance
   
   TASK [docker : Install Docker and dependencies] **************************************************************************************************************************************
   changed: [ec2-instance]
   
   TASK [docker : Add user(s) to Docker group] ******************************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_to_group.yml for ec2-instance
   
   TASK [docker : Add user to docker group] *********************************************************************************************************************************************
   changed: [ec2-instance] => (item=dante)
   
   TASK [docker : Start docker on startup] **********************************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/enable_on_boot.yml for ec2-instance
   
   TASK [docker : Enable Docker service on boot] ****************************************************************************************************************************************
   ok: [ec2-instance]
   
   TASK [docker : Configure Docker security settings] ***********************************************************************************************************************************
   included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-instance
   
   TASK [docker : Create docker config directory] ***************************************************************************************************************************************
   ok: [ec2-instance]
   
   TASK [docker : Configure Docker daemon security settings] ****************************************************************************************************************************
   changed: [ec2-instance]
   
   RUNNING HANDLER [docker : Restart Docker service] ************************************************************************************************************************************
   changed: [ec2-instance]
   
   PLAY RECAP ***************************************************************************************************************************************************************************
   ec2-instance               : ok=18   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
   ```
   </details>

3. For a dry run:
    ```bash
    ansible-playbook playbooks/dev/main.yaml --check
    ```

## Security Considerations

The role implements several security measures:

- Docker daemon runs with reduced privileges
- Container logging is limited to prevent disk space issues
- User namespace remapping is enabled by default
- New privilege escalation is disabled

## Maintenance

Regular updates and security patches should be applied using:

```bash
ansible-playbook playbooks/dev/main.yaml --tags update
```