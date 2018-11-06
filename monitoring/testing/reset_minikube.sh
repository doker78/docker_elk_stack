#!/usr/bin/env bash

set -ex

minikube config set cpus 2
minikube config set memory 2048
minikube config view
minikube delete || true
minikube start --vm-driver ${1-"virtualbox"}
