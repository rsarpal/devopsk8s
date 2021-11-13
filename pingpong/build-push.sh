#!/bin/bash

docker login
docker build -t rsarpal/k8s_pingpong:latest .
docker push rsarpal/k8s_pingpong:latest