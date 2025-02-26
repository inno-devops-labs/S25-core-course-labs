{{- define "mylibchart.name" -}}
{{- default .Chart.Name .Values.nameOverride }}
{{- end }}

{{- define "mylibchart.labels" -}}
app.kubernetes.io/name: {{ include "mylibchart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
