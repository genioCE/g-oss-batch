from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG('dbt_build', start_date=datetime(2025,1,1), schedule_interval='@daily', catchup=False) as dag:
    BashOperator(task_id='dbt_build', bash_command='dbt build --profiles-dir /opt/airflow/dbt --project-dir /opt/airflow/dbt')
