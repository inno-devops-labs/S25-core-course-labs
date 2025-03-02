{{- define "custom.labels" -}}
app: {{ .Chart.Name }}
environment: production
managed-by: Helm
{{- end -}}
