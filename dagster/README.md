\# Dagster — ETL Job

This directory contains the Dagster job definition for the ETL process.

---

\## 🚀 Start Dagster UI

dagster dev

UI: http://localhost:3000

---
\## ▶️ Run Job
\- Open Dagster UI  

\- Select \*\*etl\_dagster\_job\*\*

\- Click \*\*Launch Run\*\*

---

\## 📅 Run Backfill

Dagster UI → Backfill → Select partitions  

OR

dagster job backfill -j etl\_dagster\_job -p 2025-01-01

---

\# End of dagster README



