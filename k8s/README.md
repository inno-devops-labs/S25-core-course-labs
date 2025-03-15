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

I've had to check the diff between the `LoadBalancer` and `ClusterIP` services. I've used [this](https://habr.com/ru/companies/slurm/articles/358824/) article to figure it out.

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

# not passing the ports. LoadBalancer was used by default when I created a service using a command and it worked. 
# ClusterIP type didn't so I've changed the service spec to LoadBalancer. Apparently, Klipper (LB used in k3s) is a nice cheat to get a port mapped outside of the Colima VM.
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

2. Ingress Manifests

    In my case I already had a `LoadBalancer` service on port 80, I've changed it in case it will have a conflict with the ingress port binding. The next problem was the ingress controller. K3s colima profile doesn't have it by default (I presume it gets installed in minikube as an addon, but I don't have such option), so I've had to install it manually.

    Logs:

    ```bash
    > helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    helm repo update
    "ingress-nginx" has been added to your repositories
    Hang tight while we grab the latest from your chart repositories...
    ...Successfully got an update from the "ingress-nginx" chart repository
    Update Complete. ⎈Happy Helming!⎈
    >    helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace

    NAME: nginx-ingress
    LAST DEPLOYED: Wed Feb 26 19:06:04 2025
    NAMESPACE: ingress-nginx
    STATUS: deployed
    REVISION: 1
    TEST SUITE: None
    NOTES:
    The ingress-nginx controller has been installed.
    It may take a few minutes for the load balancer IP to be available.
    You can watch the status by running 'kubectl get service --namespace ingress-nginx nginx-ingress-ingress-nginx-controller --output wide --watch'

    An example Ingress that makes use of the controller:
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
        name: example
        namespace: foo
    spec:
        ingressClassName: nginx
        rules:
        - host: www.example.com
            http:
            paths:
                - pathType: Prefix
                backend:
                    service:
                    name: exampleService
                    port:
                        number: 80
                path: /
        # This section is only required if TLS is to be enabled for the Ingress
        tls:
        - hosts:
            - www.example.com
            secretName: example-tls

    If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

    apiVersion: v1
    kind: Secret
    metadata:
        name: example-tls
        namespace: foo
    data:
        tls.crt: <base64 encoded cert>
        tls.key: <base64 encoded key>
    type: kubernetes.io/tls
    > 
    > kubectl get service --namespace ingress-nginx nginx-ingress-ingress-nginx-controller --output wide --watch
    NAME                                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE   SELECTOR
    nginx-ingress-ingress-nginx-controller   LoadBalancer   10.43.30.226   192.168.5.1   80:31002/TCP,443:32167/TCP   70s   app.kubernetes.io/component=controller,app.kubernetes.io/instance=nginx-ingress,app.kubernetes.io/name=ingress
    ```

    Doing this and applying the ingress manifest worked, I could access the app using curl with the `--resolve` flag as indicated in the kubernetes docs (nifty feature! Glad I've found it).

    Logs:

    ```bash
    > colima ssh
    >> curl --resolve "propositional-logic-app.example:80:192.168.5.1" -i http://propositional-logic-app.example
    HTTP/1.1 200 OK
    Date: Wed, 26 Feb 2025 16:15:20 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 1002
    Connection: keep-alive
    Accept-Ranges: bytes
    Etag: "d7kwfcspgv0gru"
    Last-Modified: Wed, 05 Feb 2025 23:25:37 GMT
    Vary: Accept-Encoding

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
    >> exit
    logout
    > curl --resolve "propositional-logic-app.example:80:localhost" -i http://propositional-logic-app.example  
    curl: (49) Couldn't parse CURLOPT_RESOLVE entry 'propositional-logic-app.example:80:localhost'
    > curl --resolve "propositional-logic-app.example:80:127.0.0.1" -i http://propositional-logic-app.example
    HTTP/1.1 200 OK
    Date: Wed, 26 Feb 2025 16:15:43 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 1002
    Connection: keep-alive
    Accept-Ranges: bytes
    Etag: "d7kwfcspgv0gru"
    Last-Modified: Wed, 05 Feb 2025 23:25:37 GMT
    Vary: Accept-Encoding

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
    > 
    ```

3. Application Availability Check:

   I've kind of did, already. You can see the logs above: I've used curl to check the application availability rather than the browser because it was more convenient to me:

   ```bash
   curl --resolve "propositional-logic-app.example:80:localhost" -i http://propositional-logic-app.example # resolve for ingress host-based rule matching.
   curl 192.168.5.1:8000
   ```
