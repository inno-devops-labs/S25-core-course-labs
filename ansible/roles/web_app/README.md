# 🚀 Web App Role

## 📌 Description

This Ansible role is responsible for deploying the **Moscow Time App** using Docker and `docker-compose`.

It pulls the latest Docker image **(`enot0704/moscow-time-app`)**, configures a `docker-compose.yml` file, and ensures the application is running.

---

## 📌 Requirements

- **Ansible 2.9+**
- **Ubuntu 22.04**
- **Docker installed**

This role depends on the `docker` role, which ensures that Docker is installed and running.

---

## 📌 Role Variables

| Variable               | Description                                      | Default Value                  |
|------------------------|------------------------------------------------|--------------------------------|
| `docker_image`        | Docker image name                              | `enot0704/moscow-time-app`    |
| `app_port`            | Port on which the app runs                      | `5000`                        |
| `web_app_full_wipe`   | Enables full wipe before deployment             | `false`                        |

---

## 📌 Tasks Overview

This role includes the following tasks:

1. **Ensures Docker is installed** (via `docker` role)
2. **Pulls the latest Docker image** (`enot0704/moscow-time-app`)
3. **Creates and configures `docker-compose.yml`** using Ansible templates
4. **Deploys the application** (`docker-compose up -d`)
5. **(Optional) Wipes the application** (`docker-compose down`) when `web_app_full_wipe=true`

---

## 📌 Example Playbook

```yaml
- name: Deploy Docker
  hosts: all
  become: true
  roles:
    - docker
    - web_app
```
