```markdown

\# Apache Airflow — ETL Pipeline

This folder contains the Airflow DAG implementation of the ETL workflow.

---

\## 🚀 Run Airflow

cd airflow

docker-compose up --build

Airflow UI: http://localhost:8080  

Login: admin / admin  

Enable DAG: \*\*etl\_airflow\_dag\*\*

---

\## ▶️ Trigger DAG

airflow dags trigger etl\_airflow\_dag
--

\## 📅 Run Backfill (Required)

airflow dags backfill -s 2025-01-01 -e 2025-01-05 etl\_airflow\_dag
---

\## 📂 Output Location

output\_airflow/
---

\# End of airflow README

