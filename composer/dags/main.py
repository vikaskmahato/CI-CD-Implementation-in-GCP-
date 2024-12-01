from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print():
    print("This is a test DAG.!")


with DAG(
    dag_id='test_dag_composer',
    default_args=default_args,
    description='A sample test DAG for Cloud Composer',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    start_task = DummyOperator(
        task_id='start_task',
    )

    python_task = PythonOperator(
        task_id='print_task',
        python_callable=print,
    )

    start_task >> python_task
