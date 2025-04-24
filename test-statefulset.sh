#!/bin/bash
set -e

echo "Testing StatefulSet Helm chart with dry-run..."
helm install --dry-run --debug python-stateful ./k8s/python-app-chart

echo "Deploying the StatefulSet Helm chart..."
helm install python-stateful ./k8s/python-app-chart

echo "Checking status of StatefulSet..."
kubectl get statefulsets,pods,services,pvc

echo "Waiting for all pods to be ready..."
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=python-app-chart --timeout=90s

echo "Testing pod access and state persistence..."
kubectl exec python-stateful-python-app-chart-0 -- cat /data/visits || echo "Visit count file not found yet"

echo "Creating test visits by accessing the service..."
minikube service python-stateful-python-app-chart --url

echo "Checking visit count in each pod..."
for i in $(seq 0 $(($(kubectl get statefulset python-stateful-python-app-chart -o jsonpath='{.spec.replicas}') - 1))); do
  echo "Pod python-stateful-python-app-chart-$i visit count:"
  kubectl exec python-stateful-python-app-chart-$i -- cat /data/visits || echo "Visit count file not found"
done

echo "Testing pod deletion and state persistence..."
echo "Current pods:"
kubectl get pods

echo "Deleting pod 0..."
kubectl delete pod python-stateful-python-app-chart-0

echo "Waiting for pod to be recreated..."
kubectl wait --for=condition=ready pod python-stateful-python-app-chart-0 --timeout=90s

echo "Checking if visit count persisted after pod recreation:"
kubectl exec python-stateful-python-app-chart-0 -- cat /data/visits

echo "Testing DNS for headless service..."
kubectl exec python-stateful-python-app-chart-0 -- nslookup python-stateful-python-app-chart-1.python-stateful-python-app-chart

echo "Done!" 