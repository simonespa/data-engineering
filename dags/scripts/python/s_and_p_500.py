import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

def transform_data():
  df = pd.read_csv('/opt/airflow/data/s-and-p-500.csv')
  df = df.value_counts('GICS Sector').reset_index().rename(columns={"GICS Sector": "sector"})
  df['date'] = datetime.today().strftime('%Y-%m-%d')
  df.to_csv('/opt/airflow/data/s-and-p-500-transformed.csv', index=False)


def load_data():
  engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
  df = pd.read_csv('/opt/airflow/data/s-and-p-500-transformed.csv')
  df.to_sql("data_s_and_p_500", engine, if_exists='append', index=False)
