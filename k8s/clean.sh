#! /bin/bash

kubectl delete -f ingress.yml
kubectl delete -f quote-deployment.yml
kubectl delete -f quote-service.yml
kubectl delete -f deployment.yml
kubectl delete -f service.yml