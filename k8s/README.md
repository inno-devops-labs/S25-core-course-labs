# Kubernetes

---
## Create deployment and service without manifests

```
nikita@LAPTOP-DOBKKTS4:~$ kubectl create deployment moscow-app --image=zerohalf/moscow-time-app --port=8000
deployment.apps/moscow-app created
nikita@LAPTOP-DOBKKTS4:~$ kubectl expose deployment moscow-app --type=NodePort --port=80 --target-port=8000
service/moscow-app exposed
```

### `kubectl get pods,svc` command output
```
nikita@LAPTOP-DOBKKTS4:~$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/moscow-app-65d675bd58-45tz4   1/1     Running   0          43s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP   10.43.0.1     <none>        443/TCP        34d
service/moscow-app   NodePort    10.43.22.66   <none>        80:31576/TCP   8s
```

### Check the IP for browser access
```
nikita@LAPTOP-DOBKKTS4:~$ kubectl get nodes -o wide
NAME              STATUS   ROLES                  AGE   VERSION        INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION                       CONTAINER-RUNTIME
laptop-dobkkts4   Ready    control-plane,master   34d   v1.31.4+k3s1   172.17.201.28   <none>        Ubuntu 22.04.5 LTS   5.15.146.1-microsoft-standard-WSL2   containerd://1.7.23-k3s2
```

![Python App without manifest](screenshots/python-without-manifests.png)

### Clean up the deployment and service

```
nikita@LAPTOP-DOBKKTS4:~$ kubectl delete deployment moscow-app
deployment.apps "moscow-app" deleted
nikita@LAPTOP-DOBKKTS4:~$ kubectl delete service moscow-app
service "moscow-app" deleted
```
---

## Create deployment and service with manifests

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl apply -f k8s
deployment.apps/fastapi-moscow-deployment created
service/fastapi-service created
```

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl get pods,svc
NAME                                             READY   STATUS    RESTARTS   AGE
pod/fastapi-moscow-deployment-5559cc86cc-4xqv9   1/1     Running   0          73s
pod/fastapi-moscow-deployment-5559cc86cc-prl2l   1/1     Running   0          73s
pod/fastapi-moscow-deployment-5559cc86cc-sgwsq   1/1     Running   0          73s

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/fastapi-service   NodePort    10.43.209.247   <none>        80:30001/TCP   73s
service/kubernetes        ClusterIP   10.43.0.1       <none>        443/TCP        34d
```

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl get svc -A
NAMESPACE     NAME              TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
default       fastapi-service   NodePort       10.43.209.247   <none>          80:30001/TCP                 2m13s
default       kubernetes        ClusterIP      10.43.0.1       <none>          443/TCP                      34d
kube-system   kube-dns          ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       34d
kube-system   metrics-server    ClusterIP      10.43.107.250   <none>          443/TCP                      34d
kube-system   traefik           LoadBalancer   10.43.184.133   172.17.201.28   80:31466/TCP,443:30746/TCP   34d

nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl get svc -o wide
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE     SELECTOR
fastapi-service   NodePort    10.43.209.247   <none>        80:30001/TCP   2m28s   app=fastapi
kubernetes        ClusterIP   10.43.0.1       <none>        443/TCP        34d     <none>
```

![Python App with  manifest](screenshots/python-manifest.png)

---

## Bonus task for NodeJS with Ingress

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl apply -f k8s/
ingress.networking.k8s.io/app-ingress configured
deployment.apps/nodejs-moscow-deployment unchanged
service/nodejs-service unchanged
deployment.apps/fastapi-moscow-deployment unchanged
service/fastapi-service unchanged
```

![Nodejs App with manifest](screenshots/nodejs-manifest.png)

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ kubectl get po,svc,ingress
NAME                                             READY   STATUS    RESTARTS   AGE
pod/fastapi-moscow-deployment-5559cc86cc-4xqv9   1/1     Running   0          12m
pod/fastapi-moscow-deployment-5559cc86cc-prl2l   1/1     Running   0          12m
pod/fastapi-moscow-deployment-5559cc86cc-sgwsq   1/1     Running   0          12m
pod/nodejs-moscow-deployment-848dbcc7c4-qdrrb    1/1     Running   0          4m3s
pod/nodejs-moscow-deployment-848dbcc7c4-sd2cv    1/1     Running   0          4m3s
pod/nodejs-moscow-deployment-848dbcc7c4-xg4kk    1/1     Running   0          4m3s

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/fastapi-service   NodePort    10.43.209.247   <none>        80:30001/TCP   12m
service/kubernetes        ClusterIP   10.43.0.1       <none>        443/TCP        34d
service/nodejs-service    NodePort    10.43.87.121    <none>        80:30002/TCP   4m3s

NAME                                    CLASS     HOSTS                                ADDRESS         PORTS   AGE
ingress.networking.k8s.io/app-ingress   traefik   fastapi-app.local,nodejs-app.local   172.17.201.28   80      12s
```

I added `fastapi-app.local` and `nodejs-app.local` to `/etc/hosts` in the following format to `curl` known hosts:
```
127.0.0.1 fastapi-app.local
127.0.0.1 nodejs-app.local
```

```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ curl -H "Host: fastapi-app.local" http://localhost
{"Moscow Time":"2025-02-26 21:05:59"}

nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs$ curl -H "Host: nodejs-app.local" http://localhost
Current Moscow Time: 2025-02-26 21:06:02
```