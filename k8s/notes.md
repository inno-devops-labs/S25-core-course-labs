-1.1 
> minikube delete && minikube start

> kubectl create secret generic app-secret \
  --from-literal=MY_PASS=admin123 \
  --namespace=default

  > kubectl get secret app-secret -o yaml

  > echo "YWRtaW4xMjM=" | base64 -d


  - 1.3
  > helm create mychart

  > cd mychart/templates
rm -rf hpa.yaml ingress.yaml service.yaml serviceaccount.yaml tests/ NOTES.txt
cd ..
gedit values.yaml 
 cat values.yaml 
 gedit templates/deployment.yaml
 cat templates/deployment.yaml


 touch templates/secrets.yaml
gedit templates/secrets.yaml
 cat templates/secrets.yaml
cd ..

 helm install demo ./mychart

 kubectl get pods -l app.kubernetes.io/instance=demo
 kubectl exec <POD_NAME> -- printenv | grep MY_PASSWORD