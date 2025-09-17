from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'depends_on_past': False,
    'retries': 0,
    'catchup': False
}

with DAG(
  dag_id='download_data_dag',
  description='Download and transform top level domains data',
  start_date=datetime.today(),
  default_args=default_args
  ) as dag:
    task1 = BashOperator(
      task_id='download_data',
      bash_command='pwd'
    )
