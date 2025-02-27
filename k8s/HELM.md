# Lab 10: Introduction to Helm

---

## Mohammad Jaafar - CBS-01

### **1. Overview**

---

This document details my process of learning Helm, setting up Helm charts, deploying applications with Helm, and implementing Helm chart hooks. The lab is structured into two main tasks, with an additional bonus task covering Helm library charts.

---

## **2. Task 1: Helm Setup and Chart Creation**

### **2.1 Learning About Helm**

Before working with Helm, I reviewed the core concepts, including:

- **Helm Architecture:** Helm simplifies Kubernetes application deployment by managing configurations using Helm charts.
- **Understanding Helm Charts:** Helm charts are packages that contain Kubernetes manifests with customizable values.

Resources:

- [Helm Architecture](https://helm.sh/docs/topics/architecture/)
- [Understanding Helm Charts](https://helm.sh/docs/topics/charts/)

---

### **2.2 Installing Helm**

I installed Helm using:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

```

To verify the installation:

```bash
helm version

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image.png)

I then initialized the Helm repository:

```bash
helm repo add stable https://charts.helm.sh/stable
helm repo update

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%201.png)

---

### **2.3 Creating a Helm Chart for `python-app`**

To package my Python-based Flask application, I created a Helm chart inside the `k8s` folder:

```bash
cd k8s
helm create python-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%202.png)

This created a directory structure like:

```sh
k8s/
  ├── python-app/
      ├── charts/
      ├── templates/
      ├── values.yaml
      ├── Chart.yaml
      ├── README.md

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%203.png)

I modified the `values.yaml` file to use my Docker repository:

```yaml
image:
  repository: em1999jay/python-app
  tag: latest

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%204.png)

And updated `templates/deployment.yaml` to set the correct port:

```yaml
ports:
  - containerPort: 5000

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%205.png)

---

### **2.4 Installing the Helm Chart**

I installed the Helm chart in my Minikube cluster:

```bash
helm install python-app ./python-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%206.png)

To confirm successful deployment:

```bash
helm list
kubectl get pods,svc

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%207.png)

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%208.png)

---

### **2.5 Accessing My Application**

To access my application:

```bash
minikube service python-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%209.png)

I confirmed the correct service endpoint and accessed the application in a browser.

---

## **3. Task 2: Helm Chart Hooks**

### **2.1 Learning About Helm Hooks**

Before implementing Helm hooks, I reviewed their functionality:

- **Pre-install Hook**: Runs before Helm installs the application.
- **Post-install Hook**: Runs after the application is successfully deployed.
- **Hook Delete Policy**: Ensures that completed hooks do not persist unnecessarily.

📌 **References:**

- [Helm Hooks Documentation](https://helm.sh/docs/topics/charts_hooks/)
- [Best Practices for Helm Hooks](https://helm.sh/docs/chart_best_practices/)

---

### **2.2 Implementing Helm Hooks**

I created **pre-install** and **post-install** hooks for both applications inside their respective `templates/` directories.

### **Pre-Install Hook for `python-app`**

📍 File: `k8s/python-app/templates/pre-install-hook.yaml`

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pre-install-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": hook-succeeded

spec:
  template:
    spec:
      containers:
      - name: pre-install-job
        image: busybox
        command: ["sh", "-c", "echo 'Pre-install Hook Running for Python App'; sleep 10"]
      restartPolicy: Never

```

### **Post-Install Hook for `python-app`**

📍 File: `k8s/python-app/templates/post-install-hook.yaml`

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: post-install-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-delete-policy": hook-succeeded

spec:
  template:
    spec:
      containers:
      - name: post-install-job
        image: busybox
        command: ["sh", "-c", "echo 'Post-install Hook Completed for Python App'; sleep 10"]
      restartPolicy: Never

```

---

### **Pre-Install Hook for `node-app`**

📍 File: `k8s/node-app/templates/pre-install-hook.yaml`

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pre-install-node-hook
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-delete-policy": hook-succeeded

spec:
  template:
    spec:
      containers:
      - name: pre-install-node-job
        image: busybox
        command: ["sh", "-c", "echo 'Pre-install Hook Running for Node App'; sleep 10"]
      restartPolicy: Never

```

### **Post-Install Hook for `node-app`**

📍 File: `k8s/node-app/templates/post-install-hook.yaml`

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: post-install-node-hook
  annotations:
    "helm.sh/hook": post-install
    "helm.sh/hook-delete-policy": hook-succeeded

spec:
  template:
    spec:
      containers:
      - name: post-install-node-job
        image: busybox
        command: ["sh", "-c", "echo 'Post-install Hook Completed for Node App'; sleep 10"]
      restartPolicy: Never

```

---

### **2.3 Testing and Validating Helm Hooks**

### **Validating the Helm Charts**

I ran:

```bash
helm lint python-app
helm lint node-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2010.png)

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2011.png)

✔ **Both charts passed linting without errors.**

### **Testing Hooks with Dry-Run**

I executed:

```bash
helm install python-app ./python-app
helm install node-app ./node-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2012.png)

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2013.png)

✔ **Hooks appeared in the simulated output, confirming their recognition by Helm.**

### **Deploying Helm Charts**

I installed the Helm charts for both applications:

```bash
helm upgrade --install python-app ./python-app
helm upgrade --install node-app ./node-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2014.png)

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2015.png)

✔ **Deployments were successful.**

---

### **2.4 Verifying Hook Execution**

After deployment, I checked the running pods:

```bash
kubectl get pods

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2016.png)

