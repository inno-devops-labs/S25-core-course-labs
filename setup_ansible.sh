#!/bin/bash

# Создаем необходимые директории
mkdir -p ansible/inventory
mkdir -p ansible/playbooks/dev
mkdir -p ansible/roles/docker/{defaults,handlers,tasks}
mkdir -p ansible/roles/web_app/{defaults,handlers,meta,tasks,templates}

# Создаем ansible.cfg
cat > ansible/ansible.cfg << 'EOF'
[defaults]
inventory = ./ansible/inventory
roles_path = ./ansible/roles
host_key_checking = False
ansible_become_ask_pass = True

[privilege_escalation]
become = True
become_method = sudo
become_ask_pass = True
EOF

# Создаем inventory файл
cat > ansible/inventory/default_aws_ec2.yml << 'EOF'
---
all:
  hosts:
    localhost:
      ansible_connection: local
EOF

# Создаем плейбук
cat > ansible/playbooks/dev/main.yaml << 'EOF'
---
- name: Install Docker
  hosts: all
  become: true
  
  vars:
    docker_apt_release_channel: stable
    docker_apt_arch: amd64
    docker_apt_gpg_key: https://download.docker.com/linux/ubuntu/gpg
    docker_apt_repository: "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
    docker_install_compose: true
    docker_users:
      - "m7"
  
  roles:
    - geerlingguy.docker
EOF

# Устанавливаем роль Docker
ansible-galaxy install geerlingguy.docker

# Очищаем старые ключи и репозитории Docker
sudo rm -rf /etc/apt/keyrings/docker.asc
sudo rm -rf /usr/share/keyrings/docker-archive-keyring.gpg
sudo rm -rf /etc/apt/sources.list.d/docker.list
sudo rm -rf /etc/apt/sources.list.d/hashicorp.list

# Обновляем пакеты
sudo apt-get update

echo "Настройка Ansible завершена успешно!"
echo "Запускаем плейбук..."

# Запускаем плейбук с запросом sudo пароля
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

echo "Установка Docker завершена!" 