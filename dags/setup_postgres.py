from datetime import datetime
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sdk import DAG

with DAG(
  dag_id='setup_postgres',
  description='Setup the Postgres database by adding the required table for analysis',
  start_date=datetime.today(),
  schedule=None,
  default_args={
  'depends_on_past': False,
  'retries': 0,
  'catchup': False
  }) as dag:
    task = SQLExecuteQueryOperator(
      task_id="create_data_table",
      conn_id="postgres",
      sql="./scripts/sql/setup_postgres.sql"
    )
