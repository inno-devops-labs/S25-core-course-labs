# Terraform State & Outputs

## 🔹 Lab 3: Docker Infrastructure State

### **Docker Resources**

- **Docker Image**: nginx
- **Docker Container**: nginx
- **Container Status**: Running
- **Exposed Port**: 80

### **Terraform State**

```bash
terraform state list
```

- `docker_image.nginx`
- `docker_container.nginx`

---

## 🔹 Lab 4: GitHub Repository State

### **GitHub Repository Details**

- **Default Branch**: master
- **Repository ID**: S25-core-course-labs
- **Repository Name**: S25-core-course-labs
- **Repository URL**: <https://github.com/MoeJaafar/S25-core-course-labs>

---

## 🔹 Lab 4: GitHub Teams (Bonus Task)

### **GitHub Teams Created**

- **Team: Developers** (Push Access)
- **Team: Admins** (Full Control)

### Terraform State

```bash
terraform state list
```

- `github_team.developers`
- `github_team.admins`
- `github_team_membership.dev_member`
- `github_team_membership.admin_member`
- `github_team_repository.developers_repo_access`
- `github_team_repository.admins_repo_access`

---

## 🔹 **Terraform Best Practices Applied**

### **1️⃣ State Management**

✅ Used `terraform state list` and `terraform state show` to track resources.  
✅ Ensured proper **state file management** to avoid conflicts.  

### **2️⃣ Provider & Authentication**

✅ Used **GitHub provider** securely with an **environment variable for authentication**.  
✅ Avoided hardcoding secrets in `.tf` files by using **Terraform variables**.  

### **3️⃣ Code Structure & Reusability**

✅ Organized Terraform files (`main.tf`, `provider.tf`, `variables.tf`, `outputs.tf`).  
✅ Used `variables.tf` to allow **flexibility** and avoid hardcoded values.  

### **4️⃣ Security & Access Control**

✅ Set repository visibility based on **Terraform variables** instead of hardcoding.  
✅ Disabled **GitHub Advanced Security settings** that were not supported.  
✅ Managed **GitHub Teams** and **permissions** using Terraform for role-based access control.  

### **5️⃣ Modularity & Reproducibility**

✅ Used `terraform apply -auto-approve` to automate deployments.  
✅ Ensured **idempotency** so running `terraform apply` doesn’t create duplicates.  
✅ Created **GitHub Teams dynamically**, making infrastructure easily adjustable.  
