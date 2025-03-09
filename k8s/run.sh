cat << EOF > README.md
# Lab 9 Report

## Task 1: Basic Deployment

### Pods and Services Status
\`\`\`bash
kubectl get pods,svc
\`\`\`

\`\`\`
$(kubectl get pods,svc 2>&1)
\`\`\`

### Service URL
\`\`\`bash
minikube service python-app --url
\`\`\`

\`\`\`
$(minikube service python-app --url 2>&1)
\`\`\`

## Task 2: Declarative Manifests

### Applied Manifests
- [deployment.yml](deployment.yml)
- [service.yml](service.yml)

EOF

echo "README.md generated successfully in k8s folder!"