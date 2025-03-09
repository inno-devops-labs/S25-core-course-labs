NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-56f7689b79-w9s9x   1/1     Running   0          10m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/my-app       NodePort    10.101.157.95   <none>        80:30321/TCP   9m45s



NAME                         READY   STATUS    RESTARTS   AGE
pod/my-app-8c95b7794-fbsrb   1/1     Running   0          55s
pod/my-app-8c95b7794-lhh7p   1/1     Running   0          55s
pod/my-app-8c95b7794-wqj5k   1/1     Running   0          55s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/my-app       NodePort    10.102.40.194   <none>        80:30462/TCP   55s


|-----------|--------|-------------|---------------------------|
| NAMESPACE |  NAME  | TARGET PORT |            URL            |
|-----------|--------|-------------|---------------------------|
| default   | my-app |          80 | http://192.168.49.2:30462 |
|-----------|--------|-------------|---------------------------|
🎉  Opening service default/my-app in default browser...
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:39089 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...

![img_1.png](img_1.png)

✋  Stopping tunnel for service kubernetes.

--- Bonus

after 
```bash
curl -I http://my-app.local
```
HTTP/1.1 503 Service Temporarily Unavailable
Date: Sun, 09 Mar 2025 19:56:45 GMT
Content-Type: text/html
Content-Length: 190
Connection: keep-alive

after
```bash
curl -I http://my-java.local
```
HTTP/1.1 200 OK
Date: Sun, 09 Mar 2025 19:59:06 GMT
Content-Type: text/html
Content-Length: 45
Connection: keep-alive
Last-Modified: Mon, 11 Jun 2007 18:53:14 GMT
ETag: "2d-432a5e4a73a80"
Accept-Ranges: bytes
