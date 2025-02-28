# Lab 9

## Task 1: Kubernetes Setup and Basic Deployment

### Output of `kubectl get pods,svc`

```bash
NAME                                READY             STATUS          RESTARTS         AGE
pod/quote-app-76c97898df-mb8sw      1/1               Running          0               5m44s

NAME                TYPE          CLUSTER-IP      EXTERNAL-IP   PORT(S)               AGE
service/kubernetes  ClusterIP     10.96.0.1      <none>        443/TCP              24m
service/quote-app   LoadBalancer  10.100.151.190 <pending>     8000:32024/TCP       2m53s
```

### Steps taken to complete the task

1. **Kubernetes Setup**:

   - Installed `kubectl` and `minikube` on my local machine to manage the Kubernetes cluster.

2. **Application Deployment**:

   - Created a `Deployment` resource for the Moscow Time Web Application using the command:

     ```bash
     kubectl create deployment quote-app --image=haidarjbeily/distroless-moscow-time-app
     ```

   - Verified the deployment by checking the status of the pods.

3. **Service Creation**:

   - Exposed the application to the outside world by creating a `Service` resource:

     ```bash
     kubectl expose deployment quote-app --type=LoadBalancer --port=8000
     minikube service quote-app
     ```

   - This allows external access to the application through the specified port.

4. **Verification**:

   - Used the command `kubectl get pods,svc` to confirm that the pod and service were running correctly, as shown in the output above.

5. **Cleanup**:
   - After testing, I removed the `Deployment` and `Service` resources to maintain a clean Kubernetes environment:

     ```bash
     kubectl delete deployment quote-app
     kubectl delete service quote-app
     ```
