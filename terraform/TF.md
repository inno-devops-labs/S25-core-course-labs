# Terraform

## Creating Docker Using Terraform

- output of terraform state list:
![Alt text](assets/img1.jpg)

- output of terraform state show docker_container_nginx
![Alt text](assets/img2.jpg)

- output of terraform state show docker_image_nginx
![Alt text](assets/img3.jpg)

- let's check using the browser
![Alt text](assets/img4.jpg)

- let's change the name of the port and use a variable for the name of the docker, and then apply the changes
![Alt text](assets/img6.jpg)

- let's check the new port
![Alt text](assets/img5.jpg)

- output of terraform output
![Alt text](assets/img7.jpg)


## Creating VM Instance on AWS Using Terraform

- let's install awscli following the official documentaion https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- let's configure aws profile
![Alt text](assets/img8.jpg)

- let's create a new directory, then a new variables.tf file with our secret keys, then a new main.tf file within it with the following configurations
![Alt text](assets/img9.jpg)

- let's check the plan
![alt text](assets/img12.jpg)

- let's apply and check the result using terraform show
![Alt text](assets/img10.jpg)

- let's check the dashboard on AWS
![alt text](assets/img11.jpg)

- so everything is working exactly as it's supposed to be

## Creating Github Repo Using Terraform

- after creating a new directory, let's setup the main.tf
![alt text](assets/img16.png)

- let's initialize terraform
![alt text](assets/img15.png)

- let's check the plan
![alt text](assets/img14.png)

- let's apply and check our repo, it workes!
![alt text](assets/img17.png)

- let's import our repo into our configuration
![alt text](assets/img18.png)

- let's check the state of our terraform
![alt text](assets/img19.png)

- now let's change the description of the previous created repo, and apply the changes
![alt text](assets/img20.png)

- let's check it on github, the description got updated
![alt text](assets/img21.png)

## Creating Github Team Using Terraform

- let's create an organization on github
![alt text](assets/img22.png)

- let's define the provider and the repo
![alt text](assets/img23.png)

- let's create 3 different teams [admins, developers, viewers]
![alt text](assets/img24.png)

- let's define 3 different rules
![alt text](assets/img25.png)

- let's check the plan
![alt text](assets/img26.png)

- let's apply and check the repo
![alt text](assets/img27.png)


## Terraform Best Practices

This document highlights best practices applied in our Terraform setup for **AWS**, **Docker**, and **GitHub** infrastructure.

### 1. Provider Configuration Best Practices
- **Explicitly specify provider versions** to ensure compatibility and prevent breaking changes:
  ```hcl
  terraform {
    required_providers {
      github = {
        source  = "integrations/github"
        version = "~> 4.0"
      }
    }
  }
  ```
- **Use `var.token` for authentication** instead of hardcoding secrets.

### 2. Separation of Concerns
- AWS, Docker, and GitHub configurations are defined in separate Terraform blocks.
- Each module is **independent**, making debugging and maintenance easier.

### 3. Secure Handling of Credentials
- **AWS credentials are stored as Terraform variables** (`var.access_key`, `var.secret_access_key`, `var.session_token`).
- **GitHub token is passed using `var.token`**, avoiding hardcoded sensitive data.

### 4. Consistent Resource Naming
- Resources have clear, structured names (`github_repository.repo`, `aws_instance.my_vm`).
- Naming conventions improve **readability** and **predictability**.

### 5. Idempotency and State Management
- Terraform ensures that infrastructure matches the desired configuration.
- Running `terraform plan` before `terraform apply` prevents unintended changes.

### 6. Infrastructure as Code (IaC) Principles
- **Declarative approach:** Resources are defined explicitly.
- **Version-controlled:** Terraform files should be committed to a repository for tracking changes.

### 7. GitHub Repository and Branch Protections
- **Default branch is set explicitly** to `"main"`:
  ```hcl
  resource "github_branch_default" "main" {
    repository = github_repository.repo.name
    branch     = "main"
  }
  ```
- **Branch protection rules enforce security:**
  - Admin enforcement
  - Required PR reviews
  - Mandatory conversation resolution

### 8. Using Terraform to Manage Teams
- GitHub teams are defined in Terraform to enforce **role-based access control (RBAC)**.
- **Ensures consistent team permissions across repositories.**

### 9. Scalability and Reusability
- Modular structure allows easy **addition of new services** (e.g., more AWS instances, GitHub repositories, Docker containers).
- Variables (`var.container_name`) improve flexibility.

### 10. Docker Containerization
- Terraform manages **Docker images and containers**, ensuring consistency:
  ```hcl
  resource "docker_image" "nginx" {
    name         = "nginx:latest"
    keep_locally = false
  }
  ```
- Containers are easily deployed and version-controlled.

By following these best practices, our Terraform setup is **secure, scalable, and maintainable**. 🚀

