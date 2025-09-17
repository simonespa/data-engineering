# Data Engineering

This is a playground repository for data engineering tasks.

## Get started

This installation assumes familiarity with [Docker](https://docs.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/). Make sure to have [Docker Community Edition (CE)](https://docs.docker.com/engine/install/) and [Docker Compose v2](https://docs.docker.com/compose/install/) installed first.

Build the custom image

```sh
docker compose build
```

Initialize the database and create the default account with username `airflow` and password `airflow`

```sh
docker compose up airflow-init
```

Start all services

```sh
docker compose up
```

Access the webserver at http://localhost:8080

## References

- [Customise the Airflow Docker image](https://airflow.apache.org/docs/docker-stack/build.html)
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
