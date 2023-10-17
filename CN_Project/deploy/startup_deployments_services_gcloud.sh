#!/bin/bash

current_dir="$(pwd)"

#deployments
kubectl apply -f "$current_dir/deployments_files_gcloud/api-gateway_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files_gcloud/books_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files_gcloud/ratings_deployment.yaml"
kubectl apply -f "$current_dir/deployments_files_gcloud/users_deployment.yaml"
#kubectl apply -f "$current_dir/deployments_files/mongo_deployment.yaml"

#services
#kubectl apply -f "$current_dir/services_files/api-gateway_service.yaml"
kubectl apply -f "$current_dir/services_files_gcloud/api2_service.yaml"
kubectl apply -f "$current_dir/services_files_gcloud/books_service.yaml"
kubectl apply -f "$current_dir/services_files_gcloud/ratings_service.yaml"
kubectl apply -f "$current_dir/services_files_gcloud/users_service.yaml"
#kubectl apply -f "$current_dir/services_files/mongo_service.yaml"
