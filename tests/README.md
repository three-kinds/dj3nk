# Test

## 1. Deploy redis.

```shell
docker run -d \
  --name=redis \
  -p 6379:6379 \
  redis:7

```

## 2. Run tests.

```shell
make init
make coverage
make test

```