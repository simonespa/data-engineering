from datetime import datetime, timedelta
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

with DAG(
    dag_id='one_task_dag',
    description='A one task Airflow DAG',
    schedule=timedelta(days=1),
    start_date=datetime.today()
) as dag:
    task1 = BashOperator(
        task_id='one_task',
        bash_command='echo "Hello World"',
    )

    task1
