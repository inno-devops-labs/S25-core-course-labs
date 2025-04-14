#! /bin/bash

kubectl apply -f quote-deployment.yml
kubectl apply -f quote-service.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml