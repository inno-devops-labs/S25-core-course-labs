- Task 1.3-1.4:
    - ![alt text](image.png)

## Task 1.5:
- Screenshot:
    - ![alt text](image-1.png)
- Text format:
    - ```bash
      kubectl get pods,svc
      ```
    - ```text
      NAME                             READY   STATUS    RESTARTS   AGE
      pod/fastapi-mt-b6d999f75-8x82v   1/1     Running   0          3m45s
  
      NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE  
      service/fastapi-mt   NodePort    10.104.63.29   <none>        8000:30352/TCP   3m42s
      service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          11m
      ```

## Task 1.6:
- Screenshot:
    - ![alt text](image-2.png)

## Task 2.3
- Used `deployment.yml` and `service.yml` with kubectl apply -f `{{path}}`.
- Screenshot for bullet point 2:
    - ![alt text](image-3.png)
- Text format:
    - ```bash
      kubectl get pods,svc
      ```
    - ```text
      NAME                                        READY   STATUS    RESTARTS   AGE
      pod/fastapi-mt-deployment-b6d999f75-fvdzr   1/1     Running   0          23s
      pod/fastapi-mt-deployment-b6d999f75-l2r6f   1/1     Running   0          23s
      pod/fastapi-mt-deployment-b6d999f75-zh5s6   1/1     Running   0          23s  
      NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
      service/fastapi-mt-service   NodePort    10.107.110.143   <none>        8000:30000/TCP   19s
      service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          30m
      ```
- Screenshot for bullet point 3:
    - ```bash
      minikube service --all
      ```
      ![alt text](image-4.png)

## Bonus Task 1
- `gin-deployment.yml` and `gin-service.yml` are created for additional application.

## Bonus Task 2
- `ingress.yml` created as an ingress manifests for applications.

## Bonus Task 3
- Applying ingress ![alt text](image-5.png)
- Application availability check:
    - ![alt text](image-6.png) 
    - ![alt text](image-7.png)