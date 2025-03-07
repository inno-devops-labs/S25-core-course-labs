{{- define "common.labels" -}}
app: {{ .Chart.Name }}
release: {{ .Release.Name }}
{{- end }}
