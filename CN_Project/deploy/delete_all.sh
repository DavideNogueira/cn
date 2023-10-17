#!/bin/bash
#delete all

#deployments
kubectl delete deployment api-gateway
kubectl delete deployment books
kubectl delete deployment ratings
kubectl delete deployment users
kubectl delete deployment mongo

#services
#kubectl delete service api-gateway
kubectl delete service api-gateway-service
kubectl delete service books
kubectl delete service ratings
kubectl delete service users
kubectl delete service mongo

#hpa
kubectl delete HorizontalPodAutoscaler api-gateway-hpa
kubectl delete HorizontalPodAutoscaler users-hpa
kubectl delete HorizontalPodAutoscaler books-hpa
kubectl delete HorizontalPodAutoscaler ratings-hpa