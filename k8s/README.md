# Kubernetes lab report

Runtime: macOS with colima + `--kubernetes` option (k3s used under the hood)

## Log output of Task 1

```bash
> kubectl create deployment time-moscow --image=fallenchromium/moscow-timezone-app --port=8000
deployment.apps/time-moscow created
> kubectl get deployments

NAME          READY   UP-TO-DATE   AVAILABLE   AGE
time-moscow   0/1     1            0           7s
> kubectl get pods

> kubectl expose deployment time-moscow --type=LoadBalancer --port=8000
service/time-moscow exposed
> curl localhost:8000
{"time":"2025-02-26 18:04:03"}%                                                                                                                                

> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/time-moscow-5fddfcc55-nxs5m   1/1     Running   0          4m44s

NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.43.0.1      <none>        443/TCP          11m
service/time-moscow   LoadBalancer   10.43.196.83   192.168.5.1   8000:30543/TCP   69s
```

## Log output of Task 2

```bash
# attempt with default service spec
> kubectl apply -f deployment.yml -f service.yml
deployment.apps/time-moscow-deployment created
service/time-moscow-service created
> kubectl get pods,svc                          
NAME                                          READY   STATUS    RESTARTS   AGE
pod/time-moscow-deployment-785b5d4544-52hql   1/1     Running   0          18s
pod/time-moscow-deployment-785b5d4544-dhgvh   1/1     Running   0          18s
pod/time-moscow-deployment-785b5d4544-x27rq   1/1     Running   0          18s

NAME                          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/kubernetes            ClusterIP   10.43.0.1      <none>        443/TCP    26m
service/time-moscow-service   ClusterIP   10.43.54.220   <none>        8000/TCP   18s
> curl 10.43.0.1:8000
^C
> curl 10.43.54.220:8000
^C
> curl localhost:8000   
curl: (7) Failed to connect to localhost port 8000 after 1 ms: Couldn\'t connect to server

# not passing the ports. LoadBalancer was used by default when I created a service using a command, so I've changed the service spec
> kubectl apply -f deployment.yml -f service.yml
deployment.apps/time-moscow-deployment unchanged
service/time-moscow-service configured
> kubectl get pods,svc                       
NAME                                          READY   STATUS    RESTARTS   AGE
pod/time-moscow-deployment-785b5d4544-52hql   1/1     Running   0          2m49s
pod/time-moscow-deployment-785b5d4544-dhgvh   1/1     Running   0          2m49s
pod/time-moscow-deployment-785b5d4544-x27rq   1/1     Running   0          2m49s

NAME                          TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP      10.43.0.1      <none>        443/TCP          29m
service/time-moscow-service   LoadBalancer   10.43.54.220   192.168.5.1   8000:31544/TCP   2m49s
# I hate screenshots in the repo, so here's the curl output.
> curl localhost:8000 
{"time":"2025-02-26 18:22:20"}%                                                                                                                                
> curl 192.168.5.1:8000
^C
# not working. Apparently these are the internal IPs of my colima VM (I've used this VM with k3s instead of minikube)
> colima ssh
>> curl 192.168.5.1:8000
{"time":"2025-02-26 18:24:07"}
>> curl 10.43.54.220:8000
{"time":"2025-02-26 18:24:27"}
```

## Bonus task

1. Manifests for Extra App

Logs:

```bash
> kubectl apply -f service-extra.yml -f deployment-extra.yml 
service/propositional-logic-app-service created
deployment.apps/propositional-logic-app-deployment created
> kubectl get svc,pods
NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                        ClusterIP      10.43.0.1       <none>        443/TCP          38m
service/propositional-logic-app-service   LoadBalancer   10.43.195.163   192.168.5.1   80:32447/TCP     16s
service/time-moscow-service               LoadBalancer   10.43.54.220    192.168.5.1   8000:31544/TCP   12m

NAME                                                      READY   STATUS    RESTARTS   AGE
pod/propositional-logic-app-deployment-64cfffc74b-5x6dd   1/1     Running   0          16s
pod/propositional-logic-app-deployment-64cfffc74b-twvz2   1/1     Running   0          16s
pod/propositional-logic-app-deployment-64cfffc74b-zkmpc   1/1     Running   0          16s
pod/time-moscow-deployment-785b5d4544-52hql               1/1     Running   0          12m
pod/time-moscow-deployment-785b5d4544-dhgvh               1/1     Running   0          12m
pod/time-moscow-deployment-785b5d4544-x27rq               1/1     Running   0          12m
> curl localhost:80
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Propositional Logic Parser</title>
  <script type="module" crossorigin src="/assets/index-BtRqs7zN.js"></script>
  <link rel="stylesheet" crossorigin href="/assets/index-BW4v5JmN.css">
</head>
<body>
    <div class="container">
        <h1>Propositional Logic Parser</h1>
        
        <div class="input-section">
            <textarea id="formula-input" 
                      placeholder="Enter your formula (e.g., (A/\B))"
                      rows="3"></textarea>
            <div class="buttons">
                <button id="check-cnf">Check CNF</button>
                <button id="build-pcnf">Build PCNF</button>
            </div>
        </div>

        <div class="output-section">
            <div id="result" class="result-box"></div>
            <div id="ast-output" class="ast-box"></div>
        </div>
    </div>
</body>
</html> %                                                                                                                                                      
```

2. Ingress Manifests: