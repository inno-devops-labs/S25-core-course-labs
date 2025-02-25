{{- define "library-chart.labels" -}}
app: {{ .Values.appName }}
version: {{ .Values.appVersion }}
{{- end }}
