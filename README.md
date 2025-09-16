# Data Engineering

This is a playground repository for data engineering tasks.

## Get started

Initialise and activate the Python virtual environment using [uv](https://docs.astral.sh/uv/)

```sh
uv venv
source .venv/bin/activate
```

Export the Airflow home directory and disable the demo DAGS

```sh
export AIRFLOW_HOME=$(pwd)/airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=False
```

Install Apache Airflow

```sh
AIRFLOW_VERSION=3.0.6
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Run Airflow Standalone which initializes the database, creates a user, and starts all components.

```sh
airflow standalone
```

Access the Airflow UI visiting http://localhost:8080 in your browser and log in with the `admin` username and the generated password that you can copy from the `airflow/simple_auth_manager_passwords.json.generated` file.
