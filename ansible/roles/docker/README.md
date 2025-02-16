Here’s a **completely restructured and enhanced** version of your **Docker Role** documentation, making it more detailed, professional, and user-friendly.  

---

# **Ansible Role: Docker & Docker Compose Installation**  

This Ansible role automates the **installation, configuration, and setup** of Docker and Docker Compose on Ubuntu 22.04 hosts. It ensures that the latest stable versions are installed and ready for use.

---

## ** Supported Platforms**  
This role is designed for the following system requirements:  

 **Operating System**: Ubuntu 22.04 (Jammy)  
 **Python Version**: 3.x+ (required for Ansible execution)  

---

## ** What This Role Does**  

- Installs the latest **Docker Engine** and **Docker CLI**  
- Installs **Docker Compose** for containerized applications  
- Configures the system to allow non-root users to run Docker (optional)  
- Ensures Docker starts at boot  
- Provides a clean and idempotent setup  

---

## **⚙️ Role Variables**  

This role follows a **minimal configuration approach**—no additional variables are required.  
By default, it installs the latest stable versions of **Docker** and **Docker Compose**.

However, you can customize the installation by defining **optional variables** in your playbook:

```yaml
docker_version: latest  # Specify a Docker version (or leave as 'latest')
docker_compose_version: latest  # Specify a Docker Compose version
docker_users: []  # List of users to be added to the 'docker' group
```

---

## ** How to Use This Role**  

### **Basic Usage**  

To install and configure Docker with the default settings, use the following Ansible playbook:

```yaml
- name: Install Docker & Docker Compose
  hosts: all
  become: true  # Ensures the role runs with root privileges
  roles:
    - role: docker
```

### **Adding Users to the Docker Group **  

If you want to allow specific users to run Docker **without `sudo`**, define the `docker_users` variable:

```yaml
- name: Install Docker & Add Users to Docker Group
  hosts: all
  become: true
  roles:
    - role: docker
  vars:
    docker_users:
      - user1
      - user2
```

---

## ** Post-Installation Checks**  

After running the role, verify that Docker and Docker Compose are installed correctly:  

```bash
docker --version
docker compose version
```

To ensure Docker is running:

```bash
sudo systemctl status docker
```

To test Docker without `sudo` (if users were added to the `docker` group):

```bash
docker run hello-world
```

---