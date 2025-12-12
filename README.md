# Comparative Analysis of Data Orchestration Frameworks

This project implements the same ETL pipeline using **Apache Airflow**, **Prefect**, and **Dagster**.  
All three orchestrators run identical ETL logic using a shared module (`etl/core.py`) to ensure **output parity**, **retry validation**, and **backfill functionality**.

---

# 📁 Repository Structure
├── airflow/ # Airflow DAG + Docker files
├── prefect/ # Prefect flow implementation
├── dagster/ # Dagster job implementation
├── etl/ # Shared ETL logic for all orchestrators
├── data/ # Input dataset synthetic_events.csv
├── output_local/ # Local ETL output
├── output_airflow/ # Airflow output
├── output_prefect/ # Prefect output
├── output_dagster/ # Dagster output
├── compare_outputs.py # Script to check output equality
├── README.md # Project overview
├── COMPARISON.md # Detailed comparison of Airflow, Prefect, Dagster

---

# 🧪 ETL Pipeline Overview

Each orchestrator runs the **same ETL logic**:

### ✔ **Extract**
Reads `synthetic_events.csv` into a DataFrame.

### ✔ **Transform**
- Removes blocked countries  
- Handles optional failure simulation  
- Cleans event fields  

### ✔ **Load**
Writes partitioned Parquet output:

output_path/date=YYYY-MM-DD/data.parquet

---

# 🚀 How to Run the Project

---

## 1️⃣ Local ETL Run (No orchestrator)
python run_local_etl.py

Output stored in `output_local/`.

---

## 2️⃣ Airflow Pipeline

### Start Airflow:

cd airflow
docker-compose up --build

Open UI → http://localhost:8080  
Enable DAG → **etl_airflow_dag**

### Trigger DAG:

airflow dags trigger etl_airflow_dag


### Backfill:

airflow dags backfill -s 2025-01-01 -e 2025-01-05 etl_airflow_dag

---

## 3️⃣ Prefect Pipeline

Run the flow:

python prefect/etl_prefect_flow.py

Backfill:

python prefect/etl_prefect_flow.py --backfill 5

Optional:

prefect server start
---

## 4️⃣ Dagster Pipeline

Start UI:

cd dagster
dagster dev


Open UI → http://localhost:3000  
Run job → **etl_dagster_job**

Backfill → Use Dagster UI partitions or CLI:

dagster job backfill -j etl_dagster_job -p 2025-01-01

---

# 📊 Output Parity Check

Run:
python compare_outputs.py

Expected Result:
local vs airflow: True
local vs prefect: True
local vs dagster: True

---

# 📘 Documentation Included

- **Root README.md** (this file)
- **COMPARISON.md** → Detailed framework analysis
- **airflow/README.md**
- **prefect/README.md**
- **dagster/README.md**

---

# 🎉 Final Notes

This project demonstrates:

- Workflow orchestration  
- Cross-framework ETL consistency  
- Retry logic  
- Backfill processing  
- Parquet data engineering  

You can directly run any orchestrator and reproduce identical outputs.
