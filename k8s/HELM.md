# Helm Chart for Moscow Time App

## Chart Structure

```
moscow-time-chart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default values for templates
└── templates/
    ├── deployment.yaml # Template for Kubernetes Deployment
    ├── service.yaml    # Template for Kubernetes Service
    ├── pre-install-hook.yaml  # Pre-install hook
    └── post-install-hook.yaml # Post-install hook
```

## Helm Hooks Implementation

The chart includes both pre-install and post-install hooks:

### Pre-install Hook
- Executes before the main chart installation
- Runs a simple sleep command for 20 seconds
- Has delete policy set to `hook-succeeded`

### Post-install Hook
- Executes after the main chart installation
- Runs a simple sleep command for 20 seconds
- Has delete policy set to `hook-succeeded`

## Cleanup

To uninstall the chart:
```bash
helm uninstall moscow-time
```

## Note on Hook Delete Policy

Both hooks include the annotation `"helm.sh/hook-delete-policy": hook-succeeded` which ensures that:
- Hooks are automatically deleted once they've completed successfully
- This keeps the cluster clean by removing completed hook pods
- Reduces clutter in pod listings and improves cluster management 