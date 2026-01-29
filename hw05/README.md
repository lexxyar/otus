Reinstall (if needed) ingress nginx and apply metrics

```shell
helm uninstall nginx -n m
helm repo update
helm install nginx ingress-nginx/ingress-nginx -n nginx -f ./nginx_ingress.yaml --create-namespace
```

Rebuild app docker image
```shell
docker build -t lexxyar/otus-app:v1.6 .
docker push lexxyar/otus-app:v1.6
```