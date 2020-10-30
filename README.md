# IAM

This is an identity management microservice using Django in back-end and PostgreSQL for database.

## Installation

IAM requires Docker and docker-compose to run. After creating an env file; build the image and start the server.

```sh
cp src/iam/.env.dev src/iam/.env
make build
make up
```

To verify the success of the installation, send a request with curl:

```sh
curl http://localhost:8000/
```
