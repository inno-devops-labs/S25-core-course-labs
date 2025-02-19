# Monitoring Stack

---

## Grafana

* Mostly UI of the entire metrics system - visualise and prompts the necessary (for users) data
* Fetch the datastream from the sources like `Loki`

## Loki

* Log Storage
* Query Engine
* Mostly a database for aggregated logs from all the sources (applications)

## Promtail

* Scanner for logs (mostly - collector)
* Fetch logs from the specified files and send them into the log storages (i.e. `Loki`)

## Python & Java Application

* Two different application with logs that can be followed by the entire metrics stack

---

## Troubleshooting

It was so hard to understand that:

A) There is no ability to fetch logs from Docker containers in the windows+wsl2 system
B) There is no correct permissions to fetch logs from the Docker daemon that was installed by the ansible / terraform (at
least I didn't find)

So, I create new VM and install docker by hands. There is a result:

---

## Grafana with Loki

![img.png](res/grafana_loki.png)

## Accessible labels

![img_1.png](res/labels.png)

## Python Application Logs

![img_2.png](res/python_app_logs.png)

## Java Application Logs (fetched from containers)

![img_4.png](res/java_app_logs.png)

## All `docker-compose` container logs

![img_3.png](res/all_logs.png)
