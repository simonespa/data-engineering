from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from scripts.python.etl import transform_data, load_data

with DAG(
  dag_id='top_level_domains',
  description='Extract, transform and load data from the top-level domain names dataset',
  start_date=datetime.today(),
  schedule='@daily',
  default_args={
    'depends_on_past': False,
    'retries': 0,
    'catchup': False
  }) as dag:
    task1 = BashOperator(
      task_id='extract',
      bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O /opt/airflow/data/top-level-domains.csv'
    )

    task2 = PythonOperator(
      task_id='transform',
      python_callable=transform_data
    )

    task3 = PythonOperator(
      task_id='load',
      python_callable=load_data
    )

    task1 >> task2 >> task3
