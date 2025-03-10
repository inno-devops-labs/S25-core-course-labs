# Task 1 & Task 2: Kubernetes Deployment (Declarative)

This document outlines how to **deploy** and **expose** a Python application using declarative Kubernetes manifests, ensuring **3 replicas** and providing details on verifying the deployment.

---

## 1. Create the Deployment (3 Replicas)

Apply the manifest for the **Deployment**:

```bash
kubectl apply -f deployment.yaml

```

Where `deployment.yaml` declares **3 replicas**. Verify the **Deployment** and **Pods** status:

```bash
kubectl get deployments
kubectl get pods

```

Sample output might look like:

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   3/3     3            3           30s

```

```
NAME                              READY   STATUS    RESTARTS   AGE
app-python-5c6bc776fd-abc12       1/1     Running   0          30s
app-python-5c6bc776fd-def45       1/1     Running   0          30s
app-python-5c6bc776fd-ghi67       1/1     Running   0          30s

```

---

## 2. Expose the Application via Service

Next, apply the **Service** manifest:

```bash
kubectl apply -f service.yaml

```

Confirm the service is created (noting **NodePort**):

```bash
kubectl get svc

```

Example output:

```
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app-python-service     NodePort    10.101.183.4    <none>        5000:30001/TCP   10s

```

---

## 3. Access the App

For **Minikube**, retrieve the IP and port:

```bash
minikube ip
# e.g., 192.168.49.2

curl http://192.168.49.2:30001

```

If your container listens on **port 5000**, you should see the app’s response in a browser or terminal.

---

## 4. Output of `kubectl get pods,svc`

Below is a sample combined output:

```bash
kubectl get pods,svc

```

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5c6bc776fd-abc12   1/1     Running   0          1m
pod/app-python-5c6bc776fd-def45   1/1     Running   0          1m
pod/app-python-5c6bc776fd-ghi67   1/1     Running   0          1m

NAME                     TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python-svc   NodePort   10.108.31.244  <none>        5000:30001/TCP   1m
service/kubernetes       ClusterIP  10.96.0.1      <none>        443/TCP          19h

```

Additionally, check:

```bash
minikube service --all

```

Which displays something like:

```
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:30001 |
|-----------|--------------------|-------------|---------------------------|

```

You can open the service in your default browser:

```bash
minikube service app-python-service

```

---

## 5. Cleanup

When finished, remove the created resources:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

```

Or specifically:

```bash
kubectl delete deployment app-python
kubectl delete service app-python-service

```
