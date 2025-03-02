## Task 1: Helm Setup and Chart Creation

This document details how we leveraged **Helm** to package our `app_python` into a reusable chart and deploy it on a local Kubernetes cluster (Minikube). It provides the **helm commands** used, as well as **kubectl** outputs verifying the app’s health and hooks.

---

### Step 1: Create and Install the Helm Chart

1. **Chart Creation**

   ```
   helm create app-python-helm
   ```

   This generates a folder named `app-python-helm` with default templates.

2. **Update values** in `app-python-helm/values.yaml`:

   ```
   image:
     repository: billyboone/python-moscow-time
     tag: latest
   service:
     type: ClusterIP
     port: 5000
   ```

3. **Install Chart**:

   ```
   helm install app-python-helm ./app-python-helm
   ```

   - `app-python-helm` is the **release name**.
   - `./app-python-helm` is the chart directory.

4. **Verify**:

   ```
   helm list
   NAME            	NAMESPACE	REVISION	UPDATED                             	STATUS  	CHART             	APP VERSION
   app-python-helm	default  	1       	2025-03-05 15:52:01.123456 +0300 EET	deployed	app-python-helm-0.1.0
   ```

---

### Step 2: Access the Application via Minikube

If your `values.yaml` sets up a **NodePort** service, you can do:

```
minikube service app-python-helm
```

Sample Output:

```
| NAMESPACE |      NAME       | TARGET PORT |             URL             |
|-----------|-----------------|-------------|-----------------------------|
| default   | app-python-helm |             | http://127.0.0.1:50612      |
|-----------|-----------------|-------------|-----------------------------|
🎉  Opening service default/app-python-helm in default browser...
```

---

### Step 3: kubectl get pods,svc Output

Use the following command to check **Pods** and **Services**:

```
kubectl get pods,svc
```

Sample result:

```
NAME                                   READY   STATUS    RESTARTS   AGE
pod/app-python-helm-5d6c47db5d-97pwt   1/1     Running   0          104s

NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/app-python-helm   ClusterIP   10.106.240.107   <none>        80/TCP    104s
service/kubernetes        ClusterIP   10.96.0.1        <none>        443/TCP   2d17h
```

This indicates:

- **Pod** named `app-python-helm-5d6c47db5d-97pwt` is running.
- **Service** named `app-python-helm` has **ClusterIP** type with internal port 80 (or 5000, depending on your `values.yaml`).

---

## Additional Helm Hooks (Example)

If you use **Helm Hooks** (e.g., pre-install or post-install), you may see ephemeral pods like:

```
kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-helm-5d6c47db5d-66kbg         1/1     Running     0          8m58s
helm-hooks-app-python-helm-preinstall   0/1     Completed   0          4m39s
helm-hooks-app-python-helm-postinstall  0/1     Completed   0          4m15s
```

You can inspect them:

```
kubectl describe po helm-hooks-app-python-helm-preinstall
```

The logs or `describe` output confirm those pods completed their tasks (often migrations, checks, etc.).

---

## Cleanup

When you no longer need the release, uninstall:

```
helm uninstall app-python-helm
```

Then confirm resources are gone:

```
kubectl get pods,svc
```

No relevant pods or services should remain.
