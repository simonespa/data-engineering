from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

with DAG(
  dag_id='top_level_domains',
  description='Download and transform top level domains data',
  start_date=datetime.today(),
  schedule='@daily',
  default_args=default_args
  ) as dag:
    task1 = BashOperator(
      task_id='download_top_level_domains_data',
      bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O ./top-level-domain-names.csv'
    )
