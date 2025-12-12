APACHE AIRFLOW — ETL PIPELINE
=============================

This folder contains the Airflow DAG implementation of the ETL workflow.

------------------------------------------------------------
RUN AIRFLOW
------------------------------------------------------------

1. Open terminal and go to the airflow directory:
   cd airflow

2. Start Airflow using Docker:
   docker-compose up --build

3. Open Airflow UI:
   http://localhost:8080

4. Login credentials:
   Username: admin
   Password: admin

5. Enable the DAG:
   etl_airflow_dag

------------------------------------------------------------
TRIGGER DAG MANUALLY
------------------------------------------------------------

Command:
   airflow dags trigger etl_airflow_dag

------------------------------------------------------------
RUN BACKFILL (Required)
------------------------------------------------------------

Command:
   airflow dags backfill -s 2025-01-01 -e 2025-01-05 etl_airflow_dag

------------------------------------------------------------
OUTPUT LOCATION
------------------------------------------------------------

All processed files and results will be stored in:

   output_airflow/

------------------------------------------------------------
END OF AIRFLOW README
------------------------------------------------------------