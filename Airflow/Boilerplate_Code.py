from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator   # optional
# from airflow.operators.dummy import DummyOperator  # optional


# -------------------------
# Step 1: Define default args
# -------------------------

default_args = {
    'owner': 'Kabir',                      # e.g. 'kabir'
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,                     # e.g. 1 or 2 if retrying
    'retry_delay': timedelta(minutes=1),
}


# -------------------------
# Step 2: Define DAG
# -------------------------

with DAG(
    dag_id='practice_1',                        # e.g. 'my_etl_dag'
    description='learning airflow',                   # short purpose
    default_args=default_args,
    schedule_interval='',             # define a crone job
    start_date=datetime(2025, 10,23), # e.g. datetime(2025, 10, 1)
    catchup=False,                    # usually False for testing                        # optional: ['etl', 'project_name']
) as dag:


    # -------------------------
    # Step 3: Define Python functions
    # -------------------------

    