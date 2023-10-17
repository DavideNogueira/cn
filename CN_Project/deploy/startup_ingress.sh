#!/bin/bash

current_dir="$(pwd)"

kubectl apply -f "$current_dir/ingress/controller.yaml"

kubectl wait --namespace ingress-nginx \
--for=condition=ready pod \
--selector=app.kubernetes.io/component=controller \
--timeout=120s

kubectl apply -f "$current_dir/ingress/ingress.yaml"