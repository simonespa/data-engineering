FROM apache/airflow:3.0.6
USER root
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
          wget \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
RUN pip install --no-cache-dir "apache-airflow==3.0.6" apache-airflow-providers-postgres apache-airflow-providers-common-sql
