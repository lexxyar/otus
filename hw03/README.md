# Docker

В рекомендациях указано:
> Для сборки рекомендую указать тип платформы linux/amd64:
> docker build --platform linux/amd64 -t tag .

Для MAC OS (m1) при указании данного параметра появляется проблема совместимости и кубер падает на попытке скачать образ

```shell
docker build -t lexxyar/otus-app:v1 .
docker push lexxyar/otus-app:v1
```

# K8S

## Minikube

```shell
minikube start
```

## Ingress

```shell
kubectl create namespace m && helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx && helm repo update && helm install nginx ingress-nginx/ingress-nginx --namespace m -f nginx_ingress.yaml
```

## Apply yaml

```shell
kubectl apply -f k8s/
```

## Add to `/etc/hosts`

```plain text
# Если вписать IP миникуба, то не заработает (MAC OS)
# Нужен именно 127.0.0.1
127.0.0.1 arch.homework
```

## Run tunnel

```shell
sudo minikube tunnel
```

# CURL

```shell
curl http://arch.homework/health
```

# Удаление

```shell
kubectl delete -f k8s/
helm uninstall nginx --namespace m
kubectl delete namespace m
```