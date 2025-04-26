# Lab 12

## All pods
```
kubectl get po
NAME                                    READY   STATUS    RESTARTS       AGE
my-app-backend-6c6cb5c96b-4jhmj         1/1     Running   0              78m
my-app-db-54588cb79-twqrq               1/1     Running   0              78m
my-app-frontend-5d4cf5c5dc-zq6xn        1/1     Running   0              78m
```
## Verification of the presence `config.json`

```
kubectl exec my-app-backend-6c6cb5c96b-4jhmj -- cat /etc/config/config.json
{
  "app": {
    "visits_file": "/usr/local/app/visits"
  },
  "database": {
    "timeout": 30,
    "max_connections": 50
  }
}
```
