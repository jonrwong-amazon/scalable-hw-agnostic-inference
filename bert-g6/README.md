# DistilBERT base uncased finetuned SST-2 on EKS with Nvidia GPU's

## Deploy BERT

* This file aims to deploy BERT onto an EKS pod. We will be using the envsubst command which replaces all variables in this file with environment variables, so make sure that the correct variables are set and align with the what will be replaced in the file.
```
cat bert-g6-deploy.yaml | envsubst | kubectl apply -f -
```

## Deploy Service

* We are deploying a service file called bert-gpu-svc.yaml focused on exposing an application running in our cluster. We define the service to expose port 80, and the pods to have a targetPort of 8000, meaning that the service will route traffic from port 80 on the service to port 8000 on the pods that match the label app:bert-gpu. 
```
kubectl apply -f bert-g6-svc.yaml
```

## Deploy Ing

* We will be deploying an ingress file called bert-gpu-ing.yaml which focuses on exposing HTTP routes from outside the cluster to services within the cluster. 
```
kubectl apply -f bert-g6-ing.yaml
```