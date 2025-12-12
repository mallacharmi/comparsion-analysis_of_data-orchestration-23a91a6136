# dagster_project/etl_dagster_job.py
import os
import sys
from dagster import job, op, RetryPolicy

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

import etl.core as core


@op(
    config_schema={
        "input_path": str,
        "output_path": str,
        "blocked_countries": list,
        "simulate_failure": bool,
    },
    retry_policy=RetryPolicy(max_retries=2, delay=10),  # <-- FIXED (no delay_seconds)
)
def run_etl_op(context):
    conf = context.op_config

    df = core.extract_csv(conf.get("input_path"))
    transformed = core.transform_events(
        df,
        conf.get("blocked_countries"),
        conf.get("simulate_failure"),
    )
    core.load_to_parquet_partitioned(transformed, conf.get("output_path"))

    return True


@job
def etl_dagster_job():
    run_etl_op()
