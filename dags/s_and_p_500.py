from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from scripts.python.s_and_p_500 import transform_data, load_data

with DAG(
  dag_id='S_and_P_500',
  description='Extract, transform and load data from the S&P 500 dataset',
  start_date=datetime.today(),
  schedule='@daily',
  default_args={
    'depends_on_past': False,
    'retries': 0,
    'catchup': False
  }) as dag:
    extract = BashOperator(
      task_id='extract',
      bash_command='wget -c https://datahub.io/core/s-and-p-500-companies/r/constituents.csv -O /opt/airflow/data/s-and-p-500.csv'
    )

    transform = PythonOperator(
      task_id='transform',
      python_callable=transform_data
    )

    load = PythonOperator(
      task_id='load',
      python_callable=load_data
    )

    extract >> transform >> load
