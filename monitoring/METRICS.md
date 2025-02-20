# Metrics

## Displayed metrics in prometheus

I used cadvisor to take metrics from containers, so that webapp containers will not be changed directly.

![img.png](images/prom.png)

## Dashboards

I easily can create dashboards like that:

![img_1.png](images/dashboard.png)

## Additional practices

- Log rotation mechanisms: 3 log files of maximum 10Mb each;

- Memory limits: 512Md maximum per application.