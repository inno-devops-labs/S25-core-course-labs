#!/bin/bash

cat << EOF > HELM.md
# Lab 10 Report

## Task 1: Helm Chart

### Pods and Services
\`\`\`bash
kubectl get pods,svc -l app.kubernetes.io/instance=python-app
\`\`\`

\`\`\`
$(kubectl get pods,svc -l app.kubernetes.io/instance=python-app)
\`\`\`

## Task 2: Hooks

### Hook Execution Status
Hooks were successfully executed and automatically deleted according to the \`hook-delete-policy\`.

#### Execution Confirmation:
\`\`\`bash
helm get hooks python-app
\`\`\`

\`\`\`
$(helm get hooks python-app 2>&1)
\`\`\`
EOF

echo "HELM.md updated!"