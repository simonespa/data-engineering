# Data Engineering

This is a playground repository for data engineering tasks.

## Get started

Fetch the `docker-compose.yaml` file

```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.6/docker-compose.yaml'
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

Read more at https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
