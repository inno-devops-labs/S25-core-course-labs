# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Output of `kubectl get pods,svc`

```bash
NAME                                           READY       STATUS     RESTARTS AGE
pod/moscowtime-app-1740772199-5cc9dcd7d5-4g5c2 1/1         Running    0         2m1s
pod/moscowtime-app-1740772199-5cc9dcd7d5-jwqb7 1/1         Running    0         2m1s
pod/moscowtime-app-1740772199-5cc9dcd7d5-zrk7t 1/1         Running    0         2m1s

NAME                                TYPE            CLUSTER-IP      EXTERNAL-IP         PORT(S)         AGE
service/kubernetes                  ClusterIP       10.96.0.1       <none>              443/TCP         71m
service/moscowtime-app-1740772199   LoadBalancer    10.102.109.60   127.0.0.1           8000:30505/TCP  2m1s
```

### Steps to create a Helm chart

1. Created a Helm chart template for the application:

   ```bash
   helm create moscowtime-app
   ```

2. Modified the `values.yaml` file to update the following:

   - Set repository to `haidarjbeily/distroless-moscow-time-app`
   - Set tag to `latest`
   - Set service port to `8000`
   - Set service type to `LoadBalancer`
   - Set replicaCount to `3`

3. Installed the Helm chart:

   ```bash
   helm install moscowtime-app --generate-name
   ```

   **Output:**

   ```bash
    NAME: moscowtime-app-1740772199
    LAST DEPLOYED: Fri Feb 28 22:49:59 2025
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:

    1. Get the application URL by running these commands:
    NOTE: It may take a few minutes for the LoadBalancer IP to be available.
    You can watch its status by running 'kubectl get --namespace default svc -w moscowtime-app-1740772199'
    export SERVICE_IP=$(kubectl get svc --namespace default moscowtime-app-1740772199 --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
    echo http://$SERVICE_IP:8000
   ```

4. Verified the installation by checking the Minikube dashboard:

   - Confirmed that all pods were running in the Workloads section
   - Verified that the service was properly configured
   - Ensured that all 3 replicas were healthy and running

5. Accessed the application using:

   ```bash
   minikube service moscowtime-app-1740772199
   ```
