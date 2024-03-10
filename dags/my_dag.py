from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('my_dag', default_args=default_args, schedule_interval=timedelta(days=1))

start = DummyOperator(task_id='start', dag=dag)

end = DummyOperator(task_id='end', dag=dag)

start >> end

