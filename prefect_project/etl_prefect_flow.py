# prefect_project/etl_prefect_flow.py

import argparse
import sys
import os
from datetime import timedelta
from typing import List, Optional

# ⭐ FIX 1: Add project root to Python path automatically
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)

# ⭐ FIX 2: Correct import from shared ETL module
from etl.core import extract_csv, transform_events, load_to_parquet_partitioned

from prefect import flow, task


@task(name="extract_task")
def extract_task(input_path: str):
    return extract_csv(input_path)


@task(name="transform_task", retries=2, retry_delay_seconds=10)
def transform_task(df, blocked_countries: Optional[List[str]] = None, simulate_failure: bool = False):
    return transform_events(df, blocked_countries or [], simulate_failure)


@task(name="load_task")
def load_task(df, output_path: str):
    load_to_parquet_partitioned(df, output_path)


@flow(name="etl-prefect-flow")
def etl_prefect_flow(
    input_path: str = "data/synthetic_events.csv",
    output_path: str = "output_prefect",
    blocked_countries: Optional[List[str]] = None,
    simulate_failure: bool = False,
    run_date: Optional[str] = None,
):
    df = extract_task(input_path)
    transformed = transform_task(df, blocked_countries, simulate_failure)
    load_task(transformed, output_path)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-date", required=False)
    parser.add_argument("--simulate-failure", action="store_true")
    args = parser.parse_args()

    etl_prefect_flow(
        input_path="data/synthetic_events.csv",
        output_path="output_prefect",
        blocked_countries=None,
        simulate_failure=args.simulate_failure,
        run_date=args.run_date,
    )
