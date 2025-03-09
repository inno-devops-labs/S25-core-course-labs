#!/bin/bash

# Install Vault
echo "Installing Vault..."
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
helm install vault hashicorp/vault --set "server.dev.enabled=true"

# Wait for Vault to be ready and set it up
echo "Setting up Vault..."
./setup-vault.sh

# Deploy the application
echo "Deploying application..."
helm upgrade --install demo ./test-app

# Wait for the application to be ready
echo "Waiting for application to be ready..."
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=test-app

echo "Deployment complete!" 