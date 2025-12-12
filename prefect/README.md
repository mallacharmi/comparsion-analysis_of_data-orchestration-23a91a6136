PREFECT — ETL FLOW
==================

This directory contains the Prefect ETL implementation.

------------------------------------------------------------
RUN THE FLOW
------------------------------------------------------------

Command:
   python etl_prefect_flow.py

------------------------------------------------------------
BACKFILL
------------------------------------------------------------

Run the flow with backfill (example: last 5 days):
   python etl_prefect_flow.py --backfill 5

------------------------------------------------------------
OPTIONAL: RUN PREFECT SERVER
------------------------------------------------------------

Start Prefect server:
   prefect server start

Prefect Dashboard:
   http://127.0.0.1:4200

------------------------------------------------------------
END OF PREFECT README
------------------------------------------------------------