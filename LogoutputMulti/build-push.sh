#!/bin/bash

docker login
docker build -t rsarpal/k8s_logoutput:latest reader/.
docker push rsarpal/k8s_logoutput:latest

docker build -t rsarpal/k8s_logoutputwriter:latest Writer/.
docker push rsarpal/k8s_logoutputwriter:latest