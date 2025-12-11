# run_local_etl.py
from etl.core import run_etl

if __name__ == "__main__":
    run_etl("data/synthetic_events.csv", "output_local")
