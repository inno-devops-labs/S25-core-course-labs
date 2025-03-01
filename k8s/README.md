# Kubernetes Deployment

This folder contains the Kubernetes manifests for deployments and services for the Moscow Time API application.

## Deployment Results

```
NAME                                   READY   STATUS    RESTARTS   AGE
pod/moscow-time-api-56d97f7c6d-29slv   1/1     Running   0          30m
pod/moscow-time-api-56d97f7c6d-tkl2t   1/1     Running   0          30m
pod/moscow-time-api-56d97f7c6d-tkn88   1/1     Running   0          30m

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
service/kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP                         63m
service/moscow-time-api   NodePort    10.110.251.95   <none>        8001:31894/TCP,8000:31925/TCP   30m
```

## Service URLs

The application is accessible at the following URLs:
- API Service: http://192.168.49.2:31894
- Metrics Service: http://192.168.49.2:31925

## Accessing the Application

You can use `curl` to access the Moscow Time API:

```bash
curl http://192.168.49.2:31894
```

And you can access the metrics endpoint with:

```bash
curl http://192.168.49.2:31925
```

The application also provides a health check endpoint:

```bash
curl http://192.168.49.2:31894/health
```