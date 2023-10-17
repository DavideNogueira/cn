#!/bin/bash

current_dir="$(pwd)"

#deployments
kubectl apply -f "$current_dir/deployments_files/api-gateway_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files/books_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files/ratings_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files/users_deployment.yaml"
#kubectl apply -f "$current_dir/deployments_files/mongo_deployment.yaml"

#services
#kubectl apply -f "$current_dir/services_files/api-gateway_service.yaml"
kubectl apply -f "$current_dir/services_files/api2_service.yaml"
kubectl apply -f "$current_dir/services_files/books_service.yaml"
kubectl apply -f "$current_dir/services_files/ratings_service.yaml"
kubectl apply -f "$current_dir/services_files/users_service.yaml"
#kubectl apply -f "$current_dir/services_files/mongo_service.yaml"
