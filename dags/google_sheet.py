import datetime
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from utils import full_pipeline

default_args = {
    'owner': 'victor',
    'retries': 2
   
}


new = DAG(
    dag_id="google_job",
    description="Fetching the data from the googlesheet",
    schedule="@daily",
    start_date=datetime(2025,6,11),
    catchup=False,
    default_args=default_args
)

task1 = PythonOperator(
    dag=new,
    python_callable=full_pipeline,
    task_id="task1"
)

task1