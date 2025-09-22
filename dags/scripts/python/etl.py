import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

def transform_data():
  today = datetime.today().strftime('%Y-%m-%d')
  df = pd.read_csv('/opt/airflow/data/top-level-domains.csv')
  generic_type_df = df.query('Type == "generic"')[['Domain']]
  generic_type_df['Date'] = today
  generic_type_df.columns = [column.lower() for column in generic_type_df.columns]
  generic_type_df.to_parquet(f'/opt/airflow/data/top-level-domains-{today}.parquet', index=False, compression='brotli')

def load_data():
  engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
  today = datetime.today().strftime('%Y-%m-%d')
  df = pd.read_parquet(f'/opt/airflow/data/top-level-domains-{today}.parquet')
  df.to_sql("top_level_domains", engine, if_exists='append', index=False)
