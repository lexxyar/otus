# Installation
## Postgres
```shell
helm install my-postgres \
  oci://registry-1.docker.io/cloudpirates/postgres \
  --namespace default \
  --create-namespace \
  -f postgres-values.yaml
```

## minikube
```shell
minikube start
```

## Kubectl
```shell
kubectl apply -f k8s
```

# Docker
```shell
docker build -t lexxyar/otus-app:v1.3 .
docker push lexxyar/otus-app:v1.3
```

