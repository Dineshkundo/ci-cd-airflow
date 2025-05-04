from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='print_public_ip',
    start_date=days_ago(1),
    schedule_interval=None,  # Manual trigger
    catchup=False,
    tags=["debug", "network"],
) as dag:

    print_ip = BashOperator(
        task_id='get_public_ip',
        bash_command='curl -s ifconfig.me || curl -s https://api.ipify.org',
    )

    print_ip
