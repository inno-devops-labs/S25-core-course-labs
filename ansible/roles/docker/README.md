# Docker Role

This role installs and configures Docker and Docker Compose. It also configures Docker to start on boot and adds the current user to the Docker group to allow running Docker commands without `sudo`. Additionally, it includes security configurations to improve Docker's safety, such as disabling root access.

## Requirements

- Ansible 2.9+  
- Ubuntu 20.04/22.04


## Example Playbook


```yaml
   - hosts: all
      roles:
         - role: docker