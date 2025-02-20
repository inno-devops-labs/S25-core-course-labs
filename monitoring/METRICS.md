![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab8/monitoring/im1.jpg)
![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab8/monitoring/im3.jpg)
![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/blob/Lab8/monitoring/im2.jpg)

Configurations of the grafana, prometheus or promtail are good. There are no metrics on screenshots because my application moscow-time-app, what we created on the first lab has no mechanism to send these metrics.  
So, there was not the task to make the mechanism, but to build configurations.

## Log rotation and so on
Configuration of all services was enhanced in the docker-compose.yml file by adding two key improvements: log rotation and memory limits. Log rotation was implemented to manage disk space usage by limiting the size of individual log files and the total number of log files stored for each service. This prevents logs from consuming too much disk space, which could otherwise lead to system performance issues. Additionally, memory limits were defined for each container to ensure that no single service can use an excessive amount of memory, which helps maintain balanced resource allocation and prevents any one component from impacting the stability of the entire stack.
