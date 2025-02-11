# Web App Role  

The Web App role facilitates deploying a web application by pulling its Docker image, creating a container, and starting it. It also generates a Docker Compose configuration. Additionally, Wipe tasks allow for removing the created container and associated Docker Compose file.  

## Host Requirements  

- Ubuntu 24.04  
- Docker and Docker Compose (can be set up using the inherited `docker` role)  
- Python 3.12  

## Role Variables  

- `web_app_docker_image` – The name of the web app's Docker image  
- `web_app_docker_image_tag` – The tag/version of the Docker image  
- `web_app_container_name` – The name assigned to the running container  
- `web_app_container_port` – The internal port the application listens on within the container  
- `web_app_port` – The port exposed on the VM  
- `web_app_full_wipe` – If enabled, removes both the container and the Docker Compose file  

## Usage  

```yaml
- hosts: all
  roles:
    - role: web_app
      become: true
