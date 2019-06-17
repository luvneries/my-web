#!/usr/bin/env bash

docker build -t luvneries/api-server:latest -t luvneries/api-server:$SHA -f ./flask-server/Dockerfile ./flask-server
docker push luvneries/api-server:latest
docker push luvneries/api-server:$SHA
kubectl apply -f k8s
kubectl set image deployments/flask-deployment flask-container=luvneries/api-server:$SHA