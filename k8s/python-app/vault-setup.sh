#!/bin/bash

# Get the service account token
SERVICE_ACCOUNT_TOKEN=$(kubectl get secret $(kubectl get serviceaccount python-app -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode)

# Get the Kubernetes CA certificate
KUBE_CA_CERT=$(kubectl config view --raw --minify --flatten --output='jsonpath={.clusters[].cluster.certificate-authority-data}' | base64 --decode)

# Get the Kubernetes host
KUBE_HOST=$(kubectl config view --raw --minify --flatten --output='jsonpath={.clusters[].cluster.server}')

# Enable Kubernetes authentication in Vault
kubectl exec vault-0 -- vault auth enable kubernetes

# Configure Kubernetes authentication
kubectl exec vault-0 -- vault write auth/kubernetes/config \
    token_reviewer_jwt="$SERVICE_ACCOUNT_TOKEN" \
    kubernetes_host="$KUBE_HOST" \
    kubernetes_ca_cert="$KUBE_CA_CERT" \
    issuer="https://kubernetes.default.svc.cluster.local"

# Create a policy for our application
cat <<EOF | kubectl exec -i vault-0 -- vault policy write python-app -
path "secret/data/mysecret" {
  capabilities = ["read"]
}
EOF

# Create a role for our application
kubectl exec vault-0 -- vault write auth/kubernetes/role/python-app \
    bound_service_account_names=python-app \
    bound_service_account_namespaces=default,dev,prod \
    policies=python-app \
    ttl=1h

# Store our secret in Vault
kubectl exec vault-0 -- vault kv put secret/mysecret password=mysecretpassword 