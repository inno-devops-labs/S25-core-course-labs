# Logging report

## Applications

Both applications run and their outputs are forwarded using Promtail to Loki, which 
then serves them to Grafana

![image](https://github.com/user-attachments/assets/4d7c3d7c-0db5-4e67-82a0-a5fce7825b08)
![image](https://github.com/user-attachments/assets/73bbbcd5-5750-4ac8-aa51-9516c6863b70)

## Promtail

Promtail is a log collection tool that can collect output streams from multiple
containers and forward them all to our log storage, which is Loki

![image](https://github.com/user-attachments/assets/91c3a77f-028b-466c-9343-8a8c6575159b)


## Loki

Loki is a system that can accept, store, and give out logging information. In our
case, it gets its' data from Promtail, and allows Grafana access to it.

![image](https://github.com/user-attachments/assets/ca8e4e8b-a623-4455-99ec-aa66dce1de79)

## Grafana

Grafana is a visualising tool that can collect logs from multiple different storage
systems, in our case only Loki, and display them in a lot of different forms. It is
very flexible, so it is used a lot.

![image](https://github.com/user-attachments/assets/08038d9c-84b2-4181-aa2d-a14728b324ad)
