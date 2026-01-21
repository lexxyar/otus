# Installation
## Postgres
```shell
helm install my-postgres \
  oci://registry-1.docker.io/cloudpirates/postgres \
  --namespace default \
  --create-namespace \
  -f postgres-values.yaml
```
## Kubectl
```shell
kubectl apply -f k8s
```

