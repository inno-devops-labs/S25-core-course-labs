   # Docker Role

   This role installs and configures Docker and Docker Compose.

   ## Requirements

   - Ansible 2.18+
   - Ubuntu 24.04

   ## Example Playbook

   ```yaml
   - hosts: all
      roles:
         - role: docker
           become: true