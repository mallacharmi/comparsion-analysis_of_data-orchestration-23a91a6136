# Comparative Analysis of Data Orchestration Frameworks

This project implements the same ETL pipeline using:
- Pure Python (local)
- Apache Airflow
- Prefect
- Dagster

## Project Structure

- `etl/` — shared ETL logic (`core.py`)
- `data/` — input CSV (`synthetic_events.csv`)
- `output_local/` — output from local Python script
- `output_airflow/` — output from Airflow DAG
- `output_prefect/` — output from Prefect flow
- `output_dagster/` — output from Dagster job
- `airflow_project/` — Airflow DAG and config
- `prefect_project/` — Prefect flow code
- `dagster_project/` — Dagster job code
- `report/` — comparison document, screenshots

## How to Run the Pipelines

### 1. Local Python

```bash
python run_local_etl.py
