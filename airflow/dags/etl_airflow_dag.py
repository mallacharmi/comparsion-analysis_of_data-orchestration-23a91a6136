from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import functions from your ETL module
from etl.core import extract_csv, transform_events, load_to_parquet_partitioned

default_args = {"owner": "airflow"}

with DAG(
    dag_id="etl_airflow_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=True,
    default_args=default_args,
) as dag:

    def _extract(input_path: str, ti=None, **kwargs):
        df = extract_csv(input_path)
        ti.xcom_push(key="extracted_df", value=df.to_json(orient="split"))

    def _transform(blocked_countries, simulate_failure, ti=None, **kwargs):
        import pandas as pd
        data_json = ti.xcom_pull(key="extracted_df")
        df = pd.read_json(data_json, orient="split")
        transformed = transform_events(df, blocked_countries, simulate_failure)
        ti.xcom_push(key="transformed_df", value=transformed.to_json(orient="split"))

    def _load(output_path: str, ti=None, **kwargs):
        import pandas as pd
        data_json = ti.xcom_pull(key="transformed_df")
        df = pd.read_json(data_json, orient="split")
        load_to_parquet_partitioned(df, output_path)

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=_extract,
        op_kwargs={"input_path": "/opt/airflow/dags/synthetic_events.csv"},
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=_transform,
        op_kwargs={"blocked_countries": [], "simulate_failure": False},
        retries=2,
        retry_delay=timedelta(seconds=10),
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=_load,
        op_kwargs={"output_path": "/opt/airflow/output_airflow"},
    )

    extract_task >> transform_task >> load_task
