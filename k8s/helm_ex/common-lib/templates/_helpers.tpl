# common-lib/templates/_helpers.tpl
{{- define "common-lib.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
env: production
{{- end }}
