from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'hello_world',
    description='A simple hello world DAG',
    schedule_interval='@daily',  # Daily schedule
    start_date=datetime(2025, 1, 2),
    catchup=False,
)

# Define the task
hello_task = DummyOperator(
    task_id='hello_task',
    dag=dag,
)

# This will ensure the task runs in sequence
hello_task
