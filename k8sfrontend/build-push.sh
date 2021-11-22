#!/bin/bash

docker login
docker build -t rsarpal/k8s_k8sfrontend:latest .
docker push rsarpal/k8s_k8sfrontend:latest