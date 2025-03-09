# Lab 11: Kubernetes Secrets and Hashicorp Vault

## Task 1: Kubernetes Secrets and Resource Management

1. Creating a Secret: To create a secret in Kubernetes, the following command was executed:

```bash
kubectl create secret generic lab-11-secret --from-literal=password=lab-11-password

secret/lab-11-secret created
```

2. Verifying the Secret: To verify the secret, the following command was executed:

```bash
kubectl get secret lab-11-secret -o yaml

apiVersion: v1
data:
  password: bGFiLTExLXBhc3N3b3Jk
kind: Secret
metadata:
  creationTimestamp: "2025-03-09T19:35:54Z"
  name: lab-11-secret
  namespace: default
  resourceVersion: "712"
  uid: 2252fdff-7590-48d6-bdca-cbc755e74d88
type: Opaque
```

3. Decoding the Secret: To decode the secret, the following command was executed:

```bash
kubectl get secret lab-11-secret -o jsonpath='{.data.password}' | base64 --decode

lab-11-password
```

4. Verifying the Secret inside the Pod: To verify the secret inside the pod, the following command was executed:

```bash
kubectl exec python-app-6bbb9b5f5b-6m7hw -- printenv | grep PYTHON_APP_PASSWORD

PYTHON_APP_PASSWORD=lab-11-password
```

5. Verifying injected Vault Secret: To verify the secret inside the pod, the following command was executed:

```bash
kubectl exec -it python-app-5dc474886f-p97zl -- sh
/app $ cat /vault/secrets/database-config.txt

data: map[password:db-secret-password username:db-readonly-username]
metadata: map[created_time:2025-03-09T20:49:36.466499632Z custom_metadata:<nil> deletion_time: destroyed:false version:1]
```
