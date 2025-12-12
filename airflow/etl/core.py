from pathlib import Path
import pandas as pd

def extract_csv(input_path: str) -> pd.DataFrame:
    """Extract: Read CSV input into DataFrame."""
    df = pd.read_csv(input_path)
    return df


def transform_events(
    df: pd.DataFrame,
    blocked_countries=None,
    simulate_failure: bool = False
) -> pd.DataFrame:
    """Transform: Clean, enrich and aggregate event data."""
    if blocked_countries is None:
        blocked_countries = []

    # simulate failure for Airflow retry demonstration
    if simulate_failure:
        raise RuntimeError("Simulated failure in transform step!")

    # remove blocked countries
    df = df[~df["country"].isin(blocked_countries)]

    # convert timestamp and add date column
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    # session duration per user
    session = df.groupby("user_id")["timestamp"].agg(["min", "max"])
    session["session_duration_minutes"] = (
        (session["max"] - session["min"]).dt.total_seconds() / 60.0
    )
    session = session[["session_duration_minutes"]].reset_index()

    # event count per user per day
    events_per_user_day = (
        df.groupby(["user_id", "date"])
          .size()
          .reset_index(name="event_count")
    )

    # merge session stats
    result = events_per_user_day.merge(session, on="user_id", how="left")
    return result


def load_to_parquet_partitioned(df: pd.DataFrame, output_path: str) -> None:
    """Load: Write partitioned parquet files by date."""
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    for date_value, df_part in df.groupby("date"):
        part_dir = output_dir / f"date={date_value}"
        part_dir.mkdir(parents=True, exist_ok=True)
        file_path = part_dir / "data.parquet"
        df_part.to_parquet(file_path, index=False)


def run_etl(
    input_path: str,
    output_path: str,
    blocked_countries=None,
    simulate_failure: bool = False,
    run_date: str = None
):
    """Standalone ETL runner for CLI debugging."""
    print("🚀 ETL started")
    print("📥 Input path:", input_path)
    print("📤 Output path:", output_path)
    if run_date:
        print("📅 run_date:", run_date)

    df = extract_csv(input_path)
    print("📊 Rows after extract:", len(df))

    transformed = transform_events(df, blocked_countries, simulate_failure)
    print("⚙️ Rows after transform:", len(transformed))

    load_to_parquet_partitioned(transformed, output_path)
    print("✅ Data written successfully")
