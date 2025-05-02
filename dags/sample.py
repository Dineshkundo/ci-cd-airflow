from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the Python function to be called by the task
def print_hello():
    print(f"Hello from Airflow! The time is: {datetime.now()}")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 2),  # Set start date to current date
    'retries': 1,
}

# Initialize the DAG
dag = DAG(
    'sample_dag',  # DAG ID
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',  # Run once a day
    catchup=False,  # Don't backfill
)

# Define the task in the DAG
task1 = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag,
)

task1
