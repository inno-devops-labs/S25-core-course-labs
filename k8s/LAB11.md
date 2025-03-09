### Task 1

##### Kubernetes

- To create secret, run in the terminal command as follows:
```kubectl create secret generic mysecret --from-literal=username=secretuser --from-literal=password=secretpass```

- To view secret, run in the terminal command as follows:
```kubectl get secret mysecret```

- To decode secret, run in the terminal commands as follows:
```kubectl get secret mysecret -o jsonpath='{.data.username}' | base64 --decode secretuser```

```kubectl get secret mysecret -o jsonpath='{.data.password}' | base64 --decode secretpass```

##### Helm

- To view secrets, run in the terminal command as follows:
```helm secrets view secrets.yaml```

### Task 2

- To add hashicorp vault, run in the terminal command as follows:
```helm repo add hashicorp https://helm.releases.hashicorp.com```

- To install, run command as follows:
```helm install vault hashicorp/vault --set "server.dev.enabled=true"```

- To set a secret, run command as follows:
```kubectl exec -it vault-0 -- /bin/sh```

- To inject secrets run as follows:
```kubectl exec $(kubectl get pod -l app.kubernetes.io/instance=helm-python,app.kubernetes.io/name=helm-python -o jsonpath="{.items[0].metadata.name}") --container helm-python```

- To patch run as follows:
```kubectl patch deployment helm-python --patch "$(cat patch-inject-secrets.yaml)"```