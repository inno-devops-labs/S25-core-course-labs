## Task 1: Confirm the accessibility of your application

To confirm the accessibility of your application, run the following command:

```bash
minikube service my-app-your-app --url
```
Output:

```pgsql
😿  service default/my-app-your-app has no node port
❗  Services [default/my-app-your-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
http://127.0.0.1:52470
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```
After running this command, you will receive the URL http://127.0.0.1:52470, which you can use to access the application locally. Note that the terminal should remain open for the Docker driver to work properly on Windows.

## Task 2: Get information about the pods and services in Kubernetes
To get information about the current status of your pods and services, run the following command:

```bash
kubectl get pods,svc
```
Output:

```pgsql
NAME                                  READY   STATUS    RESTARTS   AGE
pod/my-app-your-app-784449f74-6lsdq   1/1     Running   0          46s

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP    21m
service/my-app-your-app   ClusterIP   10.101.36.186   <none>        5000/TCP   7m59s
```
