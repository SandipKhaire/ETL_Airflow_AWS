from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from User_ETL import user_detail_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 13),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'User_dag',
    default_args=default_args,
    description='User DAG with ETL process!',
    schedule_interval='*/5 * * * *',
)

run_etl = PythonOperator(
    task_id='complete_user_etl',
    python_callable=user_detail_etl,
    dag=dag, 
)

run_etl