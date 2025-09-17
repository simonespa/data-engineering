from datetime import date
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd

def transform_data():
  today = date.today().strftime('%Y-%m-%d')
  df = pd.read_csv('/opt/airflow/data/top-level-domain-names.csv')
  generic_type_df = df.query('Type == "generic"')
  generic_type_df['Date'] = today
  generic_type_df.to_csv(f'/opt/airflow/data/generic_top-level-domain-names_{today}.csv', index=False)

with DAG(
  dag_id='data_transformation',
  description='Download and transform data',
  start_date=date.today().strftime('%Y-%m-%d'),
  default_args={
    'depends_on_past': False,
    'retries': 0,
    'catchup': False
  }) as dag:
    task1 = BashOperator(
      task_id='download_data',
      bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O /opt/airflow/data/top-level-domain-names.csv'
    )

    task2 = PythonOperator(
      task_id='transform_data',
      python_callable=transform_data
    )

    task1 >> task2
