# Helm Chart Deployment Documentation

## Creating and Deploying a Helm Chart

1. **Navigate to the Kubernetes Configuration Directory:**
   ```sh
   cd k8s
   ```
2. **Create a New Helm Chart Named `moscow-time`:**
   ```sh
   helm create moscow-time
   ```
3. **Navigate to the Newly Created Helm Chart Directory:**
   ```sh
   cd moscow-time
   ```
4. **Install the Helm Chart:**
   ```sh
   helm install . --generate-name
   ```
   **Expected Output:**
   ![install](../images/charts/helm_install.png)

## Exposing Services in Minikube

1. **List All Services Running in Minikube:**

   ```sh
   minikube service --all
   ```

   **Expected Output:**
   ![services](../images/charts/services.png)


2. **Access the Minikube Dashboard:**
   ```sh
   minikube dashboard
   ```
   **Expected Output:**
   ![dashboards](../images/charts/dashboards.png)
   ![dashboards](../images/charts/workload.png)
   ![dashboards](../images/charts/deployments.png)
   ![dashboards](../images/charts/pods.png)
   ![dashboards](../images/charts/replica_sets.png)

---

This document outlines the steps to create and deploy a Helm chart within a Kubernetes Minikube environment. The outputs will be confirmed with screenshots during execution.
