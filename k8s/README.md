# Kubernetes Deployment

## Imperative Deployment 

### Preparations

```bash
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ kubectl create deployment python-app --image=jodak628286/python_app:latest
deployment.apps/python-app created
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ kubectl get deployments                
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   1/1     1            1           13s
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
python-app-5b456b4c44-lvfst   1/1     Running   0          21s
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ kubectl expose deployment python-app --type=LoadBalancer --port=8080
service/python-app exposed
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ minikube service python-app
! Executing "docker container inspect minikube --format={{.State.Status}}" took an unusually long time: 2.221566513s
* Restarting the docker service may improve performance.
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8080 | http://192.168.49.2:30994 |
|-----------|------------|-------------|---------------------------|
* Opening service default/python-app in default browser...
  http://192.168.49.2:30994
```

### Results

Output of `kubectl get pods,svc`:

```bash
ubuntu@fhmhd8tturtcnb6bcjnt:~/S25-DevOps-labs$ kubectl get pods,svc                                                                    
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-5b456b4c44-lvfst   1/1     Running   0          3m10s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          5m13s
service/python-app   LoadBalancer   10.102.101.128   <pending>     8080:30994/TCP   2m28s
```

### Cleanup

```
kubectl delete service python-app
kubectl delete pod python-app-5b456b4c44-lvfst
```


