#!/bin/bash

current_dir="$(pwd)"

docker rmi $(docker images | grep 'api_gateway')
docker rmi $(docker images | grep 'ratings')
docker rmi $(docker images | grep 'books')
docker rmi $(docker images | grep 'users')

docker build -f "$current_dir/app/api/Dockerfile" -t api_gateway "$current_dir/app/api/"
docker build -f "$current_dir/app/microservices/books/Dockerfile" -t books "$current_dir/app/microservices/books/"
docker build -f "$current_dir/app/microservices/users/Dockerfile" -t users "$current_dir/app/microservices/users/"
docker build -f "$current_dir/app/microservices/ratings/Dockerfile" -t ratings "$current_dir/app/microservices/ratings/"

docker tag api_gateway davide1234/api_gateway
docker tag users davide1234/users
docker tag books davide1234/books
docker tag ratings davide1234/ratings

docker push davide1234/api_gateway
docker push davide1234/users
docker push davide1234/books
docker push davide1234/ratings

docker rmi $(docker images | grep 'api_gateway')
docker rmi $(docker images | grep 'ratings')
docker rmi $(docker images | grep 'books')
docker rmi $(docker images | grep 'users')
