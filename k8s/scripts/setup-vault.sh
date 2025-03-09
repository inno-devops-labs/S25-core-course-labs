#!/bin/bash

# Wait for Vault pod to be ready
echo "Waiting for Vault pod to be ready..."
kubectl wait --for=condition=ready pod/vault-0

# Port forward Vault
echo "Setting up port forwarding..."
kubectl port-forward vault-0 8200:8200 &
sleep 5

# Set Vault address
export VAULT_ADDR='http://127.0.0.1:8200'

# Create the secret
echo "Creating secret in Vault..."
kubectl exec -it vault-0 -- /bin/sh -c '
vault kv put secret/myapp/config \
    username="db-user" \
    password="db-password-123"
'

# Enable Kubernetes authentication
echo "Enabling Kubernetes authentication..."
kubectl exec -it vault-0 -- /bin/sh -c '
vault auth enable kubernetes

vault write auth/kubernetes/config \
    kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" \
    token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
    kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
    issuer="https://kubernetes.default.svc.cluster.local"

vault policy write myapp-policy - <<EOF
path "secret/data/myapp/config" {
  capabilities = ["read"]
}
EOF

vault write auth/kubernetes/role/myapp \
    bound_service_account_names=test-app \
    bound_service_account_namespaces=default \
    policies=myapp-policy \
    ttl=24h
'

echo "Vault setup complete!" 