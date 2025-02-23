# Logging report

## Promtail

Promtail is a log collection tool that can collect output streams from multiple
containers and forward them all to our log storage, which is Loki

## Loki

Loki is a system that can accept, store, and give out logging information. In our
case, it gets its' data from Promtail, and allows Grafana access to it.

## Grafana

Grafana is a visualising tool that can collect logs from multiple different storage
systems, in our case only Loki, and display them in a lot of different forms. It is
very flexible, so it is used a lot.
