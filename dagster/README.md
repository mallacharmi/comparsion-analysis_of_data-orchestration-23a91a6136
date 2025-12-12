DAGSTER — ETL JOB
=================

This directory contains the Dagster job definition for the ETL process.

------------------------------------------------------------
START DAGSTER UI
------------------------------------------------------------

Run the following command:
   dagster dev

Dagster UI:
   http://localhost:3000

------------------------------------------------------------
RUN JOB
------------------------------------------------------------

1. Open Dagster UI
2. Select: etl_dagster_job
3. Click: Launch Run

------------------------------------------------------------
RUN BACKFILL
------------------------------------------------------------

Option 1 (UI):
   Dagster UI → Backfill → Select partitions

Option 2 (CLI):
   dagster job backfill -j etl_dagster_job -p 2025-01-01

------------------------------------------------------------
END OF DAGSTER README
------------------------------------------------------------