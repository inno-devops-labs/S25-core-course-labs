# Metrics report

## Prometheus setup

I have succesfully set up Prometheus to monitor my application and logging stack:

![image](https://github.com/user-attachments/assets/84e4afab-bdd2-46e8-b0ee-c92f340282ea)

## Dashboard configuration

### Loki dashboard
![image](https://github.com/user-attachments/assets/4e69a051-1d5e-451e-b4e8-2c532a50a2ea)

### Prometheus dashboard
![image](https://github.com/user-attachments/assets/55e270e8-d994-4f55-93d2-049cfbf0f8f5)

### Configuration updates

I have added a memory limit of 50M to all services to keep them from memory leaking. Furthermore,
I have added logging rotation with 2 max files and a max file size fo 10m.
