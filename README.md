# Data Engineering

This is a playground repository for data engineering tasks.

## Get started

Export the Airflow home environment variable and get the python version

```
export AIRFLOW_HOME=$(pwd)/airflow
PYTHON_VERSION=$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)
```

Install the python environment with the required packages and python version manually

```
conda create --name data-engineering python=${PYTHON_VERSION} -y
conda activate data-engineering
conda install apache-airflow -y
conda env export > environment.yaml
```

Or install the python environment with the required packages and python version from the YAML file

```
conda env create -f environment.yaml
```

Initialise the SQLlite database for Airflow

```
airflow db migrate
```

Change the `load_examples` settings under the `[core]` section in `airflow/airflow.cfg` to `False`.

Start the server, scheduler and trigger in daemon mode

```
airflow api-server --port 8080 -D
airflow scheduler -D
airflow triggerer -D
```

Start the dag-processor in the foreground (in daemon mode it doesn't show the dags in the UI).

```
airflow dag-processor
```

Go to http://localhost:8080, then copy the admin password from the `simple_auth_manager_passwords.json.generated` to login with the username `admin`.
