from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os 
import sys 
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.log_pipeline import log_pipeline
default_args = {
    "owner":"Hoang",
    "start_date": datetime(year=2025, month=6, day=28)
}

file_postfix = datetime.now().strftime("%Y%m%d")

with DAG(
    dag_id='etl_log_processing',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['log', 'etls']
) as dag:
    extract = PythonOperator(
        task_id = 'log_extraction', 
        python_callable = log_pipeline,
        op_kwargs = {
            'filename': f"{file_postfix}_log"
        }
    )

    extract