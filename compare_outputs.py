from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent

def load_all_outputs(subdir: str) -> pd.DataFrame:
    paths = [
        BASE / subdir / "date=2025-01-01" / "data.parquet",
        BASE / subdir / "date=2025-01-02" / "data.parquet",
    ]
    frames = [pd.read_parquet(p) for p in paths]
    df = pd.concat(frames, ignore_index=True)
    df = df.sort_values(["user_id", "date"]).reset_index(drop=True)
    return df

local_df   = load_all_outputs("output_local")
air_df     = load_all_outputs("output_airflow")
prefect_df = load_all_outputs("output_prefect")
dag_df     = load_all_outputs("output_dagster")

print("local vs airflow equal:",   local_df.equals(air_df))
print("local vs prefect equal:",   local_df.equals(prefect_df))
print("local vs dagster equal:",   local_df.equals(dag_df))
