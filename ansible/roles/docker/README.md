# Docker Role

## Description
This role installs and configures Docker and Docker Compose on the target system.

## Requirements
- Ubuntu/Debian-based system
- Ansible 2.9+
- Python 3.x

## Role Variables
```yaml
docker_version: latest
docker_compose_version: "2.32.1"
docker_users: []

# Security settings
docker_live_restore: true        # Allows containers to run during daemon restart
docker_userland_proxy: false     # Disables userland-proxy for better performance
docker_no_new_privileges: true   # Prevents privilege escalation in containers
docker_userns_remap: "default"   # Enables user namespace isolation
docker_log_max_size: "10m"       # Maximum log file size
docker_log_max_files: "3"        # Number of log rotation files
```

## Security Features

The role includes the following security measures:
- Disabled root access
- User namespace remapping
- Container privilege limitations
- Log rotation
- Live-restore for minimal downtime

## Usage

### Apply changes
```bash
ansible-playbook ansible/playbooks/dev/main.yaml -K
```

## Dependencies
There are no external dependencies

## Example Usage

### Simple Example
```yaml
- hosts: all
  roles:
    - role: docker
```

### Advanced Example
```yaml
- hosts: all
  become: true
  vars:
    docker_users:
      - "m7"
  roles:
    - role: docker
```

## Role Structure
```
docker/
├── defaults/
│   └── main.yml
├── handlers/
│   └── main.yml
├── tasks/
│   ├── main.yml
│   ├── install.yml
│   └── configure.yml
├── vars/
│   └── main.yml
└── README.md
```

## Executable Tasks
1. Install necessary dependencies
2. Add Docker repository
3. Install Docker (version 27.5.1)
4. Install Docker Compose (version 2.32.1)
5. Configure Docker auto-start (systemctl enable docker)
6. Add user to docker group
7. Verify installation

## Role Testing
```bash
# Syntax Check
ansible-playbook ansible/playbooks/dev/main.yaml --syntax-check

# Dry Run
ansible-playbook ansible/playbooks/dev/main.yaml --check -K

# Apply Changes
ansible-playbook ansible/playbooks/dev/main.yaml -K
```