# Kubernets

## Start cluster

After starting a cluster, we can check its status:
```
minikube status
```
![minikube status](./readme_images/minikube_status.png)


## Create a deployment and a service with a command

![kuberctl create](./readme_images/py/deploy_expose.png)

Check `pods` and `svc`

```
kubectl get pods,svc
```
![kubectl get](./readme_images/py/get_svc_1.png)

### After that, clean up

![clean up](./readme_images/py/clean_up_1.png)

## Create a deployment and a service with a file


To apply a file we need to run a command
```
kubectl apply -f <name>.yml
```

![apply -f](./readme_images/py/apply.png)

```
kubectl get pods,svc
```
![kubectl get](./readme_images/py/get_svc_2.png)


## Verify 

``` 
minikube service --all
```

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | python-service |        8080 | http://192.168.49.2:30824 |
|-----------|----------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/python-service in default browser...
🏃  Starting tunnel for service kubernetes.
update.go:85: cannot change mount namespace according to change mount (/run/user/1000/doc/by-app/snap.firefox /run/user/1000/doc none bind,rw,x-snapd.ignore-missing 0 0): cannot inspect "/run/user/1000/doc": lstat /run/user/1000/doc: permission denied
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:42455 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
update.go:85: cannot change mount namespace according to change mount (/run/user/1000/doc/by-app/snap.firefox /run/user/1000/doc none bind,rw,x-snapd.ignore-missing 0 0): cannot inspect "/run/user/1000/doc": lstat /run/user/1000/doc: permission denied
Gtk-Message: 20:52:03.196: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Gtk-Message: 20:52:03.196: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
[49288, Main Thread] WARNING: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/49288/root: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:49288): Gdk-WARNING **: 20:52:03.232: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/49288/root
[49366, Main Thread] WARNING: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/49366/root: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:49366): Gdk-WARNING **: 20:52:03.233: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/49366/root

```

![app view](./readme_images/py/app.png)


## Clean Up
```
kubectl delete -f <name>.yml
```

![clean up](./readme_images/py/clean_up_2.png)


# Bonus

## Deployment and service for a bonus app

Do the same steps for deployment

![apply](./readme_images/js/apply.png)

![get pods svc](./readme_images/js/get_svc.png)

```
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | js-service |        8081 | http://192.168.49.2:30437 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/js-service in default browser...
🏃  Starting tunnel for service kubernetes.
update.go:85: cannot change mount namespace according to change mount (/run/user/1000/doc/by-app/snap.firefox /run/user/1000/doc none bind,rw,x-snapd.ignore-missing 0 0): cannot inspect "/run/user/1000/doc": lstat /run/user/1000/doc: permission denied
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:43181 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
update.go:85: cannot change mount namespace according to change mount (/run/user/1000/doc/by-app/snap.firefox /run/user/1000/doc none bind,rw,x-snapd.ignore-missing 0 0): cannot inspect "/run/user/1000/doc": lstat /run/user/1000/doc: permission denied
Gtk-Message: 21:05:42.508: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Gtk-Message: 21:05:42.508: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
[56705, Main Thread] WARNING: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/56705/root: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:56705): Gdk-WARNING **: 21:05:42.522: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/56705/root
[56621, Main Thread] WARNING: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/56621/root: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:56621): Gdk-WARNING **: 21:05:42.522: Failed to read portal settings: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Portal operation not allowed: Unable to open /proc/56621/root

```

![app view](./readme_images/js/app.png)

![clean up](./readme_images/js/clean_up.png)

## Curl

I will use `health` endpoint
![curl health](./readme_images/curl_1.png)

We can see that both websites returned `OK` (first is `python-app`, 
second is `js-app`)

The output without using endpoint `health`

![curl](./readme_images/curl_2.png)


## Ingress

Configured `ingress` and enabled it

![ingress enable](./readme_images/ingress.png)

