# Kubernetes

## Task 1

To deploy the app I used:

```bash
kubectl create deployment app-python --image=kira354/app_python-distroless:latest
kubectl expose deployment app-python --type=NodePort --port=5000
```

![task1](images_lab9/task1_1.png)

**Outputs from kubectl get pods,svc commands**
![task1](images_lab9/task1_2.png)
![task1](images_lab9/task1_3.png)

**Cleanup**
![task1](images_lab9/task1_4.png)

## Task 2

I created deployment.yml and service.yml inside k8s folder. Then deployed using:

```bash
kubectl apply -f k8s/
```

**Outputs from kubectl get pods,svc commands**
![task2](images_lab9/task2_1.png)
![task2](images_lab9/task2_2.png)

**The output of the `minikube service --all` command and the result from my browser**
![task2](images_lab9/task2_3.png)
![task2](images_lab9/task2_4.png)
![task2](images_lab9/task2_5.png)

## Bonus Task

Firstly, I did the same steps for app_javascript and created development_js.yml and service_js.yml.

**Outputs from kubectl get pods,svc commands**
![bonus](images_lab9/bonus_1.png)
![bonus](images_lab9/bonus_2.png)

**Checked output of the `minikube service --all` command in browser**
![bonus](images_lab9/bonus_3.png)
![bonus](images_lab9/bonus_4.png)
![bonus](images_lab9/bonus_5.png)

Secondly, I worked on ingress manifests for both apps and created ingress.yml:

```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-python-ingress
spec:
  rules:
  - host: app-python.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-python-service
            port:
              number: 5000
  - host: app-javascript.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-javascript-service
            port:
              number: 3000
```

**Application Availability Check**:

- run the tunnel:

```bash
minikube tunnel
```

- added host addresses to /etc/hosts:

```bash
127.0.0.1 app-python.local
127.0.0.1 app-javascript.local  
```

**Curl commands to verify the availability of applications**
![bonus](images_lab9/bonus_8.png)
![bonus](images_lab9/bonus_9.png)

**Checking in browser**
![bonus](images_lab9/bonus_7.png)
![bonus](images_lab9/bonus_10.png)
![bonus](images_lab9/bonus_11.png)
