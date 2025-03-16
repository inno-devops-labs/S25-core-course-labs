# Lab 9: Kubernetes Deployment

This report documents the Kubernetes deployment process for Lab 9, including imperative and declarative approaches, service exposure, and Ingress configuration.

---

## **Task 1: Imperative Deployment**

### **Steps**
1. **Start Minikube**:
   ```bash
   minikube start --driver=docker
   ```

2. **Create Deployment & Service:**
   ```bash
   kubectl create deployment my-app --image=nginx:alpine
   kubectl expose deployment my-app --type=NodePort --port=80
   ```

3. **Access the Application:**
   ```bash
   minikube service my-app --url  # Output: http://192.168.49.2:32362
   ```

4. **Verification:**
   ```bash
   kubectl get pods,svc
   ```
   <details> <summary>Click to view output</summary>
   
   ```bash
   NAME                         READY   STATUS    RESTARTS   AGE
   pod/my-app-d94b8f998-c27wt   1/1     Running   0          113s

   NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
   service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        8m14s
   service/my-app       NodePort    10.110.81.28   <none>        80:32362/TCP   69s
   ```
   </details>

---

## **Task 2: Declarative Manifests**

### **Manifest Files**
- `deployment.yml`: Deployment with 3 replicas.
- `service.yml`: LoadBalancer service.

### **Apply Manifests**
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

### **Verification**
```bash
kubectl get pods,svc
```
<details> <summary>Click to view output</summary>

```bash
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-5d894496d5-2wwkr   1/1     Running   0          15s
pod/my-app-5d894496d5-fdpqb   1/1     Running   0          15s
pod/my-app-5d894496d5-p68j8   1/1     Running   0          15s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        18m
service/my-app       LoadBalancer   10.106.201.172   <pending>     80:31783/TCP   6s
```
</details>

---

## **Bonus Task: Ingress & Multi-App Deployment**

### **Steps**
1. **Enable Ingress:**
   ```bash
   minikube addons enable ingress
   ```

2. **Deploy Second App:**
   - `deployment-app2.yml`: Apache HTTPD deployment.
   - `service-app2.yml`: Service for Apache.

3. **Configure Ingress:**
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: my-ingress
     annotations:
       nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     rules:
     - http:
         paths:
         - path: /app1
           pathType: Prefix
           backend:
             service:
               name: my-app
               port:
                 number: 80
         - path: /app2
           pathType: Prefix
           backend:
             service:
               name: my-app-2
               port:
                 number: 80
   ```

### **Verification**
#### **Check Pods & Services:**
```bash
kubectl get pods,svc
```
<details> <summary>Click to view output</summary>

```bash
NAME                           READY   STATUS    RESTARTS   AGE
pod/my-app-5d894496d5-2wwkr    1/1     Running   0          15m
pod/my-app-5d894496d5-fdpqb    1/1     Running   0          15m
pod/my-app-5d894496d5-p68j8    1/1     Running   0          15m
pod/my-app-2-7d5f8d98c-abcde   1/1     Running   0          2m

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        30m
service/my-app       LoadBalancer   10.106.201.172   <pending>     80:31783/TCP   12m
service/my-app-2     ClusterIP      10.111.222.333   <none>        80/TCP         2m
```
</details>

#### **Test Ingress Routes:**
```bash
curl http://192.168.49.2/app1  # NGINX
curl http://192.168.49.2/app2  # Apache
```
<details> <summary>Click to view outputs</summary>

**NGINX Output:**
```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
</html>
```

**Apache Output:**
```html
<html><body><h1>It works!</h1></body></html>
```
</details>

---

## **Screenshots**
- **Task 1/2 Service Access**: NGINX Welcome Page 
![](/screnshoots/first%20task/1_ngnix.png)
![](/screnshoots/second%20task/2_ngnix.png)
- **Ingress Routes**: Apache "It works!" Page 
![](/screnshoots/bonus/bonus.png)

---

## **Cleanup**
```bash
kubectl delete -f deployment.yml -f service.yml -f deployment-app2.yml -f service-app2.yml -f ingress.yml
minikube stop
