#!/bin/bash

docker login
docker build -t rsarpal/k8s_k8sproj:latest .
docker push rsarpal/k8s_k8sproj:latest