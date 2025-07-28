# CONTRIBUTING

## How to build docker image

```
docker-buildx build -t fibs-app .
```

## How to run docker locally

```
docker run -p 8080:5000 -w /app -v "$(pwd):/app" fibs-app sh -c "flask run --host 0.0.0.0"
```
