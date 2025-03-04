# K8S (finally)

---

## `kubectl get pods,svc`

* Output is mostly the same for the `.yaml` specification, and in-console configuration

![img.png](res/pods_svc.png)

---

## `minikube service --all`

![img.png](res/service_all_minikube.png)

### Python Application

![img.png](res/python_app_raw_service.png)

### Java Application

![img.png](res/java_app_raw_service.png)

---

## Creating ingresses

* Because I use windows (my bad honestly), I need to open terminal opened and `curl` from another terminal

### `minikube tunnel`

![img.png](res/minikube_tunnel.png)

### Python Application

* `curl --resolve "watch.example.com:80:127.0.0.1" -i http://watch.example.com`; Host is written by me in
  the `ingress.yaml` files

![img.png](res/python_app_curl_access.png)

### Java Application

* `curl --resolve "vacation-calculator.example.com:80:127.0.0.1" -i http://vacation-calculator.example.com`; Host is
  written by me in the `ingress.yaml` files

![img.png](res/java_app_curl_access.png)