✔ **Output:**

```sh
NAME                           READY   STATUS      RESTARTS   AGE
node-app-f7ccbbb94-7gk6z       1/1     Running     0          11m
post-install-hook-92tvg        0/1     Completed   0          10m
post-install-node-hook-7jn8b   0/1     Completed   0          11m
pre-install-hook-kf9v4         0/1     Completed   0          10m
pre-install-node-hook-gxrs2    0/1     Completed   0          11m
python-app-5d47767f7f-gwdbf    1/1     Running     0          10m
```

✔ **Both applications (`python-app` and `node-app`) are running.**

✔ **All four hooks (`pre-install` and `post-install` for both apps) completed successfully.**

### **Checking Hook Logs**

```bash
kubectl logs post-install-hook-n6sq8
kubectl logs post-install-node-hook-c7l76
kubectl logs pre-install-hook-wt2zd
kubectl logs pre-install-node-hook-p95gg
```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2017.png)

✔ Logs confirmed the hooks executed successfully.

---

## **3. Verifying Services and Accessibility**

To ensure the services were accessible, I checked:

```bash
kubectl get svc

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2018.png)

✔ **Expected Output:**

```sh
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   3h11m
node-app     ClusterIP   10.110.176.22   <none>        80/TCP    3m45s
python-app   ClusterIP   10.96.191.249   <none>        80/TCP    3m4s
```

I retested my applcations:

```bash
minikube service python-app
minikube service node-app 

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2019.png)

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2020.png)

✔ **Both applications were accessible in the browser.**

---

## **4.** Hook Delete Policy

this line right here assures Hook Delete Policy which removes the hook once it has executed successfully which i added to all my hooks:

```yaml
"helm.sh/hook-delete-policy": hook-succeeded
```

✔ **This removed completed hook pods while keeping deployments intact.**

---

## **Bonus Task: Helm Library Chart**

---

---

1. **Creating a Helm Library Chart** (`my-library-chart`).
2. **Using the library chart for shared configurations**.
3. **Ensuring both `python-app` and `node-app` use the library chart**.

---

## **4.1 Learning About Helm Library Charts**

Before implementing the library chart, I studied:

- **What is a Helm Library Chart?**
  - A **Helm Library Chart** contains shared templates but does not deploy resources itself.
    - Other charts **import** and use the templates from the library chart.
- **Why Use a Helm Library Chart?**
  - Avoids **duplicate configurations.**
    - Ensures **consistent settings** across multiple applications.
    - Improves **maintainability** of Helm charts.

📌 **References:**

- [Helm Library Chart Documentation](https://helm.sh/docs/topics/library_charts/)

---

## **4.2 Creating the Library Chart**

I created a **Helm Library Chart** inside the `k8s/` directory:

```bash
cd k8s
helm create my-library-chart

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2021.png)

 **File Structure:**

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2022.png)

---

## **4.3 Implementing the Shared Labels Template**

 **File:** `k8s/my-library-chart/templates/_labels.tpl`

```yaml
{{- define "custom.labels" -}}
app: {{ .Chart.Name }}
environment: production
managed-by: Helm
{{- end -}}

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2023.png)

✔ **This ensures that `python-app` and `node-app` automatically inherit these labels.**

---

## **4.4 Integrating the Library Chart with `python-app` and `node-app`**

 **File:** `k8s/python-app/Chart.yaml`

```yaml
dependencies:
  - name: my-library-chart
    version: 1.0.0
    repository: "file://../my-library-chart"

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2024.png)

 **File:** `k8s/node-app/Chart.yaml`

```yaml
dependencies:
  - name: my-library-chart
    version: 1.0.0
    repository: "file://../my-library-chart"

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2025.png)

 **Both applications now depend on `my-library-chart`.**

---

## **4.5 Updating the Deployment Files to Use Shared Labels**

### **Updating `deployment.yaml` for `python-app`**

 **File:** `k8s/python-app/templates/deployment.yaml`

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2026.png)

### **Updating `deployment.yaml` for `node-app`**

 **File:** `k8s/node-app/templates/deployment.yaml`

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2027.png)

✔ **Now both applications use the same standardized labels from `my-library-chart`.**

---

## **4.6 Updating Helm Dependencies**

To ensure Helm recognized the new dependency, I ran:

```bash
helm dependency update ./k8s/python-app
helm dependency update ./k8s/node-app

```

✔ **This successfully added `my-library-chart` to the dependencies.**

---

## **4.7 Deploying the Applications**

I then **upgraded** the applications using Helm:

```bash
helm upgrade --install my-python-app ./k8s/python-app
helm upgrade --install my-node-app ./k8s/node-app

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2028.png)

✔ **Both applications deployed successfully!** 🎉

---

## **4.8 Verifying Labels Are Applied**

I checked if the labels were correctly inherited:

```bash
kubectl get pods --show-labels

```

![image.png](Lab%2010%20Introduction%20to%20Helm%2013cf3f87232a80e7a8ebf93a0afb9c1b/image%2029.png)

✔ **Both applications now have the shared labels from `my-library-chart`**.

---

## **5. Conclusion**

Through this Bonus Task, I successfully:
**Created a Helm Library Chart (`my-library-chart`).**

**Implemented shared labels across `python-app` and `node-app`.**

**Removed duplicate configurations from individual charts.**

**Tested and confirmed that the labels were correctly applied.**

**Deployed the applications and verified that they worked.**
