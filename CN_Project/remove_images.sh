#!/bin/bash

docker rmi $(docker images | grep 'api_gateway')
docker rmi $(docker images | grep 'ratings')
docker rmi $(docker images | grep 'books')
docker rmi $(docker images | grep 'users')
#docker rmi $(docker images | grep 'davide1234/mongo')