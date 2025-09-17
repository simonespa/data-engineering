from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd

def transform_data():
  today = datetime.today().strftime('%Y-%m-%d')
  df = pd.read_csv('/opt/airflow/data/top-level-domains.csv')
  generic_type_df = df.query('Type == "generic"')[['Domain']]
  generic_type_df['Date'] = today
  generic_type_df.to_parquet(f'/opt/airflow/data/top-level-domains-{today}.parquet', index=False, compression='brotli')

with DAG(
  dag_id='top_level_domains',
  description='Download and transform data from the top-level domain names dataset',
  start_date=datetime.today(),
  schedule='@daily',
  default_args={
    'depends_on_past': False,
    'retries': 0,
    'catchup': False
  }) as dag:
    task1 = BashOperator(
      task_id='download_data',
      bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O /opt/airflow/data/top-level-domains.csv'
    )

    task2 = PythonOperator(
      task_id='transform_data',
      python_callable=transform_data
    )

    task1 >> task2
