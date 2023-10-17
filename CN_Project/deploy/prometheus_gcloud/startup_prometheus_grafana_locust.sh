#!/bin/bash

current_dir="$(pwd)"

kubectl apply -f "grafana-deployment.yaml"
kubectl apply -f "grafana-service.yaml"
kubectl create configmap prometheus-cm --from-file prometheus-cm.yaml
kubectl apply -f "prometheus.yaml"

kubectl create -f "$current_dir/locust/nodeport.yaml" -f "$current_dir/locust/scripts-cm.yaml" -f "$current_dir/locust/master-deployment.yaml" -f "$current_dir/locust/service.yaml" -f "$current_dir/locust/slave-deployment.yaml"