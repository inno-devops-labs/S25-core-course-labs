# Lab 12: Bonus Task - ConfigMap via Environment Variables

## Overview

This document provides documentation for the bonus task implementation of ConfigMap via environment variables in our Node.js application.

## 1. Upgraded Bonus App with Persistence

I've implemented persistence logic in the Node.js application similar to what was done in the Python app:

- Added a counter to track the number of visits to the application
- Created functions to read and write the visit count to a file
- Added a `/visits` endpoint to display the recorded visits
- Updated the application to increment the counter on each visit to the home page

## 2. ConfigMap via Environment Variables

I've implemented a ConfigMap that provides environment variables to the Node.js application using the `envFrom` property:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "nodejs-app.fullname" . }}-config
  labels:
    {{- include "nodejs-app.labels" . | nindent 4 }}
data:
  NODE_ENV: "production"
  APP_NAME: "nodejs-moscow-time"
  APP_VERSION: "1.0.0"
  TIMEZONE: "Europe/Moscow"
  LOG_LEVEL: "info"
  REFRESH_INTERVAL: "60"
  MAX_VISITS: "10000"
```

## 3. Deployment Configuration

I've updated the deployment template to use the ConfigMap via environment variables:

```yaml
envFrom:
  - configMapRef:
      name: {{ include "nodejs-app.fullname" . }}-config
```

I've also added volume mounts for the visits file to ensure persistence:

```yaml
volumeMounts:
  - name: visits-volume
    mountPath: /app/visits

volumes:
  - name: visits-volume
    emptyDir: {}
```

## 4. Verification

After deploying the Helm chart, I'll verify the ConfigMap implementation with the following commands:

```bash
# Deploy the Helm chart
helm install nodejs-app ./k8s/nodejs-app

kubectl get po

NAME                                    READY   STATUS    RESTARTS       AGE
nodejs-app-84d8456744-r4pkg             1/1     Running   0              3m42s
python-app-559c7b7c68-m56xq             1/1     Running   0              7m31s
vault-0                                 0/1     Running   1 (18m ago)    3d22h
vault-agent-injector-669f58d9b5-pl2q9   1/1     Running   1 (3d4h ago)   3d22h

kubectl exec nodejs-app-84d8456744-r4pkg -- env | grep -E 'NODE_ENV|APP_NAME|APP_VERSION|TIMEZONE|LOG_LEVEL|REFRESH_INTERVAL|MAX_VISITS'

LOG_LEVEL=info
MAX_VISITS=10000
NODE_ENV=production
REFRESH_INTERVAL=60
TIMEZONE=Europe/Moscow
APP_NAME=nodejs-moscow-time
APP_VERSION=1.0.0
```

## 5. Benefits of Using ConfigMap via Environment Variables

- Simple and familiar pattern for application configuration
- No need to modify application code to read from files
- Environment variables are a standard way to configure applications in containerized environments
- Easy to update configuration without rebuilding container images
- Works well with applications that already use environment variables for configuration
