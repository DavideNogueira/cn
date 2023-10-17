#!/bin/bash

kubectl delete deployment grafana
kubectl delete deployment prometheus-deployment
kubectl delete deployment locust-master
kubectl delete deployment locust-worker

kubectl delete service grafana
kubectl delete service prometheus-svc
kubectl delete service locust-master
kubectl delete service locust-service

kubectl delete configmap prometheus-cm